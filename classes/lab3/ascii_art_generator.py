import os  # Import the module for interacting with the operating system
import pyfiglet  # Import the module for generating ASCII art
from termcolor import colored  # Import the module for colored text in the terminal

class AsciiArtGenerator:
    """Class for generating and customizing ASCII art."""
    @staticmethod
    def list_available_fonts():
        """Get a list of available fonts for ASCII art."""
        return pyfiglet.Figlet().getFonts()  # Function to get a list of available fonts for ASCII art

    @staticmethod
    def generate_ascii_art(text, font="standard", color="white", special_symbols=None):
        """
        Generate colored ASCII art.

        Args:
            text (str): The text to be converted into ASCII art.
            font (str, optional): The font style for the ASCII art. Defaults to "standard".
            color (str, optional): The color of the ASCII art. Defaults to "white".
            special_symbols (list, optional): List of special symbols to add at the end of the text.

        Returns:
            str: Colored ASCII art string.

        Raises:
            Exception: If an error occurs during the generation process.
        """
        try:
            # Get the size of the terminal
            columns, _ = os.get_terminal_size()

            # Check if there are special symbols to add at the end of the text
            if special_symbols:
                special_symbols_str = ' '.join(special_symbols)
                text = f"{text} {special_symbols_str}"

            # Generate ASCII art using pyfiglet
            ascii_art = pyfiglet.figlet_format(text, font=font)

            # Split the ASCII art into lines
            lines = ascii_art.split('\n')

            # Determine the number of characters in the longest line
            max_line_length = max(len(line) for line in lines)

            # Calculate padding for center alignment
            padding = (columns - max_line_length) // 2

            # Add padding for center alignment
            centered_ascii_art = '\n'.join(' ' * padding + line for line in lines)

            # Color the ASCII art with the selected color
            colored_ascii_art = colored(centered_ascii_art, color)
            return colored_ascii_art
        except Exception as e:
            return str(e)