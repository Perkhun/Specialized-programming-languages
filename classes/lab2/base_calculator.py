"""
Module: base_calculator
Description: Contains the Calculator class for basic arithmetic operations.
"""
import math
from logs.logger import setup_logger, logger
from shared.input_validator import InputValidator
from shared.user_input_handler import UserInputHandler

class Calculator:
    """A basic calculator class."""

    def __init__(self, localization):
        """Initialize the calculator."""
        self.memory = None
        self.calculation_records = []
        self.localization = localization
        self.input_validator = InputValidator()
        self.user_input_handler = UserInputHandler()

        self.setup_logger()

    def setup_logger(self):
        """Set up the logger."""
        setup_logger()

    def get_number_from_user(self, prompt):
        """
        Get a valid float from the user.

        Args:
            prompt: Prompt message for the user.

        Returns:
            float: Valid float entered by the user.
        """
        while True:
            num_input = input(prompt)
            if self.input_validator.is_valid_float(num_input):
                return float(num_input)
            logger.error(self.localization.INVALID_INPUT)

    def perform_calculation(self, number1, number2, operator, decimal_places):
        """Perform the specified calculation."""
        valid_operators = {'+', '-', '*', '/', '^', '√', '%'}
        if operator not in valid_operators:
            logger.error(self.localization.INVALID_OPERATOR)
            return None

        try:
            operations = {'+': float.__add__, '-': float.__sub__, '*': float.__mul__,
                          '/': float.__truediv__, '^': pow, '√': math.sqrt, '%': float.__mod__}
            result = operations[operator](float(number1), float(number2))
            return round(result, int(decimal_places))
        except ZeroDivisionError:
            logger.error(self.localization.BAN_FOR_ZERO)
            return None

    def get_continue_input(self):
        """
        Get user input to continue or exit the calculator.

        Returns:
            str: User's choice to continue or exit.
        """
        return input(self.localization.CONTINUE_CALCULATION_PROMPT).lower()

    def run_calculator(self):
        """
        Run the calculator until the user chooses to exit.
        """
        while True:
            number1 = self.get_number_from_user(self.localization.PROMPT_ENTER_FIRST_NUMBER)
            number2 = self.get_number_from_user(self.localization.PROMPT_ENTER_SECOND_NUMBER)
            operator = self.user_input_handler.get_operator_from_user()
            decimal_places = int(input(self.localization.PROMPT_ENTER_DECIMAL_PLACES))

            result = self.perform_calculation(number1, number2, operator, decimal_places)

            if result is not None:
                self.memory = result

                expression = (
                    f"{number1:.{decimal_places}f} {operator} "
                    f"{number2:.{decimal_places}f} = {result:.{decimal_places}f}"
                )
                self.calculation_records.append(expression)

                formatted_result = self.localization.RESULT_FORMAT.format(
                    result=result, decimal_places=decimal_places
                )
                print(formatted_result)

                history_str = "\n".join(self.calculation_records)
                print(f"{self.localization.MEMORY_OPERATOR_HEADER}\n{history_str}")

                logger.info(expression)

            else:
                pass

            another_calculation = self.get_continue_input()
            if another_calculation != self.localization.CONTINUE_CALCULATION:
                break
