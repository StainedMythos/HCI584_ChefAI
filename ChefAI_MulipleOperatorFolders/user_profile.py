import tkinter as tk
from tkinter import messagebox
import json

class UserProfileWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("User Profile")

        # Set minimum window size to prevent squishing
        self.minsize(600, 400)

        # Create a label to instruct users
        self.instruction_label = tk.Label(self, text="Please click on 'User Preferences' in the menu at the top left.", font=("Arial", 12))
        self.instruction_label.pack(pady=10, padx=10)

        # Create the menu
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)

        # Add the "User Profile" menu
        self.user_profile_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="User Preferences", menu=self.user_profile_menu)
        self.user_profile_menu.add_command(label="Diet Restrictions", command=self.show_diet_restrictions)
        self.user_profile_menu.add_command(label="Search History", command=self.show_search_history)
        self.user_profile_menu.add_command(label="Save Preferences", command=self.save_preferences)
        self.user_profile_menu.add_command(label="Load Preferences", command=self.load_preferences)

        # Initialize lists
        self.allergies_and_restrictions = sorted([
            "Alcohol", "Animal Products", "Cashews", "Celery", "Chili Peppers", "Chocolate", "Corn",
            "Eggs", "Fish", "Gluten", "Grapes", "Lactose", "Legumes", "Milk", "Nuts", "Peanuts",
            "Shellfish", "Soy", "Wheat"
        ])
        
        self.dietary_preferences = sorted([
            "Dairy-Free", "Gluten-Free", "Keto", "Low-Carb", "Low-FODMAP", "Mediterranean", "Paleo",
            "Pescatarian", "Raw", "Vegan", "Vegetarian"
        ])

        # Initialize content label for search history
        self.content_label = tk.Label(self, text="Search History: Not yet implemented.", font=("Arial", 12))
        self.content_label.pack(pady=10, padx=10)

        # Initialize variables for checkbuttons
        self.allergy_vars = {item: tk.BooleanVar() for item in self.allergies_and_restrictions}
        self.dietary_vars = {item: tk.BooleanVar() for item in self.dietary_preferences}

    def show_diet_restrictions(self):
        # Create a new top-level window for showing dietary restrictions
        diet_restrictions_window = tk.Toplevel(self)
        diet_restrictions_window.title("Diet Restrictions")

        # Add a frame to hold the checkbuttons for allergies and restrictions
        frame = tk.Frame(diet_restrictions_window)
        frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Create a label and checkbuttons for allergies and restrictions
        tk.Label(frame, text="Allergies and Restrictions:", font=("Arial", 12)).pack(anchor=tk.W)
        for item in self.allergies_and_restrictions:
            tk.Checkbutton(frame, text=item, variable=self.allergy_vars[item]).pack(anchor=tk.W)

        tk.Label(frame, text="Dietary Preferences:", font=("Arial", 12)).pack(anchor=tk.W)
        for item in self.dietary_preferences:
            tk.Checkbutton(frame, text=item, variable=self.dietary_vars[item]).pack(anchor=tk.W)

        # Add a button to confirm selections
        confirm_button = tk.Button(frame, text="Confirm", command=self.confirm_selections)
        confirm_button.pack(pady=10)

    def confirm_selections(self):
        selected_allergies = [item for item, var in self.allergy_vars.items() if var.get()]
        selected_dietary = [item for item, var in self.dietary_vars.items() if var.get()]

        # Display selected options for debugging or further processing
        print("Selected Allergies and Restrictions:", selected_allergies)
        print("Selected Dietary Preferences:", selected_dietary)

        # Optionally, you can store these selections or use them for filtering recipes
        messagebox.showinfo("Selections", f"Allergies and Restrictions: {selected_allergies}\nDietary Preferences: {selected_dietary}")

    def save_preferences(self):
        selected_allergies = [item for item, var in self.allergy_vars.items() if var.get()]
        selected_dietary = [item for item, var in self.dietary_vars.items() if var.get()]

        preferences = {
            'allergies': selected_allergies,
            'dietary': selected_dietary
        }

        try:
            with open('user_preferences.json', 'w') as f:
                json.dump(preferences, f)
            messagebox.showinfo("Save Preferences", "Preferences saved successfully.")
        except Exception as e:
            messagebox.showerror("Save Preferences", f"Error saving preferences: {e}")

    def load_preferences(self):
        try:
            with open('user_preferences.json', 'r') as f:
                preferences = json.load(f)
                
            for item, var in self.allergy_vars.items():
                var.set(item in preferences.get('allergies', []))
                
            for item, var in self.dietary_vars.items():
                var.set(item in preferences.get('dietary', []))

            messagebox.showinfo("Load Preferences", "Preferences loaded successfully.")
        except FileNotFoundError:
            messagebox.showerror("Load Preferences", "No saved preferences found.")
        except json.JSONDecodeError:
            messagebox.showerror("Load Preferences", "Error decoding preferences file.")
        except Exception as e:
            messagebox.showerror("Load Preferences", f"Error loading preferences: {e}")

    def show_search_history(self):
        # Placeholder for search history functionality
        self.content_label.config(text="Search History: Not yet implemented.")
