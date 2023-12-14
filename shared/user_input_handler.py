"""Module for handling user input."""
class UserInputHandler:
    """
    Class for handling user input.
    """
    def __init__(self, localization=None):
        """
         Initialize the UserInputHandler.

         Args:
             localization: An optional localization object.
         """
        self.localization = localization

    def get_operator_from_user(self):
        """
        Get a valid operator from the user.

        Returns:
            str: Valid operator entered by the user.
        """
        valid_operators = {'+', '-', '*', '/', '^', '√', '%'}
        prompt_message = (
            self.localization.PROMPT_CHOOSE_OPERATOR
            if self.localization else
            "Enter the operator (+, -, *, /,  ^, √, %): "
        )
        invalid_message = (
            self.localization.INVALID_OPERATOR
            if self.localization else
            "Invalid operator. Please enter a valid operator from the list "
            "(+, -, *, /, ^, √, %): "
        )

        while True:
            operator = input(prompt_message)
            if operator in valid_operators:
                return operator
            else:
                print(invalid_message)
