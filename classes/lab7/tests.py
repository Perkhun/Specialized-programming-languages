"""
Module Docstring: A brief description of the module.
"""
import unittest
import os
from unittest.mock import Mock, patch, mock_open
import requests.exceptions
from classes.lab7.api_handler import APIHandler
from classes.lab7.message_box_wrapper import MessageBoxWrapper
from classes.lab7.display_handler import DisplayHandler
from classes.lab7.input_parser import InputParser
from classes.lab7.file_operations import FileOperations

class TestAPIHandler(unittest.TestCase):

    """
    Test class for the APIHandler class.
    """
    @patch('classes.lab7.api_handler.requests.get')
    def test_get_users_success(self, mock_get):
        """
        Test the get_users method for a successful API request.
        """
        # Arrange
        expected_data = [{'id': 1, 'firstname': 'John'}, {'id': 2, 'firstname': 'Jane'}]
        mock_get.return_value.json.return_value = expected_data

        # Act
        result = APIHandler.get_users()

        # Assert
        self.assertEqual(result, expected_data)

    @patch('classes.lab7.api_handler.requests.get')
    @patch('message_box_wrapper.MessageBoxWrapper.show_error')
    def test_get_users_failure(self, mock_show_error, mock_get):
        """
        Test the get_users method for a failed API request.
        """
        # Arrange
        mock_get.side_effect = requests.exceptions.RequestException("Fake Exception")

        # Act
        result = APIHandler.get_users()

        # Assert
        self.assertEqual(result, [])
        mock_show_error.assert_called_once_with("API Error", "Error getting data from API: Fake Exception")

    @patch('classes.lab7.api_handler.requests.get')
    def test_get_user_by_id_success(self, mock_get):
        # Arrange
        user_id = 1
        expected_data = {'id': user_id, 'firstname': 'John'}
        mock_get.return_value.json.return_value = expected_data

        # Act
        result = APIHandler.get_user_by_id(user_id)

        # Assert
        self.assertEqual(result, expected_data)

    @patch('classes.lab7.api_handler.requests.get')
    @patch('message_box_wrapper.MessageBoxWrapper.show_error')
    def test_get_user_by_id_failure(self, mock_show_error, mock_get):
        # Arrange
        user_id = 1
        mock_get.side_effect = requests.exceptions.RequestException("Fake Exception")

        # Act
        result = APIHandler.get_user_by_id(user_id)

        # Assert
        self.assertEqual(result, {})
        mock_show_error.assert_called_once_with("API Error", f'Error getting user data from API: Fake Exception')

    def test_display_table_success(self):
        # Arrange
        root_mock = Mock()
        data = [{'id': 1, 'firstname': 'John'}, {'id': 2, 'firstname': 'Jane'}]
        header_color = "black"
        table_bg_color = "white"

        # Act
        with patch('classes.lab7.display_handler.messagebox') as messagebox_mock, \
             patch('classes.lab7.display_handler.tk.Toplevel') as toplevel_mock:
            DisplayHandler.display_table(root_mock, data, header_color, table_bg_color)

        # Assert
        messagebox_mock.showinfo.assert_not_called()
        toplevel_mock.assert_called_once()

    def test_display_table_empty_data(self):
        # Arrange
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
        # Arrange
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
        # Arrange
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
        result = InputParser.parse_user_input("John Doe")
        self.assertEqual(result, "Full name entered: John Doe")

    def test_parse_phone_number(self):
        result = InputParser.parse_user_input("(123) 456-7890")
        self.assertEqual(result, "Phone number entered: (123) 456-7890")

    def test_parse_date(self):
        result = InputParser.parse_user_input("2023-01-01")
        self.assertEqual(result, "Date entered: 2023-01-01")

    def test_parse_datetime(self):
        result = InputParser.parse_user_input("2023-01-01 12:34:56")
        self.assertEqual(result, "Date and time entered 2023-01-01 12:34:56")

    def test_parse_email(self):
        result = InputParser.parse_user_input("test@example.com")
        self.assertEqual(result, "Email entered: test@example.com")

    def test_parse_website(self):
        result = InputParser.parse_user_input("http://example.com")
        self.assertEqual(result, "Website entered: http://example.com")

    @patch('data_saver.DataSaver.save_history_entry')
    def test_save_history_entry_called(self, mock_save_history_entry):
        user_input = "John Doe"
        InputParser.parse_user_input(user_input)
        mock_save_history_entry.assert_called_with(user_input)

    @patch("tkinter.filedialog.asksaveasfilename")
    @patch("tkinter.messagebox.showinfo")
    def test_save_representation(self, mock_showinfo, mock_file_dialog):
        """
        Test the save_representation method.
        """
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
        # Determine the expected path based on the current test directory
        test_directory = os.path.dirname(os.path.abspath(__file__))
        expected_path = os.path.join(test_directory, 'history.json')

        # Create an empty history file
        with open(expected_path, 'w', encoding='utf-8') as history_file:
            history_file.write('[]')

        # Now run the test
        history_data = FileOperations.load_history_from_file()

        # Perform assertions on history_data as needed
        self.assertEqual(history_data, [])

        # Clean up: remove the history file after the test
        os.remove(expected_path)

    # def test_save_history_to_file(self):
    #     # Create a mock open function
    #     m = mock_open()

    #     # Patch the built-in open function to use the mock open
    #     with patch("builtins.open", m):
    #         # Run the code that writes to the file
    #         FileOperations.save_history_to_file([{"timestamp": "2023-01-01 12:00:00", "user_input": "test input"}])

    #     # Check if the open method was called with the expected mode at least once
    #     m.assert_any_call('history.json', 'w', encoding='utf-8')

    #     # Check if the write method is called with the expected content
    #     expected_content = [{"timestamp": "2023-01-01 12:00:00", "user_input": "test input"}]
    #     handle = m()

    #     # Assert that the expected content is in the actual content
    #     calls = handle.write.call_args_list
    #     actual_content = ''.join([call_args[0][0] for call_args in calls])

    #     # Replace newline characters for correct JSON decoding
    #     actual_content = actual_content.replace('\n', '').replace('\r', '')

    #     # Load the actual content as a JSON object
    #     actual_content_json = json.loads(actual_content)

    #     # Assert that the expected JSON content is in the actual JSON content
    #     self.assertIn(expected_content[0], actual_content_json)

if __name__ == '__main__':
    unittest.main()
