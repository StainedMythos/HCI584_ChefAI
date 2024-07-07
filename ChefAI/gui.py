import tkinter as tk
import json
from tkinter import messagebox
from APIPullReq import EAPI

class RecipeGUI:
    def __init__(self, master):
        self.master = master
        master.title("Recipe Generator")

        # Configure the grid
        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=3)

        # Create input fields
        self.dietary_label = tk.Label(master, text="Dietary Preferences:")
        self.dietary_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.dietary_entry = tk.Entry(master)
        self.dietary_entry.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=5)

        self.ingredients_label = tk.Label(master, text="Available Ingredients:")
        self.ingredients_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.ingredients_entry = tk.Entry(master)
        self.ingredients_entry.grid(row=1, column=1, sticky=tk.EW, padx=5, pady=5)

        # Create buttons
        self.generate_button = tk.Button(master, text="Generate Recipe", command=self.generate_recipe)
        self.generate_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.grid(row=3, column=0, columnspan=2, pady=10)

    def generate_recipe(self):
        ingredients = self.ingredients_entry.get()
        dietary = self.dietary_entry.get()
        recipe = EAPI.search_recipe(query=ingredients)
        with open('data.json', 'w') as f:
            json.dump(recipe, f, indent=2)
       
        if recipe:
            messagebox.showinfo("Recipe Suggestion", recipe['hits'][0]['recipe']['label'])
        else:
            messagebox.showinfo("Error", "No matching recipe found.")

root = tk.Tk()
my_gui = RecipeGUI(root)
root.mainloop()
