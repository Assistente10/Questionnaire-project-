#!#!/usr/bin/env python3
"""
main.py - Main Entry Point for Greenwich University Quiz Application

This is the main module that starts the quiz application.
It first shows the login screen, then launches the quiz application.

Module Structure:
- main.py (this file) - Entry point that starts login app
- login_app.py - Contains the login form with user's exact code
- app.py - Contains the App class and quiz data
- quiz_components.py - Contains MainMenu and QuizPage classes

Usage:
    python main.py

Author: Greenwich University Project
"""

# Import the login application module
from login_app import run_login_app

def main():
    """
    Main function that starts the application with login.
    This function calls the login app which then launches the quiz.
    """
    print("=" * 50)
    print("Greenwich University Quiz Application")
    print("=" * 50)
    print("Starting login process...")
    print("Please enter your student information to continue.")
    print("=" * 50)

    # Run the login application
    # The login app will handle launching the quiz app after successful login
    run_login_app()

    print("=" * 50)
    print("Application session ended.")
    print("Thank you for using Greenwich University Quiz!")
    print("=" * 50)


if __name__ == "__main__":
    # This block runs only when this file is executed directly
    # It calls the main function to start the application with login
    main()
