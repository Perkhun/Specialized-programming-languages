"""
Module Docstring: A brief description of the module.
"""
import unittest
from logs.logger import setup_logger, logger
from classes.lab2.base_calculator import Calculator
from classes.lab2.scientific_calculator import ScientificCalculator
from classes.lab2.en_localization import EnglishLocalization as localization

class TestCalculatorAddition(unittest.TestCase):
    """
    Class Docstring: A brief description of the test class.
    """
    setup_logger()
    logger.info("Test function started.")

    def setUp(self):
        """
        Set up method for initializing test fixtures.
        """
        self.calculator = Calculator(None)
        self.scientific_calculator = ScientificCalculator(None)

    def test_addition_positive_numbers(self):
        """
        Check addition of positive numbers.
        """
        result = self.calculator.perform_calculation(2.0, 3.0, '+', 0.0)
        self.assertEqual(result, 5.0)

    def test_addition_negative_numbers(self):
        """
        Check addition of negative numbers.
        """
        result = self.calculator.perform_calculation(-2.0, -3.0, '+', 0.0)
        self.assertEqual(result, -5.0)

    def test_addition_mixed_numbers(self):
        """
        Check addition of positive and negative numbers.
        """
        result = self.calculator.perform_calculation(2.0, -3.0, '+', 0)
        self.assertEqual(result, -1.0)

    # Subtraction

    def test_subtraction_positive_numbers(self):
        """
        Check subtraction of positive numbers.
        """
        result = self.calculator.perform_calculation(5.0, 3.0, '-', 0.0)
        self.assertEqual(result, 2.0)

    def test_subtraction_negative_numbers(self):
        """
        Check subtraction of negative numbers.
        """
        result = self.calculator.perform_calculation(-5.0, -3.0, '-', 0.0)  # -5 - -3 = -5 + 3 = -2
        self.assertEqual(result, -2.0)

    def test_subtraction_mixed_numbers(self):
        """
        Check subtraction of positive and negative numbers.
        """
        result = self.calculator.perform_calculation(5.0, -3.0, '-', 0.0)  # 5 - -3 = 5 + 3 = 8
        self.assertEqual(result, 8.0)

    # Multiplication

    def test_multiplication_positive_numbers(self):
        """
        Check multiplication of positive numbers.
        """
        result = self.calculator.perform_calculation(2.0, 3.0, '*', 0.0)
        self.assertEqual(result, 6.0)

    def test_multiplication_negative_numbers(self):
        """
        Check multiplication of negative numbers.
        """
        result = self.calculator.perform_calculation(-2.0, -3.0, '*', 0.0)
        self.assertEqual(result, 6.0)

    def test_multiplication_mixed_numbers(self):
        """
        Check multiplication of positive and negative numbers.
        """
        result = self.calculator.perform_calculation(2.0, -3.0, '*', 0)
        self.assertEqual(result, -6.0)

    def test_multiplication_with_zero(self):
        """
        Check multiplication by zero.
        """
        result = self.calculator.perform_calculation(5.0, 0.0, '*', 0.0)
        self.assertEqual(result, 0)

    # Division

    def test_division_positive_numbers(self):
        """
        Check division of positive numbers.
        """
        result = self.calculator.perform_calculation(6.0, 3.0, '/', 0.0)
        self.assertEqual(result, 2.0)

    def test_division_negative_numbers(self):
        """
        Check division of negative numbers.
        """
        result = self.calculator.perform_calculation(-6.0, -3.0, '/', 0.0)
        self.assertEqual(result, 2.0)

    def test_division_mixed_numbers(self):
        """
        Check division of positive by negative number.
        """
        result = self.calculator.perform_calculation(6.0, -3.0, '/', 0.0)
        self.assertEqual(result, -2.0)

    def test_division_by_zero(self):
        """
        Check division by zero.
        """
        self.calculator.localization = localization
        result = self.calculator.perform_calculation(5.0, 0.0, '/', 0.0)
        self.assertIsNone(result)

    def test_square_root_negative_number_error(self):
        """
        Check handling error of taking square root of a negative number.
        """
        with self.assertRaises(ValueError):
            self.scientific_calculator.calculate_square_root(-5)

    logger.info("Test function completed.")

if __name__ == '__main__':
    unittest.main()
