import unittest
import requests.exceptions
from unittest.mock import Mock, patch, mock_open
from lab_work_7.api_handler import APIHandler
from lab_work_7.message_box_wrapper import MessageBoxWrapper
from lab_work_7.display_handler import DisplayHandler
from lab_work_7.input_parser import InputParser
from lab_work_7.file_operations import FileOperations

class TestAPIHandler(unittest.TestCase):

    @patch('api_handler.requests.get')
    def test_get_users_success(self, mock_get):
        # Testing the successful case of getting users from the API

        expected_data = [{'id': 1, 'firstname': 'John'}, {'id': 2, 'firstname': 'Jane'}]
        mock_get.return_value.json.return_value = expected_data

        # Act
        result = APIHandler.get_users()
        # Assert
        self.assertEqual(result, expected_data)

    @patch('api_handler.requests.get')
    @patch('message_box_wrapper.MessageBoxWrapper.show_error')
    def test_get_users_failure(self, mock_show_error, mock_get):
        # Testing the case where an exception occurs while getting users from the API
        mock_get.side_effect = requests.exceptions.RequestException("Fake Exception")

        # Act
        result = APIHandler.get_users()
        # Assert
        self.assertEqual(result, [])
        mock_show_error.assert_called_once_with("API Error", "Error getting data from API: Fake Exception")

    @patch('api_handler.requests.get')
    def test_get_user_by_id_success(self, mock_get):
        # Testing the successful case of getting user by ID from the API
        user_id = 1
        expected_data = {'id': user_id, 'firstname': 'John'}
        mock_get.return_value.json.return_value = expected_data

        # Act
        result = APIHandler.get_user_by_id(user_id)
        # Assert
        self.assertEqual(result, expected_data)

    @patch('api_handler.requests.get')
    @patch('message_box_wrapper.MessageBoxWrapper.show_error')
    def test_get_user_by_id_failure(self, mock_show_error, mock_get):
        # Testing the case where an exception occurs while getting user by ID from the API
        user_id = 1
        mock_get.side_effect = requests.exceptions.RequestException("Fake Exception")

        # Act
        result = APIHandler.get_user_by_id(user_id)
        # Assert
        self.assertEqual(result, {})
        mock_show_error.assert_called_once_with("API Error", f'Error getting user data from API: Fake Exception')

    def test_display_table_success(self):
        # Testing the successful case of displaying data in a table
        root_mock = Mock()
        data = [{'id': 1, 'firstname': 'John'}, {'id': 2, 'firstname': 'Jane'}]
        header_color = "black"
        table_bg_color = "white"

        # Act
        with patch('display_handler.messagebox') as messagebox_mock, \
             patch('display_handler.tk.Toplevel') as toplevel_mock:
            DisplayHandler.display_table(root_mock, data, header_color, table_bg_color)
        # Assert
        messagebox_mock.showinfo.assert_not_called()
        toplevel_mock.assert_called_once()

    def test_display_table_empty_data(self):
        # Testing the case of displaying an empty table
   
        root_mock = Mock()
        data = []
        header_color = "black"
        table_bg_color = "white"

        # Act
        with patch('display_handler.messagebox') as messagebox_mock, \
             patch('display_handler.tk.Toplevel') as toplevel_mock:
            DisplayHandler.display_table(root_mock, data, header_color, table_bg_color)
        # Assert
        messagebox_mock.showinfo.assert_called_once()
        toplevel_mock.assert_not_called()

    def test_display_list_success(self):
        # Testing the successful case of displaying data in a list

        root_mock = Mock()
        data = ['User 1', 'User 2']
        item_color = "green"
        list_bg_color = "lightblue"

        # Act
        with patch('display_handler.messagebox') as messagebox_mock, \
             patch('display_handler.tk.Toplevel') as toplevel_mock:
            DisplayHandler.display_list(root_mock, data, item_color, list_bg_color)
        # Assert
        messagebox_mock.showinfo.assert_not_called()
        toplevel_mock.assert_called_once()

    def test_display_list_empty_data(self):
        # Testing the case of displaying an empty list

        root_mock = Mock()
        data = []
        item_color = "black"
        list_bg_color = "white"

        # Act
        with patch('display_handler.messagebox') as messagebox_mock, \
             patch('display_handler.tk.Toplevel') as toplevel_mock:
            DisplayHandler.display_list(root_mock, data, item_color, list_bg_color)
        # Assert
        messagebox_mock.showinfo.assert_called_once()
        toplevel_mock.assert_not_called()

    def test_parse_full_name(self):
        # Testing the parsing of a full name
        result = InputParser.parse_user_input("John Doe")
        self.assertEqual(result, "Entered full name: John Doe")

    def test_parse_phone_number(self):
        # Testing the parsing of a phone number
        result = InputParser.parse_user_input("(123) 456-7890")
        self.assertEqual(result, "Entered phone number: (123) 456-7890")

    def test_parse_date(self):
        # Testing the parsing of a date
        result = InputParser.parse_user_input("2023-01-01")
        self.assertEqual(result, "Entered date: 2023-01-01")

    def test_parse_datetime(self):
        # Testing the parsing of a date and time
        result = InputParser.parse_user_input("2023-01-01 12:34:56")
        self.assertEqual(result, "Entered date and time: 2023-01-01 12:34:56")

    def test_parse_email(self):
        # Testing the parsing of an email
        result = InputParser.parse_user_input("test@example.com")
        self.assertEqual(result, "Entered email: test@example.com")

    def test_parse_website(self):
        # Testing the parsing of a website
        result = InputParser.parse_user_input("http://example.com")
        self.assertEqual(result, "Entered website: http://example.com")

    @patch('data_saver.DataSaver.save_history_entry')
    def test_save_history_entry_called(self, mock_save_history_entry):
        # Testing if save_history_entry is called
        user_input = "John Doe"
        InputParser.parse_user_input(user_input)
        mock_save_history_entry.assert_called_with(user_input)

    @patch("tkinter.filedialog.asksaveasfilename")
    @patch("tkinter.messagebox.showinfo")
    def test_save_representation(self, mock_showinfo, mock_file_dialog):
        # Testing saving representation to a file
        representation = "Test representation"
        representation_type = "Test Type"
        file_format = "txt"

        # Configure mock_file_dialog to return a file path
        mock_file_dialog.return_value = "test_file.txt"

        # Run the code that writes to the file
        FileOperations.save_representation(representation, representation_type, file_format)

        # Check if the function called the correct methods with the file
        mock_file_dialog.assert_called_once_with(
            defaultextension=f".{file_format}",
            filetypes=[(f"{file_format.upper()} files", f"*.{file_format}"), ("All files", "*.*")],
            title=f"Save {representation_type} representation as"
        )

        # Check if the showinfo method was not called
        mock_showinfo.assert_called_once_with("Success", f"{representation_type} representation saved successfully to test_file.txt")

    def test_load_history_from_file(self):
        # Testing loading history from a file
        # Create an empty history file
        with open('history.json', 'w', encoding='utf-8') as history_file:
            history_file.write('[]')

        # Now run the test
        history_data = FileOperations.load_history_from_file()

        # Perform assertions on history_data as needed
        self.assertEqual(history_data, [])


if __name__ == '__main__':
    unittest.main()
