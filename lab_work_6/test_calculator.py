import unittest
import sys
from importlib.machinery import SourceFileLoader

sys.path.append(r"D:\ЛПНУ\5_семестр\Спеціалізовані мови програмування\lab_works")

calculator_module = SourceFileLoader(
    "calculator",
    r"D:\ЛПНУ\5_семестр\Спеціалізовані мови програмування\lab_works\lab_work_2\calculator.py",
).load_module()

import lab_work_2.en_localization as localization

class TestCalculatorAddition(unittest.TestCase):
    def setUp(self):
        # Initialize the calculator object before each test
        self.calculator = calculator_module.Calculator(None)
        # self.calculator = Calculator(None)  # Pass None since we don't need localization for tests
        self.scientific_calculator = calculator_module.ScientificCalculator(None)

    # Addition

    def test_addition_positive_numbers(self):
        # Check addition of positive numbers
        result = self.calculator.perform_calculation(2, 3, '+', 0)
        self.assertEqual(result, 5)

    def test_addition_negative_numbers(self):
        # Check addition of negative numbers
        result = self.calculator.perform_calculation(-2, -3, '+', 0)
        self.assertEqual(result, -5)

    def test_addition_mixed_numbers(self):
        # Check addition of positive and negative numbers
        result = self.calculator.perform_calculation(2, -3, '+', 0)
        self.assertEqual(result, -1)
    
    # Subtraction

    def test_subtraction_positive_numbers(self):
        # Check subtraction of positive numbers
        result = self.calculator.perform_calculation(5, 3, '-', 0)
        self.assertEqual(result, 2)

    def test_subtraction_negative_numbers(self):
        # Check subtraction of negative numbers
        result = self.calculator.perform_calculation(-5, -3, '-', 0)  # -5 - -3 = -5 + 3 = -2
        self.assertEqual(result, -2)

    def test_subtraction_mixed_numbers(self):
        # Check subtraction of positive and negative numbers
        result = self.calculator.perform_calculation(5, -3, '-', 0)  # 5 - -3 = 5 + 3 = 8
        self.assertEqual(result, 8)

    # Multiplication

    def test_multiplication_positive_numbers(self):
        # Check multiplication of positive numbers
        result = self.calculator.perform_calculation(2, 3, '*', 0)
        self.assertEqual(result, 6)

    def test_multiplication_negative_numbers(self):
        # Check multiplication of negative numbers
        result = self.calculator.perform_calculation(-2, -3, '*', 0)
        self.assertEqual(result, 6)

    def test_multiplication_mixed_numbers(self):
        # Check multiplication of positive and negative numbers
        result = self.calculator.perform_calculation(2, -3, '*', 0)
        self.assertEqual(result, -6)

    def test_multiplication_with_zero(self):
        # Check multiplication by zero
        result = self.calculator.perform_calculation(5, 0, '*', 0)
        self.assertEqual(result, 0)

    # Division

    def test_division_positive_numbers(self):
        # Check division of positive numbers
        result = self.calculator.perform_calculation(6, 3, '/', 0)
        self.assertEqual(result, 2)

    def test_division_negative_numbers(self):
        # Check division of negative numbers
        result = self.calculator.perform_calculation(-6, -3, '/', 0)
        self.assertEqual(result, 2)

    def test_division_mixed_numbers(self):
        # Check division of positive by negative number
        result = self.calculator.perform_calculation(6, -3, '/', 0)
        self.assertEqual(result, -2)

    def test_division_by_zero(self):
        # Check division by zero
        self.calculator.localization = localization 
        result = self.calculator.perform_calculation(5, 0, '/', 0)
        self.assertIsNone(result)  

    def test_square_root_negative_number_error(self): 
        # Check handling error of taking square root of a negative number
        with self.assertRaises(ValueError):  # Expecting an error to be raised. If it does, the test is successful
            self.scientific_calculator.calculate_square_root(-5)

if __name__ == '__main__':
    unittest.main()