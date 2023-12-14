import re
from datetime import datetime
from .data_saver import DataSaver

class InputParser:
    """
    InputParser is a utility class for parsing user input and determining its format.

    Methods:
    - parse_user_input(user_input):
        Parse the given user input and determine its format, such as full name, phone number, date, etc.

    Usage:
    - Create an instance of InputParser to parse user input.

    Example:
    ```python
    input_parser = InputParser()

    # Parse user input
    user_input = "John Doe"
    result = input_parser.parse_user_input(user_input)
    print(result)
    ```

    Result:
    ```
    Entered full name: John Doe
    ```

    Note: The result may vary based on the input format.
    """
    @staticmethod
    def parse_user_input(user_input):
        """
        Parse the given user input and determine its format.

        Args:
        - user_input (str): The user input to be parsed.

        Returns:
        - str: A string indicating the format of the user input.

        Example:
        ```python
        input_parser = InputParser()
        user_input = "John Doe"
        result = input_parser.parse_user_input(user_input)
        print(result)
        ```

        Result:
        ```
        Entered full name: John Doe
        ```
        """
        # Визначаємо шаблон для регулярного виразу для повного імені
        full_name_pattern = r'^[A-Z][a-z]+ [A-Z][a-z]+$'

        # Визначаємо шаблон для регулярного виразу для номера телефону
        phone_pattern = r'^\(\d{3}\) \d{3}-\d{4}$'

        # Визначаємо шаблон для регулярного виразу для дати
        date_pattern = r'\d{4}-\d{2}-\d{2}$'

        # Визначаємо шаблон для регулярного виразу для дати та часу
        datetime_pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'

        # Визначаємо шаблон для регулярного виразу для електронної пошти
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

        # Визначаємо шаблон для регулярного виразу для веб-сайту
        website_pattern = r'^(http|https)://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        # Перевіряємо, чи введення відповідає якомусь з шаблонів
        if re.match(full_name_pattern, user_input):
            result = f"Full name entered: {user_input}"
        elif re.match(phone_pattern, user_input):
            result = f"Phone number entered: {user_input}"
        elif re.match(date_pattern, user_input):
            try:
                parsed_date = datetime.strptime(user_input, '%Y-%m-%d').date()
                result = f"Date entered: {parsed_date}"
            except ValueError:
                result = "Failed to parse date."
        elif re.match(datetime_pattern, user_input):
            try:
                parsed_datetime = datetime.strptime(user_input, '%Y-%m-%d %H:%M:%S')
                result = f"Date and time entered: {parsed_datetime}"
            except ValueError:
                result = "Failed to parse date and time."
        elif re.match(email_pattern, user_input):
            result = f"Email entered: {user_input}"
        elif re.match(website_pattern, user_input):
            result = f"Website entered: {user_input}"
        else:
            result = "Unable to determine the input format."

       # Змінено: передача user_input у функцію save_history_entry
        DataSaver.save_history_entry(user_input)

        return result
