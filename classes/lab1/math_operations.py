import math
import logging

"""
Operations Module.

This module contains classes for mathematical operations.
"""

logger = logging.getLogger(__name__)

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
                logger.info("Calculation: %s %s %s = %s", number1, operator, number2, result)
            return result
        # Exception handling
        except ZeroDivisionError as e:
            logger.error("ZeroDivisionError: %s", e)
            print(e)
        except ValueError as e:
            logger.error("ValueError: %s", e)
            print(e)
        except Exception as e:
            logger.error("An unexpected error occurred: %s", e)
            print("An unexpected error occurred.")
            print(e)
        return None