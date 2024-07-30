import tkinter as tk
import json
from tkinter import messagebox
from recipe_gui import RecipeGUI
from register_gui import RegisterGUI

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
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            with open('users.json', 'r') as f:
                users = json.load(f)
        except FileNotFoundError:
            users = {}

        if username in users and users[username] == password:
            self.master.destroy()
            main_app = tk.Tk()
            RecipeGUI(main_app)
            main_app.mainloop()
        else:
            messagebox.showerror("Login Error", "Invalid username or password")

    def open_register_window(self):
        self.master.withdraw()
        register_window = tk.Toplevel(self.master)
        RegisterGUI(register_window, self.master)

if __name__ == "__main__":
    root = tk.Tk()
    login_gui = LoginGUI(root)
    root.mainloop()
