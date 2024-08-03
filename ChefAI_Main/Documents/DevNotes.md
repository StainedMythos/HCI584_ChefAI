# Developer Notes

## Overview

ChefAI is a recipe generator application that helps users find recipes based on their dietary preferences and available ingredients. Users can register, log in, set dietary restrictions, and generate recipes depending on foods available to them.

Login GUI: Handles user authentication.
Recipe GUI: Allows users to generate and view recipes based on input ingredients and dietary preferences.
Register GUI: Facilitates new user registration.
User Profile: Manages user dietary restrictions and preferences.



## Table of Contents

1. [Installation](#installation)
2. [Setup](#setup)
3. [Usage](#usage)
4. [Screenshots](#screenshots)
5. [Troubleshooting](#troubleshooting)
6. [Known Issues and Limitations](#known-issues-and-limitations)
7. [Developer Documentation](#developer-documentation)
8. [Future Work](#future-work)
9. [Ongoing Development](#ongoing-development)

## Project Cleanup and Structure

### Project Structure

Ensure your project is well-structured with clear and meaningful file names. The project structure should be as follows:

- `main_login_gui.py` - Entry point for the login GUI
- `recipe_gui.py` - Recipe GUI tool
- `register_gui.py` - User registration GUI
- `user_profile.py` - User profile management

### Running the Application

To start the application, run `main_login_gui.py`. This script initializes the login interface and serves as the entry point for the application.

### Installing as a Package

If you wish to create a pip-installable package, refer to the packaging documentation for Python. You can create a `setup.py` file and follow the instructions to package your project.

## In-Code Documentation

### Docstrings and Comments

Used docstrings and comments to make the code understandable and to
explain the purpose of each function.



## Installation
Clone the repository:
git clone https://github.com/yourusername/chefai.git
cd chefai

Install the required packages:
pip install -r requirements.txt



## Setup
API Key Setup:
The project requires an API key for recipe generation. Create a file named API_keys.py in the project directory with the following content (replace YOUR_API_KEY with your actual API key):

ApplicationKey = "YOUR_API_KEY"
ApplicationID = "YOUR_API_ID"


Create Necessary Files:
Ensure that you have the following files in your project directory:
users.json (for storing user login information)
user_preferences.json (for storing user preferences)
These files will be automatically created by the application if they do not exist.



## Usage
Starting the Application:

Run the login GUI to start the application:
python main_login_gui.py


Logging In:
Enter your username and password to log in. If you are a new user, click on "New User - Register Here" to register.

Registering a New User:
Enter a new username, password, and confirm your password. Click "Register" to complete the registration.

Generating Recipes:
After logging in, you will be directed to the recipe generator window.
Enter your dietary preferences and available ingredients.
Click "Generate Recipe" to find recipes.

User Profile:
Access the user profile by selecting "User Profile" from the "Options" menu.
Set your dietary restrictions and save them for future use.



## Screenshots
#### Login Screen
    - Log into the app
![Login Screen](screenshots/login_screen.png)

    - If this is your first time ever logging in, click register. Enter
    your username, password, and confirm your password. Click "Register" to complete the registration

#### Registration Screen
![Register Screen](screenshots/register_screen.png)

    - Enter your desired username and password

#### Recipe Generator
![Recipe Generator](screenshots/recipe_generator.png)

#### User Options
![User Options](screenshots/options_screen.png)
    - Click here to initialize preferences

#### User Main Menu
![User Main Menu](screenshots/user_profile_menu.png)
    - Here's the nesting page for the user restrictions and preferences.


#### User Preference Drop Down
![User Preference Drop Down](screenshots/user_profile_dropdown.png)
    - Here's the drop down for the different options. Again, the saved and loaded preferences, only saves the most recent, in the current session.


## Troubleshooting
If you encounter any issues while using the app, please refer to the following troubleshooting guide:

### Invalid Username or Password:
Ensure that the username and password are correct.
If you forgot your password, there is no password recovery feature implemented.

### File Not Found Errors:

Ensure that users.json and user_preferences.json are in the project directory.
These files should be created automatically by the application.

### API Key Errors:
Ensure that your API key is correctly set in API_keys.py file.
Check your internet connection.
Known Issues and Limitations
Search History: The search history feature is not yet implemented.

Error Handling: Limited error handling for network issues and API errors.

User Preferences: Preferences are saved locally and are not encrypted. These also save only per instance or session.



## Future  Work
- Implement more detailed user profiles with additional dietary options.
- Optimize recipe search for performance improvements.
- Add error handling for file operations.

## Ongoing Development
- Consider adding unit tests for each GUI component.
- Implement logging to track user interactions and errors.