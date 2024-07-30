import tkinter as tk
import json
from tkinter import messagebox

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
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        try:
            with open('users.json', 'r') as f:
                users = json.load(f)
        except FileNotFoundError:
            users = {}

        if username in users:
            messagebox.showerror("Register Error", "Username already exists")
        elif password != confirm_password:
            messagebox.showerror("Register Error", "Passwords do not match")
        else:
            users[username] = password
            with open('users.json', 'w') as f:
                json.dump(users, f, indent=2)
            messagebox.showinfo("Register Success", "Registration successful")
            self.master.destroy()
            self.parent.deiconify()

    def cancel(self):
        self.master.destroy()
        self.parent.deiconify()
