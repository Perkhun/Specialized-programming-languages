def generate_colored_ascii_art(text, letters, width, height, alignment="left"):
    colors = {  # ANSI color definitions
        "R": "\x1b[31m",  # Red
        "G": "\x1b[32m",  # Green
        "Y": "\x1b[33m",  # Yellow
        "B": "\x1b[34m",  # Blue
        "M": "\x1b[35m",  # Magenta
        "C": "\x1b[36m",  # Cyan
        "W": "\x1b[37m"   # White
    }
    text = text.upper()  # Convert the input text to uppercase
    ascii_art = []       # Initialize the ASCII art lines
    real_letter_width = len(letters["A"][0])  # Calculate the real width of the letter "A" (or any other letter).
                                              # This real width is then used to determine the number of characters horizontally for each letter.
    if width < len(text) * real_letter_width:
        real_letter_width = width // len(text)
    for line in range(5):  # Iterate through each line of ASCII art
        art_line = ""
        for char in text:  # Iterate through each letter in the input text 
            if char in letters:
                letter = letters[char]
                color_code = (ord(char) % len(colors))  # Character code % number of colors (from 0 to 5 in the array)
                colored_char = f"{colors[list(colors.keys())[color_code]]}{letter[line][:real_letter_width]}\x1b[0m"  # Reset color
                art_line += colored_char
            else:
                art_line += " " * real_letter_width  # Add spaces if the letter is not found
        if alignment == "left":      # Left alignment (default)
            ascii_art.append(art_line)
        elif alignment == "center":  # Center alignment
            left_padding = (width - len(art_line)) // 2
            right_padding = width - len(art_line) - left_padding
            centered_line = " " * left_padding + art_line + " " * right_padding
            ascii_art.append(centered_line)
        elif alignment == "right":  # Right alingment
            right_padding = width - len(art_line)
            right_aligned_line = " " * right_padding + art_line
            ascii_art.append(right_aligned_line)
    scaled_ascii_art = []
    for line in ascii_art:
        for i in range(height):
            scaled_ascii_art.append(line)
    return "\n".join(scaled_ascii_art)  # Return the final ASCII art as a string

def get_valid_size():
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

def get_alignment_choice():
    while True:
        print("Choose an alignment option:")
        print("1. Left alignment")
        print("2. Center alignment")
        print("3. Right alignment")
        choice = input("Your choice (1/2/3): ")
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Please select one of the options (1/2/3).")

def save_ascii_art_to_file(ascii_art, filename):
    try:
        with open(filename, 'w') as file:
            file.write(ascii_art)
        print(f"ASCII art has been saved to the file {filename}")
    except IOError as e:
        print(f"Error while saving the file: {e}")

def main():
    letters = {
        "A": ["   A   ", "  A A  ", " A   A ", " AAAAA ", " A   A "],
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
    width, height = get_valid_size()
    alignment_choice = get_alignment_choice()

    if alignment_choice == "1":
        alignment = "left"
    elif alignment_choice == "2":
        alignment = "center"
    elif alignment_choice == "3":
        alignment = "right"

    ascii_art = generate_colored_ascii_art(user_input, letters, width, height, alignment)
    print(ascii_art)
    save_to_file = input("Save ASCII art to a file? (Yes/No): ").strip().lower()

    if save_to_file == "yes":
        filename = input("Enter the file name for saving (e.g., art.txt): ")
        save_ascii_art_to_file(ascii_art, filename)

if __name__ == "__main__":
    main()

