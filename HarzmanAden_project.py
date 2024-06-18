from flask import Flask
from app.db import init_db

def create_app():
    # Initialize a Flask application
    app = Flask(__name__)
    
    # Initialize the database
    init_db(app)
    
    return app



import click
from app.db import get_db

@click.command()
@click.option('--dietary', prompt='Dietary Preferences', help='Enter your dietary preferences.')
@click.option('--ingredients', prompt='Available Ingredients', help='Enter available ingredients.')
def input_preferences(dietary, ingredients):
    """
    Command-line interface to input dietary preferences and available ingredients.
    """
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



import sqlite3
from flask import current_app, g

def get_db():
    """
    Get a database connection.
    """
    if 'db' not in g:
        # Connect to the SQLite database
        g.db = sqlite3.connect(
            'database.db',
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # Return rows as dictionaries
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    """
    Close the database connection.
    """
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db(app):
    """
    Initialize the database with the application context.
    """
    with app.app_context():
        db = get_db()
        with current_app.open_resource('schema.sql') as f:
            db.executescript(f.read().decode('utf8'))
    # Register the close_db function to be called when the app context ends
    app.teardown_appcontext(close_db)



def generate_recipe(ingredients):
    """
    Generate a recipe based on available ingredients.
    """
    # Hardcoded recipes for demonstration purposes
    recipes = {
        "quinoa salad": ["quinoa", "tomatoes", "spinach", "avocados"],
        "vegan wrap": ["tortilla", "spinach", "avocados", "tomatoes"]
    }
    
    # Match ingredients to recipes
    for recipe, req_ingredients in recipes.items():
        if all(item in ingredients for item in req_ingredients):
            return recipe
    
    return "No matching recipe found."

def get_recipe_suggestion(user_id):
    """
    Retrieve a recipe suggestion for a user based on their inputs.
    """
    db = get_db()
    user = db.execute('SELECT * FROM user WHERE id = ?', (user_id,)).fetchone()
    
    if user:
        ingredients = user['ingredients'].split(', ')
        return generate_recipe(ingredients)
    
    return "User not found."



import speech_recognition as sr

def recognize_speech():
    """
    Recognize speech input from the user.
    """
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)
    
    try:
        # Recognize speech using Google's speech recognition
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
    except sr.RequestError:
        print("Could not request results; check your network connection.")

if __name__ == '__main__':
    # Run the speech recognition function
    recognize_speech()
