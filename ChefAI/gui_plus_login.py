import tkinter as tk
import json
from tkinter import messagebox
#from APIPullReq import EAPI


class LoginGUI:
    def __init__(self, master):
        self.master = master
        master.title("Login")

        # Set minimum window size to prevent squishing
        master.minsize(300, 200)

        # Configure the grid to auto-center elements with equal spacing
        for i in range(5):
            master.columnconfigure(i, weight=1)
            master.rowconfigure(i, weight=1)

        # Create and place the username label and entry field
        self.username_label = tk.Label(master, text="Username:")
        self.username_label.grid(row=0, column=0, columnspan=2, pady=5, sticky=tk.EW)
        self.username_entry = tk.Entry(master)
        self.username_entry.grid(row=0, column=2, columnspan=2, pady=5, sticky=tk.EW)

        # Create and place the password label and entry field
        self.password_label = tk.Label(master, text="Password:")
        self.password_label.grid(row=1, column=0, columnspan=2, pady=5, sticky=tk.EW)
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.grid(row=1, column=2, columnspan=2, pady=5, sticky=tk.EW)

        # Create and place the login button
        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.grid(row=2, column=1, columnspan=3, pady=10, sticky=tk.EW)

        # Create and place the register button
        self.register_button = tk.Button(master, text="New User - Register Here", command=self.open_register_window)
        self.register_button.grid(row=3, column=1, columnspan=3, pady=10, sticky=tk.EW)

        # Create and place the quit button
        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.grid(row=4, column=1, columnspan=3, pady=10, sticky=tk.EW)


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
            # If they match, destroy the login window and open the main application
            self.master.destroy()
        
            #main_app = tk.Tk()
            #RecipeGUI(main_app)
            #main_app.mainloop()
        else:
            # If they don't match, show an error message
            messagebox.showerror("Login Error", "Invalid username or password")

    def open_register_window(self):
        # Hide the login window and open the register window
        self.master.withdraw()
        register_window = tk.Toplevel(self.master)
        RegisterGUI(register_window, self.master)

class RegisterGUI:
    def __init__(self, master, parent):
        self.master = master
        self.parent = parent
        master.title("Register")

        # Set minimum window size to prevent squishing
        master.minsize(300, 200)

        # Configure the grid to auto-center elements with equal spacing
        for i in range(5):
            master.columnconfigure(i, weight=1)
            master.rowconfigure(i, weight=1)

        # Create and place the new username label and entry field
        self.username_label = tk.Label(master, text="New Username:")
        self.username_label.grid(row=0, column=0, columnspan=2, pady=5, sticky=tk.EW)
        self.username_entry = tk.Entry(master)
        self.username_entry.grid(row=0, column=2, columnspan=2, pady=5, sticky=tk.EW)

        # Create and place the new password label and entry field
        self.password_label = tk.Label(master, text="New Password:")
        self.password_label.grid(row=1, column=0, columnspan=2, pady=5, sticky=tk.EW)
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.grid(row=1, column=2, columnspan=2, pady=5, sticky=tk.EW)

        # Create and place the confirm password label and entry field
        self.confirm_password_label = tk.Label(master, text="Confirm Password:")
        self.confirm_password_label.grid(row=2, column=0, columnspan=2, pady=5, sticky=tk.EW)
        self.confirm_password_entry = tk.Entry(master, show="*")
        self.confirm_password_entry.grid(row=2, column=2, columnspan=2, pady=5, sticky=tk.EW)

        # Create and place the register button
        self.register_button = tk.Button(master, text="Register", command=self.register)
        self.register_button.grid(row=3, column=1, columnspan=3, pady=10, sticky=tk.EW)

        # Create and place the cancel button
        self.cancel_button = tk.Button(master, text="Cancel", command=self.cancel)
        self.cancel_button.grid(row=4, column=1, columnspan=3, pady=10, sticky=tk.EW)

    def register(self):
        # Get username, password, and confirm password from the entry fields
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        
        # Try to load the users from the JSON file, if it doesn't exist, create an empty dictionary
        try:
            with open('users.json', 'r') as f:
                users = json.load(f)
        except FileNotFoundError:
            users = {}

        # Check if the username already exists
        if username in users:
            messagebox.showerror("Register Error", "Username already exists")
        # Check if the passwords match
        elif password != confirm_password:
            messagebox.showerror("Register Error", "Passwords do not match")
        else:
            # Add the new user to the dictionary and save it to the JSON file
            users[username] = password
            with open('users.json', 'w') as f:
                json.dump(users, f, indent=2)
            messagebox.showinfo("Register Success", "Registration successful")
            self.master.destroy()
            self.parent.deiconify()  # Show the login window again

    def cancel(self):
        # Destroy the register window and show the login window again
        self.master.destroy()
        self.parent.deiconify()

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

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.grid(row=3, column=1, columnspan=2, pady=10, sticky=tk.EW)

    def generate_recipe(self):
        ingredients = self.ingredients_entry.get()
        dietary = self.dietary_entry.get()
        
        # below commented out isn't working - supposed to collect a max of 10 recipes
        # recipe = EAPI.search_recipe(query=ingredients, from_=0, to=10)
        # Checks for recipes
        recipe = EAPI.search_recipe(query=ingredients)
        with open('data.json', 'w') as f:
            json.dump(recipe, f, indent=2)

        if recipe:
        
        # Display the recipe suggestions in a message box
            messagebox.showinfo("Recipe Suggestion", recipe['hits'][0]['recipe']['label'])
        else:
        # Display an error message if no recipes were found

            messagebox.showinfo("Error", "No matching recipe found.")

if __name__ == "__main__":
    root = tk.Tk()
    login_gui = LoginGUI(root)
    root.mainloop()
