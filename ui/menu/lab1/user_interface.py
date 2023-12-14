from classes.lab1.input_validator import InputValidator

class UserInterface:
    """Handles user interaction for the calculator application."""
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
