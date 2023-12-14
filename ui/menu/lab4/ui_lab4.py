"""
Module for defining the UserInput class providing various user input functionalities.
"""
class UserInput:
    """
    Module for defining the UserInput class providing various user input functionalities.
    """
    @staticmethod
    def get_valid_size():
        """
        Get a valid size for ASCII art from the user.

        Returns:
            tuple: A tuple containing width and height (integers) of the ASCII art.
        """
        while True:
            try:
                width = int(input("Enter the width of the ASCII art: "))
                height = int(input("Enter the height of the ASCII art: "))
                if width > 0 and height > 0:
                    return width, height
                else:
                    print("Dimensions should be greater than 0.")
            except ValueError:
                print("Please enter valid numbers for dimensions.")

    @staticmethod
    def get_alignment_choice():
        """
        Get the user's choice for text alignment.

        Returns:
            str: The user's alignment choice as a string ("1", "2", or "3").
        """
        while True:
            print("Choose the alignment option:")
            print("1. Left alignment")
            print("2. Center alignment")
            print("3. Right alignment")
            choice = input("Your choice (1/2/3): ")
            if choice in ["1", "2", "3"]:
                return choice
            else:
                print("Please choose one of the options (1/2/3).")
