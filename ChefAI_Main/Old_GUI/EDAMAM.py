# simple SDK for EDAMAM API to support ChefAI app
import requests
from pprint import pprint
from API_keys import ApplicationID, ApplicationKey


def get_recipes(ingredients, num_recipes=3, dietary="None", health="None", cuisine="None", meal_type="None", dish_type="None", calories="None", time="None", excluded="None"):
    """
    Get recipes from the EDAMAM API.
    """
    # Set the base URL for the API
    base_url = "https://api.edamam.com/search"

    ningr = len(ingredients.split(","))
    ingr_range = f"{ningr}-{ningr+4}" # get up to 4 more ingredients in recipes
    if time == "None":
        time = "0-60"

    # Set the parameters for the API
    params = {
        "q": ingredients,
        "app_id": ApplicationID,
        "app_key": ApplicationKey,
        "ingr":ingr_range, # number of ingredients, 
        "from":0, "to":num_recipes, # return the first 3 recipes
        "time": time, # time in minutes, 
        "diet": dietary, # return only balanced recipes
        #"health":"peanut-free",
        #"calories":"500-900",
        #"excluded":"bell peppers",
        #"cuisineType":["American", "European"], # a list means either American or European
        #"dishType":"main course",
        #"mealType":["dinner", "lunch"],
        # return only these fields in the JSON results
        # label is the title of the recipe
        "field":["label","image", "calories","ingredientLines","yield", "totalTime", "url"],
        }   


    response = requests.get(base_url, params=params)
    response.raise_for_status()  
    #print(response.status_code)
    #print(response.url)

    result = response.json()
    recipes = result['hits']
    return recipes