import tkinter as tk
from tkinter import messagebox
import json
import webbrowser
from APIPullReq import EAPI
from user_profile import UserProfileWindow  # Ensure you import the UserProfileWindow class

class RecipeGUI:
    def __init__(self, master):
        self.master = master
        master.title("Recipe Generator")

        # Set minimum window size to prevent squishing
        master.minsize(400, 300)

        # Create the menu
        self.menu = tk.Menu(master)
        master.config(menu=self.menu)

        # Add the "Options" menu
        self.options_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Options", menu=self.options_menu)
        self.options_menu.add_command(label="User Profile", command=self.open_user_profile)
        self.options_menu.add_command(label="Recipe Generator", command=self.open_recipe_generator)
        self.options_menu.add_separator()
        self.options_menu.add_command(label="Quit", command=master.quit)

        # Configure the grid to auto-center elements with equal spacing
        for i in range(4):
            master.columnconfigure(i, weight=1)
            master.rowconfigure(i, weight=1)

        # Create input fields
        self.dietary_label = tk.Label(master, text="Dietary Preferences:")
        self.dietary_label.grid(row=0, column=0, columnspan=2, pady=5, sticky=tk.EW)
        self.dietary_entry = tk.Entry(master)
        self.dietary_entry.grid(row=0, column=2, columnspan=2, pady=5, sticky=tk.EW)

        self.ingredients_label = tk.Label(master, text="Available Ingredients:")
        self.ingredients_label.grid(row=1, column=0, columnspan=2, pady=5, sticky=tk.EW)
        self.ingredients_entry = tk.Entry(master)
        self.ingredients_entry.grid(row=1, column=2, columnspan=2, pady=5, sticky=tk.EW)

        # Create buttons
        self.generate_button = tk.Button(master, text="Generate Recipe", command=self.generate_recipe)
        self.generate_button.grid(row=2, column=1, columnspan=2, pady=10, sticky=tk.EW)

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.grid(row=3, column=1, columnspan=2, pady=10, sticky=tk.EW)

    def generate_recipe(self):
        ingredients = self.ingredients_entry.get()
        dietary = self.dietary_entry.get()
        
        # Retrieve dietary restrictions
        user_restrictions = self.get_user_restrictions()

        # Perform the recipe search with restrictions
        recipe = EAPI.search_recipe(query=ingredients)
        
        with open('data.json', 'w') as f:
            json.dump(recipe, f, indent=2)

        if recipe:
            # Display the recipes in a new window
            RecipeWindow(recipe)
        else:
            # Display an error message if no recipes were found
            messagebox.showinfo("Error", "No matching recipe found.")

    def get_user_restrictions(self):
        """
        Retrieve user restrictions from the UserProfileWindow or a similar place.
        """
        # This is just an example; adapt based on your actual implementation
        return {
            'diet': 'low-carb',
            'health': 'gluten-free'
        }

    def open_user_profile(self):
        UserProfileWindow()

    def open_recipe_generator(self):
        self.master.deiconify()


class RecipeWindow(tk.Toplevel):
    def __init__(self, recipes):
        super().__init__()
        self.title("Recipe Suggestions")

        # Set minimum window size to prevent squishing
        self.minsize(600, 400)

        # Create a canvas and a scrollbar
        self.canvas = tk.Canvas(self)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        row = 0
        for hit in recipes['hits'][:10]:  # Display the first 10 hits
            recipe = hit['recipe']
            label = tk.Label(self.scrollable_frame, text=recipe['label'], wraplength=500, fg="blue")
            label.grid(row=row, column=0, columnspan=6, pady=2, sticky=tk.W)
            label.bind("<Double-Button-1>", lambda e, url=recipe['url']: self.open_url(url))
            row += 1

            ingredient_label = tk.Label(self.scrollable_frame, text="Ingredients:")
            ingredient_label.grid(row=row, column=0, pady=2, sticky=tk.W)
            ingredients = "\n".join(recipe['ingredientLines'])
            ingredient_text = tk.Text(self.scrollable_frame, height=3, width=50)
            ingredient_text.insert(tk.END, ingredients)
            ingredient_text.grid(row=row, column=1, columnspan=5, pady=2, sticky=tk.W)
            ingredient_text.config(state=tk.DISABLED)
            row += 1

            # CH using int() on calories
            calories_label = tk.Label(self.scrollable_frame, text=f"Calories: {int(recipe['calories'])}")
            calories_label.grid(row=row, column=0, pady=2, sticky=tk.W)
            row += 1

    def open_url(self, url):
        webbrowser.open_new(url)
