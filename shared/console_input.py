"""Module for hanle console input"""
import logging

class UserInputHandler:
    """
    Handles user input from the console.
    """
    @staticmethod
    def get_integer_input(prompt):
        """
        Get an integer input from the user.

        Args:
            prompt (str): The prompt to display to the user.

        Returns:
            int: The integer entered by the user.
        """
        while True:
            try:
                user_input = input(prompt)
                return int(user_input)
            except ValueError:
                logging.error("Invalid input. Input is not an integer")

    @staticmethod
    def get_yes_no_input(prompt):
        """
        Get a yes/no input from the user.

        Args:
            prompt (str): The prompt to display to the user.

        Returns:
            str: 'yes' if the user enters 'yes', 'no' if the user enters 'no'.
        """
        while True:
            user_input = input(prompt).lower()
            if user_input in ('yes', 'no'):
                return user_input
            print("Please enter 'yes' or 'no")
