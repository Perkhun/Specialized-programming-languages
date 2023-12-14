"""
Module for creating the CalculatorUI class and UI related functionalities.
"""
class UserInterface:
    """
    Class for creating the calculator user interface.
    """
    @staticmethod
    def preview_ascii_art(ascii_art):
        """
        Display a preview of ASCII art.

        Parameters:
            ascii_art (str): The ASCII art to be previewed.
        """
        print("Preview of ASCII art:")
        print(ascii_art)
        input("Press Enter to continue...")

    @staticmethod
    def display_available_fonts(available_fonts):
        """
        Display available fonts.

        Parameters:
            available_fonts (list): List of available fonts.
        """
        print("Available fonts:")
        for font in available_fonts:
            print(font)

    @staticmethod
    def display_available_colors(available_colors):
        """
        Display available colors.

        Parameters:
            available_colors (list): List of available colors.
        """
        print("Available colors:")
        for color in available_colors:
            print(color)

    @staticmethod
    def get_user_input(prompt):
        """
        Get user input with a prompt.

        Parameters:
            prompt (str): The prompt to display.

        Returns:
            str: User input.
        """
        return input(prompt)

    @staticmethod
    def get_special_symbols():
        """
        Get special symbols chosen by the user.

        Returns:
            list: List of special symbols chosen by the user.
        """
        special_symbols_after = []
        while True:
            symbol_choice = input("Choose a special symbol: 1 for '@', 2 for '#', 3 for '* (q to quit): ")
            if symbol_choice == '1':
                special_symbols_after.append('@')
            elif symbol_choice == '2':
                special_symbols_after.append('#')
            elif symbol_choice == '3':
                special_symbols_after.append('*')
            elif symbol_choice.lower() == 'q':
                break
        return special_symbols_after
