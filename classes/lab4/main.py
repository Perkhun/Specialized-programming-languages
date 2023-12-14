"""
Module: main
Description: Contains the main function for interacting with the user and generating ASCII art.
"""
from tkinter import filedialog, messagebox
from logs.logger import setup_logger, logger
from shared.file_operations import FileOperations
from ui.menu.lab4.ui_lab4 import UserInput
from .ascii_art_generator import ASCIIArtGenerator

def main():
    """
    Main function to interact with the user, generate, and optionally save ASCII art.

    This function prompts the user for input, including the word or phrase to convert to ASCII art,
    the size of the ASCII art, and the alignment preference. It then generates colored ASCII art
    and offers the option to save the art to a file.

    Raises:
        None
    """

    setup_logger()
    logger.info("Main function started.")

    letters = {
        "A": ["   A   ", "  A A  ", " A   A ", " AAAAA ", " A   A за"],
        "B": ["  BBB  ", " B   B ", "  BBB  ", " B   B ", "  BBB  "],
        "C": ["  CCC  ", "  C    ", " C    ", "  C    ", "   CCC  "],
        "D": [" DD   ", " D  D  ", " D   D ", " D  D  ", " DD   "],
        "E": [" EEEE ", " E    ", " EEE  ", " E    ", " EEEE "],
        "F": [" FFFF ", " F    ", " FFF  ", " F    ", " F    "],
        "G": ["  GGG ", " G    ", " G  GG", " G   G", "  GGGG"],
        "H": [" H   H ", " H   H ", " HHHHH ", " H   H ", " H   H "],
        "I": [" III  ", "  I   ", "  I   ", "  I   ", " III  "],
        "J": ["  JJJ  ", "   J  ", "   J  ", " J J  ", "  JJ  "],
        "K": [" K  K ", " K K  ", " KK   ", " K K  ", " K  K "],
        "L": [" L    ", " L    ", " L    ", " L    ", " LLLL "],
        "M": [" M   M ", " MM MM ", " M M M ", " M   M ", " M   M "],
        "N": [" N   N ", " NN  N ", " N N N ", " N  NN ", " N   N "],
        "O": ["  O  ", " O O ", " O O ", " O O ", "  O  "],
        "P": [" PPP  ", " P   P ", " PPP  ", " P    ", " P    "],
        "Q": ["  QQ  ", " Q  Q ", " Q  Q ", " Q QQ ", "  QQ Q"],
        "R": [" RRR  ", " R  R ", " RRR  ", " R R  ", " R  R "],
        "S": ["  SSS  ", " S    ", "  SSS ", "     S", "  SSS "],
        "T": [" TTTTT ", "   T  ", "   T  ", "   T  ", "   T  "],
        "U": [" U   U ", " U   U ", " U   U ", " U   U ", "  UUU "],
        "V": [" V   V ", " V   V ", " V   V ", "  V V  ", "   V  "],
        "W": [" W   W ", " W   W ", " W W W ", " W W W ", "  W W "],
        "X": [" X   X ", " X   X ", "  X X  ", " X   X ", " X   X "],
        "Y": [" Y   Y ", " Y   Y ", "  YYY  ", "   Y  ", "   Y  "],
        "Z": [" ZZZZ  ", "   Z  ", "  Z   ", " Z    ", " ZZZZ "],
        "А": ["   А   ", "  А А  ", " А   А ", " ААААА ", " А   А "],
        "Б": ["  БББ  ", " Б   Б ", "  БББ  ", " Б   Б ", "  БББ  "],
        "В": [" ВВВ   ", " В   В ", " ВВВ   ", " В   В ", " ВВВ   "],
        "Г": [" ГГГГГ ", " Г     ", " Г     ", " Г     ", " Г     "],
        "Д": [" Д  Д  ", " Д  Д  ", " ДДДДД ", " Д   Д ", " Д   Д "],
        "Е": [" ЕЕЕЕ ", " Е    ", " ЕЕЕ  ", " Е    ", " ЕЕЕЕ "],
        "Є": ["  ЄЄЄЄЄ ", " Є      ", " ЄЄЄЄ   ", " Є      ", "  ЄЄЄЄЄ "],
        "Ж": [" Ж   Ж   Ж ", "  Ж Ж    Ж  ", "   ЖЖЖЖЖ   ", "  Ж Ж    Ж  ", " Ж   Ж   Ж "],
        "З": [" ЗЗЗ ", "   З  ", "  З   ", "   З  ", " ЗЗЗ "],
        "И": [" И   И ", " И  I  ", " И I I ", " И   I ", " И   I "],
        "І": [" ІІІ ", "  І  ", "  І  ", "  І  ", " ІІІ "], 
        "Ї": ["   Ї   ", "   Ї   ", "   Ї   ", "  ЇЇЇ  ", "  ЇЇЇ  "],
        "Й": [" Й   Й ", " Й   Й ", " ЙЙЙЙЙ ", " Й   Й ", " Й   Й "],
        "К": [" К   К ", " К  К  ", " ККК  ", " К  К  ", " К   К "],
        "Л": [" Л   Л ", " Л   Л ", " Л   Л ", " Л   Л ", " ЛЛЛЛ "],
        "М": [" М   М   М ", " ММ ММ  ММ ", " М М М М М ", " М  M  M  М ", " М   M   М "],
        "Н": [" Н   Н ", " Н   Н ", " ННННН ", " Н   Н ", " Н   Н "],
        "О": ["  ООО  ", " О   О ", " О   О ", " О   О ", "   ООО  "],
        "П": ["  ППП  ", " П   П ", " П   П ", " П   П ", " П   П"],
        "Р": [" РРР  ", " Р   Р ", " РРР  ", " Р     ", " Р     "],
        "С": ["  ССС  ", " С     ", " С     ", " С     ", "  ССС  "],
        "Т": [" ТТТТТ ", "   Т   ", "   Т   ", "   Т   ", "   Т   "],
        "У": [" У   У ", " У   У ", " У   У ", " У У У ", "  УУУ  "],
        "Ф": ["   ФФФ   ", "  Ф   Ф  ", " ФФФФФФ ", " Ф   Ф  ", " Ф   Ф  "],
        "Х": [" Х   Х ", "  ХХХ  ", "   Х   ", "  ХХХ  ", " Х   Х "],
        "Ц": [" Ц   Ц   Ц ", "  Ц   Ц   Ц  ", "  Ц   Ц   Ц  ", " ЦЦЦЦЦЦ ", "       Ц  "],
        "Ч": [" Ч   Ч ", "  Ч   Ч ", "  Ч   Ч ", "   ЧЧЧ  ", "   ЧЧ   "],
        "Ш": [" Ш     Ш ", "  Ш   Ш  ", "   Ш Ш   ", "    Ш    ", " Ш     Ш "],
        "Щ": [" Щ     Щ     Щ ", "  Щ   Щ   Щ  ", "   Щ ЩЩ Щ   ", "    Щ   Щ    ", " Щ     Щ     Щ "],
        "Ь": [" Ь   Ь ", " Ь   Ь ", " Ь   Ь ", " Ь ЬЬ  ", "  Ь   Ь "],
        "Ю": [" Ю   Ю ", " Ю   Ю ", "  ЮЮЮ  ", " Ю   Ю ", " Ю   Ю "],
        "Я": ["  ЯЯЯ ", " Я   Я ", "  ЯЯЯ ", "     Я", " ЯЯЯ "],
    }

    user_input = input("Enter the word or phrase you want to convert to ASCII art: ")
    logger.info(f"User input: {user_input}")
    width, height = UserInput.get_valid_size()
    logger.info(f"Width: {width}, Height: {height}")
    alignment_choice = UserInput.get_alignment_choice()
    logger.info(f"Alignment choice: {alignment_choice}")

    if alignment_choice == "1":
        alignment = "left"
    elif alignment_choice == "2":
        alignment = "center"
    elif alignment_choice == "3":
        alignment = "right"

    ascii_art = ASCIIArtGenerator.generate_colored_ascii_art(
        user_input, letters, width, height, alignment
    )

    print(ascii_art)

    save_to_file = input("Save to file? (Yes/No): ").strip().lower()
    logger.info(f"User choice to save to file: {save_to_file}")

    if save_to_file == "yes":
        try:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt")],
                initialdir="data/lab4",
                initialfile="art"
            )

            if file_path:
                FileOperations.save_representation(ascii_art, "ASCII", "txt", file_path)
                logger.info(f"ASCII art saved to: {file_path}")

        except FileNotFoundError as e:
            logger.error(f'Error saving ASCII art: {e}')
            messagebox.showerror("Error", f'Error saving ASCII art: {e}')

    logger.info("Main function completed.")

if __name__ == "__main__":
    main()
