import math
import en_localization  # Localization for the English language
import ua_localization  # Localization for the Ukrainian language

class Calculator:
    def __init__(self, localization):
        # Constructor initializes the Calculator object with localization
        self.memory = None  # Memory for storing results of previous calculations
        self.calculation_records = []  # List to store calculation records
        self.localization = localization  # Stores the localization object for displaying texts

    def is_valid_float(self, data):
        # Checks if the text can be converted to a floating-point number
        try:
            float(data)
            return True
        except ValueError:
            return False

    def get_number_from_user(self, prompt):
        # Prompts the user to enter a number and returns its value
        while True:
            num_input = input(prompt)
            if self.is_valid_float(num_input):
                return float(num_input)
            else:
                print(localization.INVALID_INPUT)

    def get_operator_from_user(self):
        # Prompts the user to enter an operator and returns it
        valid_operators = ['+', '-', '*', '/', '^', '√', '%']
        while True:
            operator = input(self.localization.PROMPT_CHOOSE_OPERATOR)
            if operator in valid_operators:
                return operator
            else:
                print(localization.INVALID_OPERATOR)

    def perform_calculation(self, number1, number2, operator, decimal_places):
        # Performs calculations based on the entered numbers and operator
        result = None
        try:
            if operator == '+':
                result = number1 + number2
            elif operator == '-':
                result = number1 - number2
            elif operator == '*':
                result = number1 * number2
            elif operator == '/':
                if number2 == 0:
                    raise ZeroDivisionError
                else:
                    result = number1 / number2
            elif operator == '^':
                result = number1 ** number2
            elif operator == '√':
                result = math.sqrt(number1)
            elif operator == '%':
                result = number1 % number2
            return result
        except ZeroDivisionError:
            print(localization.BAN_FOR_ZERO)
            return None

    def get_continue_input(self):
        # Asks the user if they want to continue calculations
        return input(localization.CONTINUE_CALCULATION_PROMPT).lower()

    def run_calculator(self):
        # Main method for interacting with the user and performing calculations
        while True:
            number1 = self.get_number_from_user(localization.PROMPT_ENTER_FIRST_NUMBER)
            number2 = self.get_number_from_user(localization.PROMPT_ENTER_SECOND_NUMBER)
            operator = self.get_operator_from_user()
            decimal_places = int(input(localization.PROMPT_ENTER_DECIMAL_PLACES))

            result = self.perform_calculation(number1, number2, operator, decimal_places)

            if result is not None:
                self.memory = result

                expression = f"{number1:.{decimal_places}f} {operator} {number2:.{decimal_places}f} = {result:.{decimal_places}f}"
                self.calculation_records.append(expression)

                formatted_result = localization.RESULT_FORMAT.format(result=result, decimal_places=decimal_places)

                print(formatted_result)

                history_str = "\n".join(self.calculation_records)
                # join - joins all strings from the self.calculation_records list into one string, separating them with a newline character "\n".
                print(f"{localization.MEMORY_OPERATOR_HEADER}\n{history_str}")

            else:
                pass

            another_calculation = self.get_continue_input()
            if another_calculation != localization.CONTINUE_CALCULATION:
                break

if __name__ == "__main__":
    language_choice = input("Choose language (English/Ukrainian): ").strip().lower()
    # strip - removes all spaces (and other whitespace characters) from the beginning and end of the string.
    # lower - converts to lowercase.
    
    if language_choice == 'english':
        import en_localization as localization
    elif language_choice == 'ukrainian':
        import ua_localization as localization
    else:
        print("Invalid choice. Using English as default.")
        import en_localization as localization
