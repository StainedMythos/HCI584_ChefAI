# ChefAI

## Overview

ChefAI is a recipe generator application that helps users find recipes based on their dietary preferences and available ingredients. Users can register, log in, set dietary restrictions, and generate recipes depending on foods available to them.

## Table of Contents

1. [Installation](#installation)
2. [Setup](#setup)
3. [Usage](#usage)
4. [Screenshots](#screenshots)
4. [Troubleshooting](#troubleshooting)
5. [Known Issues and Limitations](#known-issues-and-limitations)
6. [Developer Documentation](#developer-documentation)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/chefai.git
    cd chefai
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Setup

1. **API Key Setup:**
    - The project requires an API key for recipe generation, create a file named `API_keys.py` in the project directory with the following content (replace `YOUR_API_KEY` with your actual API key):

        ```python
        ApplicationKey = "YOUR_API_KEY"
        ApplicationID = "YOUR_API_ID"
        ```


2. **Create Necessary Files:**
    - Ensure that you have the following files in your project directory:
        - `users.json` (for storing user login information)
        - `user_preferences.json` (for storing user preferences)

    These files will be automatically created by the application if they do not exist.

## Usage

1. **Starting the Application:**
    - Run the login GUI to start the application:

        ```bash
        python login_gui.py
        ```

2. **Logging In:**
    - Enter your username and password to log in. If you are a new user, click on "New User - Register Here" to register.

3. **Registering a New User:**
    - Enter a new username, password, and confirm your password. Click "Register" to complete the registration.

4. **Generating Recipes:**
    - After logging in, you will be directed to the recipe generator window.
    - Enter your dietary preferences and available ingredients.
    - Click "Generate Recipe" to find recipes.

5. **User Profile:**
    - Access the user profile by selecting "User Profile" from the "Options" menu.
    - Set your dietary restrictions and save them for future use.

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

1. **Invalid Username or Password:**
    - Ensure that the username and password are correct.
    - If you forgot your password, there is no password recovery feature implemented.

2. **File Not Found Errors:**
    - Ensure that `users.json` and `user_preferences.json` are in the project directory.
    - These files should be created automatically by the application.

3. **API Key Errors:**
    - Ensure that your API key is correctly set in `API_keys.py`.
    - Check your internet connection.

## Known Issues and Limitations

- **Search History:** The search history feature is not yet implemented.
- **Error Handling:** Limited error handling for network issues and API errors.
- **User Preferences:** Preferences are saved locally and are not encrypted. These also save only per instance or session.

## Developer Documentation

For more detailed information on the project's code structure, API usage, and customization, refer to the [Developer Documentation](docs/developer_documentation.md).

---
