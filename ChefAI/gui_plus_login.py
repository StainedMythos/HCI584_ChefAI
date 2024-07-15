import tkinter as tk
import json
from tkinter import messagebox
from APIPullReq import EAPI
import webbrowser

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
            # If they match, destroy the login window and open the main application
            self.master.destroy()
            main_app = tk.Tk()
            RecipeGUI(main_app)
            main_app.mainloop()
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

if __name__ == "__main__":
    root = tk.Tk()
    login_gui = LoginGUI(root)
    root.mainloop()
