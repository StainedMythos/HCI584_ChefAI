import click
from flask import Flask
from APIPullReq import get_db, EAPI, init_db

def create_app():
    # Initialize a Flask application
    app = Flask(__name__)
    
    # Initialize the database
    init_db(app)
    
    return app

app = create_app()

@click.command()
@click.option('--dietary', prompt='Dietary Preferences', help='Enter your dietary preferences.')
@click.option('--ingredients', prompt='Available Ingredients', help='Enter available ingredients.')
def input_preferences(dietary, ingredients):
    """
    Command-line interface to input dietary preferences and available ingredients.
    """
    with app.app_context():  # Set up the application context
        # Get the database connection
        db = get_db()
        
        # Insert the user inputs into the database
        db.execute('INSERT INTO user (dietary, ingredients) VALUES (?, ?)', (dietary, ingredients))
        db.commit()
        
        # Provide feedback to the user
        click.echo(f'Dietary Preferences: {dietary}, Ingredients: {ingredients} saved.')

if __name__ == '__main__':
    # Run the CLI
    input_preferences()

def generate_recipe(ingredients, dietary):
    """
    Generate a recipe based on available ingredients.
    """
    # Use the Edamam API to search for a recipe
    response = search_recipe(ingredients, dietary)
    
    if response:
        return response[0]['recipe']['label']
    return "No matching recipe found."

def search_recipe(ingredients, dietary):
    """
    Use the Edamam API to search for a recipe.
    """
    response = EAPI.search_recipe(q=ingredients, health=dietary)  # Adjust the API call parameters as needed
    if response:
        return response
    return None

def get_recipe_suggestion(user_id):
    """
    Retrieve a recipe suggestion for a user based on their inputs.
    """
    with app.app_context():  # Set up the application context
        db = get_db()
        user = db.execute('SELECT * FROM user WHERE id = ?', (user_id,)).fetchone()
        
        if user:
            ingredients = user['ingredients'].split(', ')
            return generate_recipe(ingredients, user['dietary'])
        
        return "User not found."



#import speech_recognition as sr

#def recognize_speech():
#    """
#    Recognize speech input from the user.
#    """
#    recognizer = sr.Recognizer()
    
#    with sr.Microphone() as source:
#        print("Say something:")
#        audio = recognizer.listen(source)
#    
#    try:
        # Recognize speech using Google's speech recognition
#        text = recognizer.recognize_google(audio)
#        print(f"You said: {text}")
#    except sr.UnknownValueError:
#        print("Sorry, I did not understand that.")
#    except sr.RequestError:
#        print("Could not request results; check your network connection.")

#if __name__ == '__main__':
    # Run the speech recognition function
#    recognize_speech()
