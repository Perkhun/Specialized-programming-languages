from lab_work_7.data_saver import DataSaver
import re
from datetime import datetime

class InputParser:
    @staticmethod
    def parse_user_input(user_input):
        # Define a pattern for the full name using a regular expression
        full_name_pattern = r'^[A-Z][a-z]+ [A-Z][a-z]+$'

        # Define a pattern for the phone number using a regular expression
        phone_pattern = r'^\(\d{3}\) \d{3}-\d{4}$'

        # Define a pattern for the date using a regular expression
        date_pattern = r'\d{4}-\d{2}-\d{2}$'

        # Define a pattern for the date and time using a regular expression
        datetime_pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'

        # Define a pattern for the email using a regular expression
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

        # Define a pattern for the website using a regular expression
        website_pattern = r'^(http|https)://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        # Check if the input matches any of the patterns
        if re.match(full_name_pattern, user_input):
            result = f"Entered full name: {user_input}"
        elif re.match(phone_pattern, user_input):
            result = f"Entered phone number: {user_input}"
        elif re.match(date_pattern, user_input):
            try:
                parsed_date = datetime.strptime(user_input, '%Y-%m-%d').date()
                result = f"Entered date: {parsed_date}"
            except ValueError:
                result = "Unable to parse the date."
        elif re.match(datetime_pattern, user_input):
            try:
                parsed_datetime = datetime.strptime(user_input, '%Y-%m-%d %H:%M:%S')
                result = f"Entered date and time: {parsed_datetime}"
            except ValueError:
                result = "Unable to parse the date and time."
        elif re.match(email_pattern, user_input):
            result = f"Entered email: {user_input}"
        elif re.match(website_pattern, user_input):
            result = f"Entered website: {user_input}"
        else:
            result = "Unable to determine the input format."

        # Change: Passing user_input to the save_history_entry function
        DataSaver.save_history_entry(user_input)

        return result
