"""
Module: main
Description: This module contains the main function for interacting with the user 
and generating/displaying ASCII art.
"""
from tkinter import filedialog, messagebox
from logs.logger import setup_logger, logger
from shared.file_operations import FileOperations
from ui.menu.lab3.ui_lab3 import UserInterface
from .ascii_art_generator import AsciiArtGenerator

def main():
    """
    Main function to interact with the user and generate/display ASCII art.

    This function initializes the logger, retrieves available fonts, prompts the user for input,
    and generates/display ASCII art based on user preferences.

    Raises:
        None
    """
    setup_logger()
    logger.info("Main function started.")

    available_fonts = AsciiArtGenerator.list_available_fonts()

    if not available_fonts:
        logger.warning("No fonts found.")
        print("No fonts found.")  # Display a message if there are no available fonts
    else:
        UserInterface.display_available_fonts(available_fonts)  # Print a list of available fonts
        # Prompt the user to enter text for conversion to ASCII art
        user_input = UserInterface.get_user_input(
            "Enter a word or phrase to convert to ASCII art: "
        )
        logger.info(f"User entered: {user_input}")

        selected_font = UserInterface.get_user_input(
            "Enter the name of the font (choose from the list above): "
        )
        logger.info(f"User entered: {selected_font}")

        if selected_font not in available_fonts:
            logger.warning("Invalid font. Using the default font.")
            print("Invalid font. Using the default font.")
            selected_font = "standard"  # Use the default font if the selected one is invalid

        available_colors = {
            "red": "red",
            "green": "green",
            "blue": "blue",
            "yellow": "yellow",
            "white": "white"
        }

        UserInterface.display_available_fonts(
            available_fonts
        )  # Print a list of available colors
        selected_color = UserInterface.get_user_input(
            "Enter the color for the text (choose from the list above): "
        )
        logger.info(f"User entered: {selected_color}")

        if selected_color not in available_colors:
            logger.warning("Invalid color. Using white as the default color.")
            print("Invalid color. Using white as the default color.")
            selected_color = "white"  # Use white color as default if the selected one is invalid

        logger.info(f"Selected font: {selected_font}, Selected color: {selected_color}")

        # Ask the user if they want to use special symbols
        use_special_symbols = UserInterface.get_user_input(
            "Do you want to use special symbols at the end of your phrase? (y/n): "
        )
        logger.info(f"User chose to use special symbols: {use_special_symbols}")

        special_symbols_after = []
        if use_special_symbols.lower() == 'y':
            special_symbols_after = UserInterface.get_special_symbols()

        # Generate ASCII art
        ascii_art_result = AsciiArtGenerator.generate_ascii_art(
            user_input,
            font=selected_font,
            color=selected_color,
            special_symbols=special_symbols_after
        )

        # Display the generated ASCII art for preview
        UserInterface.preview_ascii_art(ascii_art_result)

        try:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt")],
                initialdir="data/lab3",
                initialfile="art"
            )

            if file_path:
                FileOperations.save_representation(ascii_art_result, "ASCII", "txt", file_path)
                logger.info(f"ASCII art saved to: {file_path}")

        except FileNotFoundError as e:
            logger.error(f'Error saving ASCII art result: {e}')
            messagebox.showerror("Error", f'Error saving ASCII art result: {e}')

    logger.info("Main function completed.")

if __name__ == "__main__":
    main()
