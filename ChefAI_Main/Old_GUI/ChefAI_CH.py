import tkinter as tk
import json
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from gui_plus_login import LoginGUI # change file name to login_gui.py
from EDAMAM import get_recipes
import webbrowser



class ChefAIapp(tk.Tk):
    def __init__(self):
        super().__init__() # init tk so we can use self as 
        self.title("Recipe Generator")

        self.geometry("510x650")

        # Create input fields
        self.dietary_label = tk.Label(self, text="Dietary Preferences:")
        self.dietary_label.grid(row=0, column=0, columnspan=2, pady=5, sticky=tk.EW)
        self.dietary_options = ["balanced", "high-fiber", "high-protein", "low-carb", "low-fat", "low-sodium"]
        self.dietary_var = tk.StringVar(self)  # this contains the seleced value!
        self.dietary_var.set("balanced")
        self.dietary_entry = tk.OptionMenu(self, self.dietary_var, *self.dietary_options)
        self.dietary_entry.grid(row=0, column=2, columnspan=2, pady=5, sticky=tk.EW)

        self.ingredients_label = tk.Label(self, text="Available Ingredients:")
        self.ingredients_label.grid(row=1, column=0, pady=5, sticky=tk.EW)
        self.ingredients_entry = tk.Entry(self)
        self.ingredients_entry.grid(row=1, column=1, columnspan=3, pady=5, sticky=tk.EW)

        # Create buttons
        self.generate_button = tk.Button(self, text="Generate Recipe", command=self.generate_recipe)
        self.generate_button.grid(row=2, column=3, columnspan=2, pady=5, sticky=tk.EW)

        # Text output for recipes
        self.recipe_text = ScrolledText(self, wrap=tk.WORD, width=60, height=30)
        self.recipe_text.grid(row=3, column=0, columnspan=4, pady=5, sticky=tk.EW)

        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.grid(row=4, column=1, columnspan=2, pady=10, sticky=tk.EW)
        
        # loop until the window is closed or quit botton is pressed
        self.mainloop()
    
    def quit(self):
        # save stuff?
        self.destroy()


    def generate_recipe(self):

        ingredients = self.ingredients_entry.get()
        dietary = self.dietary_var.get()
        
        # below commented out isn't working - supposed to collect a max of 10 recipes
        # recipe = EAPI.search_recipe(query=ingredients, from_=0, to=10)
        # Checks for recipes
        recipes = get_recipes(ingredients, dietary=dietary)

        if len(recipes) > 0:
            # for DEBUG
            with open('data.json', 'w') as f:
                json.dump(recipes, f, indent=2)
            
            # Clear the text box
            self.recipe_text.delete(1.0, tk.END)

            for r in recipes:
                self.recipe_text.insert(tk.INSERT, f"{r['recipe']['label']}\n")
                self.recipe_text.insert(tk.INSERT, f"Calories: {int(r['recipe']['calories'])}\n")
                self.recipe_text.insert(tk.INSERT, f"Time: {int(r['recipe']['totalTime'])} mins\n")
                self.recipe_text.insert(tk.INSERT, f"Cuisine: {r['recipe']['cuisineType'][0]}\n")
                self.recipe_text.insert(tk.INSERT, f"Meal type: {r['recipe']['mealType'][0]}\n")
                self.recipe_text.insert(tk.INSERT, f"Dish type: {r['recipe']['dishType'][0]}\n")
                self.recipe_text.insert(tk.INSERT, f"Dietary Preference: {r['recipe']['dietLabels'][0]}\n")
                self.recipe_text.insert(tk.INSERT, "Ingredients:\n")
                for ingr in r['recipe']['ingredientLines']:
                    self.recipe_text.insert(tk.INSERT, f" - {ingr}\n")
                self.recipe_text.insert(tk.INSERT, f"Yield: {int(r['recipe']['yield'])} portions\n")
                self.recipe_text.insert(tk.INSERT, '\n')    

        else:
            self.recipe_text.insert(tk.INSERT, "No recipes found\n")
            self.recipe_text.see(tk.END)

# MAIN

#root = tk.Tk()
#LoginGUI(root)
#root.mainloop()

ChefAIapp()

