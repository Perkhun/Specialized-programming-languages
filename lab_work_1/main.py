"""
Calculator Application.

This module contains a simple calculator application that performs basic arithmetic operations.
"""
import logging
from lab_work_1.library import MathOperations, InputValidator

# Setting logging
logging.basicConfig(filename='calculator.log', level=logging.INFO)

class Calculator:
    """A simple calculator class."""
    def __init__(self):
        """Initialize the Calculator class."""
        self.calculation_records = []

    def perform_calculation(self, number1, number2, operator):
        """
        Perform a calculation.

        :param number1: The first number.
        :param number2: The second number.
        :param operator: The operator.
        :return: The result of the calculation.
        """
        result = None
        try:
            result = MathOperations.calculate(number1, number2, operator)
            return result
        except ZeroDivisionError as e:
            logging.error(e)
            return None

    def display_result(self, result, expression, decimal_places):
        """
        Display the result of the calculation.

        :param result: The result of the calculation.
        :param expression: The expression used for the calculation.
        :param decimal_places: The number of decimal places.
        """
        formatted_result = f"Result: {result:.{decimal_places}f}"
        print(formatted_result)
        history_str = ", ".join([entry["expression"] for entry in self.calculation_records])
        print(f"Memory operator: {history_str}")

    def display_history(self):
        """Display the calculation history."""
        for entry in self.calculation_records:
            print(entry["expression"])

class UserInterface:
    """Handles user interaction for the calculator application."""
    # Prompt the user to enter the number
    @staticmethod
    def get_number_from_user(prompt):
        """
        Prompt the user to enter a number.

        :param prompt: The prompt message.
        :return: The entered number.
        """
        while True:
            num_input = input(prompt)
            if InputValidator.is_valid_float(num_input):
                return float(num_input)
            print("Invalid input. Please enter a valid number.")

    # Prompt the user to enter an operator
    @staticmethod
    def get_operator_from_user():
        """
        Prompt the user to enter an operator.

        :return: The entered operator.
        """
        valid_operators = ['+', '-', '*', '/', '^', '√', '%']
        while True:
            operator = input("Enter the operator (+, -, *, /,  ^, √, %): ")
            if operator in valid_operators:
                return operator
            print("Invalid operator. Please enter a valid operator from the list "
                  "(+, -, *, /, ^, √, %): ")

    @staticmethod
    def get_decimal_places_from_user():
        """
        Prompt the user to enter the number of decimal places.

        :return: The entered number of decimal places.
        """
        return int(input("Enter the number of decimal places: "))

    @staticmethod
    def get_another_calculation_from_user():
        """
        Prompt the user if they want to perform another calculation.

        :return: True if the user wants another calculation, False otherwise.
        """
        return input("Do you want to perform another calculation? (yes/no): ").lower() == 'yes'

def main():
    """
    Main function to execute the calculator application.
    """
    calculator = Calculator()
    ui = UserInterface()

    while True:
        number1 = ui.get_number_from_user("Enter the first number: ")
        number2 = ui.get_number_from_user("Enter the second number: ")
        operator = ui.get_operator_from_user()
        decimal_places = ui.get_decimal_places_from_user()

        result = calculator.perform_calculation(number1, number2, operator)

        if result is not None:
            # Store the calculation and expression in history
            expression = (
                f"{number1:.{decimal_places}f} {operator} {number2:.{decimal_places}f} = "
                f"{result:.{decimal_places}f}"
            )
            calculator.calculation_records.append({"expression": expression, "result": result})
            calculator.display_result(result, expression, decimal_places)
        else:
            print("Calculation failed.")

        if not ui.get_another_calculation_from_user():
            break

if __name__ == "__main__":
    main()
