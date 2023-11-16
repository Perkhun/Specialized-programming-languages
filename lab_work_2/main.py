#from calculator import Calculator
from lab_work_2.calculator import ScientificCalculator

def main():
    language_choice = input("Choose language (English/Ukrainian): ").strip().lower()
    # strip - removes all spaces (and other whitespace characters) from the beginning and end of the string.
    # lower - converts to lowercase.
    
    if language_choice == 'english':
        import lab_work_2.en_localization as localization
    elif language_choice == 'ukrainian':
        import lab_work_2.ua_localization as localization
    else:
        print("Invalid choice. Using English as default.")
        import lab_work_2.en_localization as localization

    calculator = ScientificCalculator(localization)
    calculator.run_calculator()

if __name__ == "__main__":
    main()