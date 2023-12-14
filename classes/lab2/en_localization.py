"""
English localization for the calculator program.
"""
from .localization import BaseLocalization

class EnglishLocalization(BaseLocalization):
    """English localization for the calculator program."""
    PROMPT_ENTER_FIRST_NUMBER = "Enter the first number: "
    PROMPT_ENTER_SECOND_NUMBER = "Enter the second number: "
    INVALID_INPUT = "Invalid input. Please enter a valid number."
    PROMPT_CHOOSE_OPERATOR = "Choose operator (+, -, *, /, ^, √, %): "
    INVALID_OPERATOR = "Invalid operator. Please enter a valid operator from the list (+, -, *, /, ^, √, %): "
    PROMPT_ENTER_DECIMAL_PLACES = "Enter the number of decimal places: "
    RESULT_FORMAT = "Result: {result:.{decimal_places}f}"
    MEMORY_OPERATOR_HEADER = "Memory operator:"
    CONTINUE_CALCULATION_PROMPT = "Do you want to perform another calculation? (yes/no): "
    CONTINUE_CALCULATION = "yes"
    BAN_FOR_ZERO = "Cannot divide by zero. Please enter a non-zero denominator."
