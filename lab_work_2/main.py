from calculator import Calculator

if __name__ == "__main__":
    language_choice = input("Choose language (English/Ukrainian): ").strip().lower()
    # strip - removes all spaces (and other whitespace characters) from the beginning and end of the string.
    # lower - converts to lowercase.
    
    if language_choice == 'english':
        import en_localization as localization
    elif language_choice == 'ukrainian':
        import ua_localization as localization
    else:
        print("Invalid choice. Using English as default.")
        import en_localization as localization

    calculator = Calculator(localization)
    calculator.run_calculator()