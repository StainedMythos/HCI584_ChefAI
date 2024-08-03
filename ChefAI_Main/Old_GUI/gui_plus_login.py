import tkinter as tk
import json
from tkinter import messagebox
from APIPullReq import EAPI
import webbrowser


class MainMenu:
    def __init__(self, master):
        self.master = master
        master.title("Main Menu")
        master.configure(bg="white")

        # Set minimum window size to prevent squishing
        master.minsize(400, 300)

        # Configure the grid to auto-center elements with equal spacing
        for i in range(6):  # Adjust the range for the number of buttons
            master.columnconfigure(i, weight=1)
            master.rowconfigure(i, weight=1)

        # Add buttons for different options
        self.profile_button = tk.Button(master, text="User Profile", command=self.open_user_profile)
        self.profile_button.grid(row=0, column=1, columnspan=4, pady=10, sticky=tk.EW)

        self.budgeting_button = tk.Button(master, text="Budgeting Restrictions", command=self.open_budgeting_window)
        self.budgeting_button.grid(row=1, column=1, columnspan=4, pady=10, sticky=tk.EW)

        self.recipe_generator_button = tk.Button(master, text="Recipe Generator", command=self.open_recipe_generator)
        self.recipe_generator_button.grid(row=2, column=1, columnspan=4, pady=10, sticky=tk.EW)

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.grid(row=3, column=1, columnspan=4, pady=10, sticky=tk.EW)

    def open_user_profile(self):
        UserProfile(tk.Toplevel(self.master))

    def open_budgeting_window(self):
        BudgetingRestrictions(tk.Toplevel(self.master))

    def open_recipe_generator(self):
        self.master.destroy()
        main_app = tk.Tk()
        RecipeGUI(main_app)
        main_app.mainloop()


class UserProfile:
    def __init__(self, master):
        self.master = master
        master.title("User Profile")
        master.configure(bg="white")

        # Set minimum window size to prevent squishing
        master.minsize(600, 400)

        # Create buttons for different profile options
        self.dietary_button = tk.Button(master, text="Dietary Restrictions", command=self.open_dietary_window)
        self.dietary_button.pack(pady=10, fill=tk.X)

        self.favorite_foods_button = tk.Button(master, text="Favorite Foods", command=self.open_favorite_foods_window)
        self.favorite_foods_button.pack(pady=10, fill=tk.X)

        self.medical_info_button = tk.Button(master, text="Medical Information", command=self.open_medical_info_window)
        self.medical_info_button.pack(pady=10, fill=tk.X)

        self.budgeting_button = tk.Button(master, text="Budgeting Restrictions", command=self.open_budgeting_window)
        self.budgeting_button.pack(pady=10, fill=tk.X)

        self.history_button = tk.Button(master, text="History", command=self.open_history_window)
        self.history_button.pack(pady=10, fill=tk.X)

    def open_dietary_window(self):
        DietaryRestrictions(tk.Toplevel(self.master))

    def open_favorite_foods_window(self):
        FavoriteFoods(tk.Toplevel(self.master))

    def open_medical_info_window(self):
        MedicalInformation(tk.Toplevel(self.master))

    def open_budgeting_window(self):
        BudgetingRestrictions(tk.Toplevel(self.master))

    def open_history_window(self):
        History(tk.Toplevel(self.master))


class RecipeWindow(tk.Toplevel):
    def __init__(self, recipes):
        super().__init__()
        self.title("Recipe Suggestions")
        self.configure(bg="white")

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
            label = tk.Label(self.scrollable_frame, text=recipe['label'], wraplength=500)
            label.grid(row=row, column=0, columnspan=6, pady=2, sticky=tk.W)
            row += 1

            ingredient_label = tk.Label(self.scrollable_frame, text="Ingredients:")
            ingredient_label.grid(row=row, column=0, pady=2, sticky=tk.W)
            ingredients = "\n".join(recipe['ingredientLines'])
            ingredient_text = tk.Text(self.scrollable_frame, height=3, width=50)
            ingredient_text.insert(tk.END, ingredients)
            ingredient_text.grid(row=row, column=1, columnspan=5, pady=2, sticky=tk.W)
            ingredient_text.config(state=tk.DISABLED)
            row += 1

            calories_label = tk.Label(self.scrollable_frame, text=f"Calories: {recipe['calories']}")
            calories_label.grid(row=row, column=0, pady=2, sticky=tk.W)
            row += 1

            url_label = tk.Label(self.scrollable_frame, text="URL:")
            url_label.grid(row=row, column=0, pady=2, sticky=tk.W)

            url_text = tk.Text(self.scrollable_frame, height=1, width=50, bg=self.cget('bg'), relief="flat")
            url_text.insert(tk.END, recipe['url'])
            url_text.grid(row=row, column=1, columnspan=5, pady=2, sticky=tk.W)
            url_text.tag_config("hyperlink", foreground="blue", underline=1)
            url_text.tag_bind("hyperlink", "<Button-1>", lambda e, url=recipe['url']: self.open_url(url))
            url_text.config(state=tk.DISABLED)
            row += 1

    def open_url(self, url):
        webbrowser.open_new(url)


class LoginGUI:
    def __init__(self, master):
        self.master = master
        master.title("Login")
        master.configure(bg="white")

        # Set minimum window size to prevent squishing
        master.minsize(300, 200)

        # Configure the grid to auto-center elements with equal spacing
        for i in range(5):
            master.columnconfigure(i, weight=1)
            master.rowconfigure(i, weight=1)

        # Load and place the image
        self.logo = tk.PhotoImage(file="ChefAI_Icon.png")
        self.logo_label = tk.Label(master, image=self.logo)
        self.logo_label.grid(row=0, column=0, columnspan=5, pady=10)

        # Create and place the username label and entry field
        self.username_label = tk.Label(master, text="Username:")
        self.username_label.grid(row=1, column=0, columnspan=2, pady=5, sticky=tk.EW)
        self.username_entry = tk.Entry(master)
        self.username_entry.grid(row=1, column=2, columnspan=2, pady=5, sticky=tk.EW)

        # Create and place the password label and entry field
        self.password_label = tk.Label(master, text="Password:")
        self.password_label.grid(row=2, column=0, columnspan=2, pady=5, sticky=tk.EW)
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.grid(row=2, column=2, columnspan=2, pady=5, sticky=tk.EW)

        # Create and place the login button
        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.grid(row=3, column=1, columnspan=3, pady=10, sticky=tk.EW)

        # Create and place the register button
        self.register_button = tk.Button(master, text="New User - Register Here", command=self.open_register_window)
        self.register_button.grid(row=4, column=1, columnspan=3, pady=10, sticky=tk.EW)

        # Create and place the quit button
        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.grid(row=5, column=1, columnspan=3, pady=10, sticky=tk.EW)

    def login(self):
        # Get username and password from the entry fields
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Try to load the users from the JSON file, if it doesn't exist, create an empty dictionary
        try:
            with open('users.json', 'r') as f:
                users = json.load(f)
        except FileNotFoundError:
            users = {}

        # Check if the username and password match
        if username in users and users[username] == password:
            # If they match, destroy the login window and open the main menu
            self.master.destroy()
            main_menu = tk.Tk()
            MainMenu(main_menu)
            main_menu.mainloop()
        else:
            # If they don't match, show an error message
            messagebox.showerror("Login Error", "Invalid username or password.")

    def open_register_window(self):
        RegisterWindow(tk.Toplevel(self.master))


class RegisterWindow:
    def __init__(self, master):
        self.master = master
        master.title("Register")
        master.configure(bg="white")

        # Set minimum window size to prevent squishing
        master.minsize(300, 200)

        # Create and place the username label and entry field
        self.username_label = tk.Label(master, text="Username:")
        self.username_label.pack(pady=5, anchor=tk.W)
        self.username_entry = tk.Entry(master)
        self.username_entry.pack(pady=5, fill=tk.X)

        # Create and place the password label and entry field
        self.password_label = tk.Label(master, text="Password:")
        self.password_label.pack(pady=5, anchor=tk.W)
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack(pady=5, fill=tk.X)

        # Create and place the register button
        self.register_button = tk.Button(master, text="Register", command=self.register)
        self.register_button.pack(pady=10)

        # Create and place the quit button
        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack(pady=10)

    def register(self):
        # Get username and password from the entry fields
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Try to load the users from the JSON file, if it doesn't exist, create an empty dictionary
        try:
            with open('users.json', 'r') as f:
                users = json.load(f)
        except FileNotFoundError:
            users = {}

        # Check if the username already exists
        if username in users:
            messagebox.showerror("Registration Error", "Username already exists.")
        else:
            # If the username doesn't exist, add it to the dictionary and save to the JSON file
            users[username] = password
            with open('users.json', 'w') as f:
                json.dump(users, f)
            messagebox.showinfo("Registration Successful", "You have been registered successfully.")
            self.master.destroy()
            login_window = tk.Tk()
            LoginGUI(login_window)
            login_window.mainloop()


class DietaryRestrictions:
    def __init__(self, master):
        self.master = master
        master.title("Dietary Restrictions")
        master.configure(bg="white")

        # Set minimum window size to prevent squishing
        master.minsize(300, 200)

        # Create and place the restriction label and entry field
        self.restriction_label = tk.Label(master, text="Enter your dietary restrictions:")
        self.restriction_label.pack(pady=10)
        self.restriction_entry = tk.Entry(master)
        self.restriction_entry.pack(pady=10, fill=tk.X)

        # Create and place the save button
        self.save_button = tk.Button(master, text="Save", command=self.save_restriction)
        self.save_button.pack(pady=10)

        # Create and place the quit button
        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack(pady=10)

    def save_restriction(self):
        restriction = self.restriction_entry.get()
        # Save the restriction to a file or database
        with open('dietary_restrictions.txt', 'w') as f:
            f.write(restriction)
        messagebox.showinfo("Saved", "Your dietary restriction has been saved.")


class FavoriteFoods:
    def __init__(self, master):
        self.master = master
        master.title("Favorite Foods")
        master.configure(bg="white")

        # Set minimum window size to prevent squishing
        master.minsize(300, 200)

        # Create and place the food label and entry field
        self.food_label = tk.Label(master, text="Enter your favorite foods (comma-separated):")
        self.food_label.pack(pady=10)
        self.food_entry = tk.Entry(master)
        self.food_entry.pack(pady=10, fill=tk.X)

        # Create and place the save button
        self.save_button = tk.Button(master, text="Save", command=self.save_foods)
        self.save_button.pack(pady=10)

        # Create and place the quit button
        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack(pady=10)

    def save_foods(self):
        foods = self.food_entry.get()
        # Save the foods to a file or database
        with open('favorite_foods.txt', 'w') as f:
            f.write(foods)
        messagebox.showinfo("Saved", "Your favorite foods have been saved.")


class MedicalInformation:
    def __init__(self, master):
        self.master = master
        master.title("Medical Information")
        master.configure(bg="white")

        # Set minimum window size to prevent squishing
        master.minsize(300, 200)

        # Create and place the medical info label and entry field
        self.medical_info_label = tk.Label(master, text="Enter your medical information:")
        self.medical_info_label.pack(pady=10)
        self.medical_info_entry = tk.Entry(master)
        self.medical_info_entry.pack(pady=10, fill=tk.X)

        # Create and place the save button
        self.save_button = tk.Button(master, text="Save", command=self.save_medical_info)
        self.save_button.pack(pady=10)

        # Create and place the quit button
        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack(pady=10)

    def save_medical_info(self):
        medical_info = self.medical_info_entry.get()
        # Save the medical information to a file or database
        with open('medical_info.txt', 'w') as f:
            f.write(medical_info)
        messagebox.showinfo("Saved", "Your medical information has been saved.")


class BudgetingRestrictions:
    def __init__(self, master):
        self.master = master
        master.title("Budgeting Restrictions")
        master.configure(bg="white")

        # Set minimum window size to prevent squishing
        master.minsize(300, 200)

        # Create and place the budget label and entry field
        self.budget_label = tk.Label(master, text="Enter your budgeting restrictions:")
        self.budget_label.pack(pady=10)
        self.budget_entry = tk.Entry(master)
        self.budget_entry.pack(pady=10, fill=tk.X)

        # Create and place the save button
        self.save_button = tk.Button(master, text="Save", command=self.save_budget)
        self.save_button.pack(pady=10)

        # Create and place the quit button
        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack(pady=10)

    def save_budget(self):
        budget = self.budget_entry.get()
        # Save the budget to a file or database
        with open('budgeting_restrictions.txt', 'w') as f:
            f.write(budget)
        messagebox.showinfo("Saved", "Your budgeting restrictions have been saved.")


class History:
    def __init__(self, master):
        self.master = master
        master.title("History")
        master.configure(bg="white")

        # Set minimum window size to prevent squishing
        master.minsize(600, 400)

        # Create a text widget to display the history
        self.history_text = tk.Text(master, wrap=tk.WORD)
        self.history_text.pack(expand=True, fill=tk.BOTH)

        # Load history from file and display it
        self.load_history()

        # Create and place the quit button
        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack(pady=10)

    def load_history(self):
        try:
            with open('history.json', 'r') as f:
                history = json.load(f)
            for entry in history:
                self.history_text.insert(tk.END, f"Recipe: {entry['recipe']}\n")
                self.history_text.insert(tk.END, f"URL: {entry['url']}\n")
                self.history_text.insert(tk.END, f"Search Restrictions: {entry['search_restrictions']}\n")
                self.history_text.insert(tk.END, f"Foods Used: {', '.join(entry['foods_used'])}\n")
                self.history_text.insert(tk.END, "-"*40 + "\n")
        except FileNotFoundError:
            self.history_text.insert(tk.END, "No history found.")


class RecipeGUI:
    def __init__(self, master):
        self.master = master
        master.title("Recipe Generator")

        # Set minimum window size to prevent squishing
        master.minsize(400, 300)

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

        self.quit_button = tk.Button(master, text="Back", command=self.quit)
        self.quit_button.grid(row=3, column=1, columnspan=2, pady=10, sticky=tk.EW)

    def generate_recipe(self):
        ingredients = self.ingredients_entry.get()
        dietary = self.dietary_entry.get()
        
        # Checks for recipes
        recipe = EAPI.search_recipe(query=ingredients)
        with open('data.json', 'w') as f:
            json.dump(recipe, f, indent=2)

        if recipe:
            # Display the recipes in a new window
            RecipeWindow(recipe)
        else:
            # Display an error message if no recipes were found
            messagebox.showinfo("Error", "No matching recipe found.")

    def quit(self):
        # Close the current window
        self.master.destroy()


class MainMenu:
    def __init__(self, master):
        self.master = master
        master.title("Main Menu")
        master.configure(bg="white")

        # Set minimum window size to prevent squishing
        master.minsize(300, 200)

        # Create and place the recipe button
        self.recipe_button = tk.Button(master, text="Generate Recipe", command=self.open_recipe_gui)
        self.recipe_button.pack(pady=10)

        # Create and place the dietary restrictions button
        self.dietary_restrictions_button = tk.Button(master, text="Dietary Restrictions", command=self.open_dietary_restrictions)
        self.dietary_restrictions_button.pack(pady=10)

        # Create and place the favorite foods button
        self.favorite_foods_button = tk.Button(master, text="Favorite Foods", command=self.open_favorite_foods)
        self.favorite_foods_button.pack(pady=10)

        # Create and place the medical information button
        self.medical_information_button = tk.Button(master, text="Medical Information", command=self.open_medical_information)
        self.medical_information_button.pack(pady=10)

        # Create and place the budgeting restrictions button
        self.budgeting_restrictions_button = tk.Button(master, text="Budgeting Restrictions", command=self.open_budgeting_restrictions)
        self.budgeting_restrictions_button.pack(pady=10)

        # Create and place the history button
        self.history_button = tk.Button(master, text="History", command=self.open_history)
        self.history_button.pack(pady=10)

        # Create and place the quit button
        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack(pady=10)

    def open_recipe_gui(self):
        RecipeGUI(tk.Toplevel(self.master))

    def open_dietary_restrictions(self):
        DietaryRestrictions(tk.Toplevel(self.master))

    def open_favorite_foods(self):
        FavoriteFoods(tk.Toplevel(self.master))

    def open_medical_information(self):
        MedicalInformation(tk.Toplevel(self.master))

    def open_budgeting_restrictions(self):
        BudgetingRestrictions(tk.Toplevel(self.master))

    def open_history(self):
        History(tk.Toplevel(self.master))


if __name__ == "__main__":
    root = tk.Tk()
    LoginGUI(root)
    root.mainloop()
