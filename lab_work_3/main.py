import os  # Import the module for interacting with the operating system
import pyfiglet  # Import the module for generating ASCII art
from termcolor import colored  # Import the module for colored text in the terminal
from tkinter import filedialog, Tk  # Import the module for a file dialog to choose a file

def list_available_fonts():
    return pyfiglet.Figlet().getFonts()  # Function to get a list of available fonts for ASCII art

def generate_ascii_art(text, font="standard", color="white", special_symbols=None):
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

def preview_ascii_art(ascii_art):
    print("Preview of ASCII art:")
    print(ascii_art)
    input("Press Enter to continue...")  # Display a preview of the ASCII art and wait for Enter key press

def save_ascii_art(ascii_art, filename):
    try:
        # Save the ASCII art to the specified file
        with open(filename, "w") as file:
            file.write(ascii_art)
        print(f"ASCII art saved to {filename}")  # Notify about successful file save
    except Exception as e:
        print(f"Error saving ASCII art: {e}")  # Print an error message if there's an issue with saving

if __name__ == "__main__":
    available_fonts = list_available_fonts()
    
    if not available_fonts:
        print("No fonts found.")  # Display a message if there are no available fonts
    else:
        print("Available fonts:")
        for font in available_fonts:
            print(font)  # Print a list of available fonts

        # Prompt the user to enter text for conversion to ASCII art
        user_input = input("Enter a word or phrase to convert to ASCII art: ")
        
        selected_font = input("Enter the name of the font (choose from the list above): ")

        if selected_font not in available_fonts:
            print("Invalid font. Using the default font.")
            selected_font = "standard"  # Use the default font if the selected one is invalid

        available_colors = {
            "red": "red",
            "green": "green",
            "blue": "blue",
            "yellow": "yellow",
            "white": "white"
        }

        print("Available colors:")
        for color in available_colors:
            print(color)  # Print a list of available colors

        selected_color = input("Enter the color for the text (choose from the list above): ")

        if selected_color not in available_colors:
            print("Invalid color. Using white as the default color.")
            selected_color = "white"  # Use white color as default if the selected one is invalid

        # Ask the user if they want to use special symbols
        use_special_symbols = input("Do you want to use special symbols in the end of your phrase like '@', '#', or '*'? (y/n): ")
        special_symbols_after = []

        if use_special_symbols.lower() == 'y':
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

        # Generate ASCII art
        ascii_art_result = generate_ascii_art(user_input, font=selected_font, color=selected_color, special_symbols=special_symbols_after)
        
        # Display the generated ASCII art for preview
        preview_ascii_art(ascii_art_result)

        root = Tk()
        root.withdraw()  # Hide the main Tkinter window

        # Ask the user for a path to save the ASCII art
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            save_ascii_art(ascii_art_result, file_path)  # Save the ASCII art to the specified file
