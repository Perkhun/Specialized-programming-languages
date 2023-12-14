"""
Input Module.

This module contains classes for input validation and mathematical operations.
"""

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
