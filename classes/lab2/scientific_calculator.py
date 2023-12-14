"""
Module containing the ScientificCalculator class, a subclass of Calculator.
"""
import math
from .base_calculator import Calculator

class ScientificCalculator(Calculator):
    """
    ScientificCalculator extends Calculator and provides additional scientific functions.
    """
    def __init__(self, localization):
        """
        Initialize the ScientificCalculator.

        Parameters:
        - localization (BaseLocalization): The localization object for user prompts.
        """
        super().__init__(localization)

    def calculate_square_root(self, number):
        """
        Calculate the square root of a number.

        Parameters:
        - number (float): The input number.

        Returns:
        - float: The square root of the input number.
        """
        result = math.sqrt(number)
        return result

    def calculate_power(self, base, exponent):
        """
        Calculate the power of a base to an exponent.

        Parameters:
        - base (float): The base number.
        - exponent (float): The exponent.

        Returns:
        - float: The result of base raised to the exponent.
        """
        result = pow(base, exponent)
        return result
