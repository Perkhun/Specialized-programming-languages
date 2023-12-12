"""
Library Module.

This module contains classes for input validation and mathematical operations.
"""
import math
import logging

class InputValidator:
    """
    Input Validator Class.

    This class provides methods for validating input data.
    """
    # Function to check if a data can be converted to a float. If data can we convert it to float
    @staticmethod
    def is_valid_float(data):
        """
        Check if data can be converted to a float.

        :param data: The data to check.
        :return: True if data can be converted to float, False otherwise.
        """
        try:
            float(data)
            return True
        except ValueError:  # Error handling ValueError to check numbers
            return False

class MathOperations:
    """
    Math Operations Class.

    This class provides methods for performing mathematical operations.
    """
    # Perform calculations based on the operator which user entered
    @staticmethod
    def calculate(number1, number2, operator):
        """
        Perform calculations based on the operator.

        :param number1: The first number.
        :param number2: The second number.
        :param operator: The operator.
        :return: The result of the calculation.
        """
        result = None
        try:
            if operator == '+':
                result = number1 + number2
            elif operator == '-':
                result = number1 - number2
            elif operator == '*':
                result = number1 * number2
            elif operator == '/':
                # Check for division by zero
                if number2 == 0:
                    # Generation of an exception, we create an instance of an exception
                    # of type ZeroDivisionError
                    raise ZeroDivisionError("Error: Division by zero is not allowed")
                result = number1 / number2
            elif operator == '^':  # exponentiation
                result = number1 ** number2
            elif operator == '√':  # sqrt
                if number1 < 0:
                    raise ValueError("Error: Cannot calculate square root of a negative number")
                result = math.sqrt(number1)
            elif operator == '%':  # Remainder from division
                result = number1 % number2

            if result is not None:
                logging.info("Calculation: %s %s %s = %s", number1, operator, number2, result)
            return result
            # Exception handling
        except ZeroDivisionError as e: # The variable e contains information about the exception
            print(e)
        return None
