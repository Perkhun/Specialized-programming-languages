from .math_operations import MathOperations

class Calculator:
    """A simple calculator class."""
    def __init__(self):
        """Initialize the Calculator class."""
        self.calculation_records = []

    def perform_calculation(self, number1, number2, operator):
        result = None
        try:
            result = MathOperations.calculate(number1, number2, operator)
            return result
        except ZeroDivisionError as e:
            print(e)
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