"""
This module contains the main logic for the calculator application.
"""
from ui.menu.lab1.user_interface import UserInterface
from shared.user_input_handler import UserInputHandler
from logs.logger import setup_logger, logger
from .calculator import Calculator

def main():
    """
    Main function for the calculator application.
    """
    setup_logger()

    calculator = Calculator()
    ui = UserInterface()
    user_input = UserInputHandler()

    while True:
        number1 = ui.get_number_from_user("Enter the first number: ")
        logger.info("User input: First number - %s", number1)
        number2 = ui.get_number_from_user("Enter the second number: ")
        logger.info("User input: Second number - %s", number2)
        operator = user_input.get_operator_from_user()
        logger.info("User input: Operator - %s", operator)
        decimal_places = ui.get_decimal_places_from_user()
        logger.info("User input: Decimal places - %s", decimal_places)

        result = calculator.perform_calculation(number1, number2, operator)

        if result is not None:
            # Store the calculation and expression in history
            expression = (
                f"{number1:.{decimal_places}f} {operator} {number2:.{decimal_places}f} = "
                f"{result:.{decimal_places}f}"
            )
            calculator.calculation_records.append({"expression": expression, "result": result})
            calculator.display_result(result, expression, decimal_places)
            logger.info("Calculation successful: %s", expression)
        else:
            print("Calculation failed.")
            logger.error("Calculation failed.")

        if not ui.get_another_calculation_from_user():
            break

if __name__ == "__main__":
    main()
