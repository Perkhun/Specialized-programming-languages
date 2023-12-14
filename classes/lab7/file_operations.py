from tkinter import messagebox
import json
import os

class FileOperations:
    """
    FileOperations is a utility class for handling file-related operations,
    including saving representations and managing history data.

    Methods:

    - load_history_from_file():
        Load history data from a file.

    - save_history_to_file(history_data):
        Save history data to a file.

    Usage:
    - Create an instance of FileOperations to perform file-related operations.

    Example:
    ```python
    file_ops = FileOperations()

    # Load history data from a file
    history_data = file_ops.load_history_from_file()

    # Save updated history data to a file
    file_ops.save_history_to_file(history_data)
    ```
    """
    @staticmethod
    def load_history_from_file():
        """
        Load history data from a file.

        Returns:
        - list: List containing history data.

        Raises:
        - json.JSONDecodeError: If there is an issue decoding JSON from the history file.
        """
        # Отримання шляху до поточного модуля
        history_file_path = "data/lab7/history.json"

        try:
            if os.path.exists(history_file_path):
                with open(history_file_path, 'r', encoding='utf-8') as history_file:
                    history_data = json.load(history_file)
            else:
                history_data = []
        except json.JSONDecodeError as e:
            messagebox.showerror("Error", f'Error decoding JSON from history file: {e}')
            history_data = []

        return history_data

    @staticmethod
    def save_history_to_file(history_data):
        """
        Save history data to a file.

        Args:
        - history_data (list): List containing history data.

        Raises:
        - Exception: If there is an issue saving the history file.
        """
        # Отримання шляху до поточного модуля
        history_file_path = "data/lab7/history.json"

        try:
            with open(history_file_path, 'w', encoding='utf-8') as history_file:
                json.dump(history_data, history_file, ensure_ascii=False, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f'Error saving history file: {e}')
