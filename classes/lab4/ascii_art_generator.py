"""
Module: ascii_art_generator
Description: Contains the ASCIIArtGenerator class for generating and manipulating colored ASCII art.
"""

class ASCIIArtGenerator:
    """
    Class for generating and manipulating colored ASCII art.

    Attributes:
        letters (dict): Dictionary containing ASCII representations of letters.

    Methods:
        generate_colored_ascii_art(text, letters, width, height, alignment="left"):
            Generate colored ASCII art from the given text.
    """
    def __init__(self, letters):
        """
        Initialize the ASCIIArtGenerator object.

        Args:
            letters (dict): Dictionary containing ASCII representations of letters.

        Returns:
            None

        Raises:
            None
        """
        self.letters = letters

    @staticmethod
    def generate_colored_ascii_art(text, letters, width, height, alignment="left"):
        """
        Generate colored ASCII art from the given text.

        Args:
            text (str): The text to be converted into colored ASCII art.
            letters (dict): Dictionary containing ASCII representations of letters.
            width (int): Width of the generated ASCII art.
            height (int): Height of the generated ASCII art.
            alignment (str, optional): Alignment of the ASCII art (default is "left").

        Returns:
            str: Colored ASCII art string.

        Raises:
            None
        """
        colors = {
            "R": "\x1b[31m",  # Червоний
            "G": "\x1b[32m",  # Зелений
            "Y": "\x1b[33m",  # Жовтий
            "B": "\x1b[34m",  # Синій
            "M": "\x1b[35m",  # Магента
            "C": "\x1b[36m",  # Бірюзовий
            "W": "\x1b[37m"   # Білий
        }

        text = text.upper()
        ascii_art = []

        real_letter_width = len(letters["A"][0])
        if width < len(text) * real_letter_width:
            real_letter_width = width // len(text)

        for line in range(5):
            art_line = ""
            for char in text:
                if char in letters:
                    letter = letters[char]
                    color_code = (ord(char) % len(colors))
                    colored_char = (
                        f"{colors[list(colors.keys())[color_code]]}"
                        f"{letter[line][:real_letter_width]}\x1b[0m"
                    )
                    art_line += colored_char
                else:
                    art_line += " " * real_letter_width
            if alignment == "left":
                ascii_art.append(art_line)
            elif alignment == "center":
                left_padding = (width - len(art_line)) // 2
                right_padding = width - len(art_line) - left_padding
                centered_line = " " * left_padding + art_line + " " * right_padding
                ascii_art.append(centered_line)
            elif alignment == "right":
                right_padding = width - len(art_line)
                right_aligned_line = " " * right_padding + art_line
                ascii_art.append(right_aligned_line)

        scaled_ascii_art = []
        for line in ascii_art:
            for i in range(height):
                scaled_ascii_art.append(line)

        return "\n".join(scaled_ascii_art)
