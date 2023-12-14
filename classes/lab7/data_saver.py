import json
import csv
from datetime import datetime
from tkinter import messagebox
from tkinter import filedialog
from shared.file_operations import FileOperations
from .file_operations import FileOperations as load_save

history_entries = []

class DataSaver:
    """Class for saving data and history entries."""
    @staticmethod
    def save_data(users_data, file_format):
        """
        Save user data in the specified file format.

        Args:
            users_data (list): List of user data.
            file_format (str): File format (json, csv, txt).

        Raises:
            ValueError: If an unsupported file format is provided.
            Exception: If an error occurs during saving.
        """
        try:
            if file_format == "json":
                json_representation = json.dumps(users_data, ensure_ascii=False, indent=4)
                file_path = filedialog.asksaveasfilename(
                    defaultextension=f".{file_format}",
                    filetypes=[(f"{file_format.upper()} files", f"*.{file_format}"), ("All files", "*.*")],
                    title=f"Save {json_representation} representation as",
                    initialdir="data/lab7", initialfile="api_data"
                )
                if file_path:
                    FileOperations.save_representation(json_representation, "JSON", file_format, file_path)

            elif file_format == "csv":
                with open('data.csv', 'w', newline='', encoding='utf-8') as csv_file:
                    csv_writer = csv.DictWriter(csv_file, fieldnames=users_data[0].keys())
                    csv_writer.writeheader()
                    csv_writer.writerows(users_data)

                with open('data.csv', 'r', encoding='utf-8') as csv_file:
                    csv_representation = csv_file.read()
                    file_path = filedialog.asksaveasfilename(
                        defaultextension=f".{file_format}",
                        filetypes=[(f"{file_format.upper()} files", f"*.{file_format}"), ("All files", "*.*")],
                        title=f"Save {csv_representation} representation as",
                        initialdir="data/lab7", initialfile="api_data"
                    )

                if file_path:
                    FileOperations.save_representation(csv_representation, "CSV", file_format, file_path)

            elif file_format == "txt":
                txt_representation = "\n".join(str(line) for line in users_data)
                file_path = filedialog.asksaveasfilename(
                    defaultextension=f".{file_format}",
                    filetypes=[(f"{file_format.upper()} files", f"*.{file_format}"), ("All files", "*.*")],
                    title=f"Save {txt_representation} representation as",
                    initialdir="data/lab7", initialfile="api_data"
                )

                if file_path:
                    FileOperations.save_representation(txt_representation, "TXT", file_format, file_path)

            else:
                messagebox.showinfo("Unsupported Format", "Unsupported file format.")
        except Exception as e:
            messagebox.showerror("Error", f'Error saving data: {e}')

    @staticmethod
    def save_history_entry(user_input):
        """
        Save user input as a history entry.

        Args:
            user_input (str): User input.

        Raises:
            Exception: If an error occurs during saving.
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_entry = {'timestamp': timestamp, 'user_input': user_input}
        try:
            # Load existing history from the file
            history_data = load_save.load_history_from_file()

            # Append the new entry to the existing history
            history_data.append(new_entry)

            # Save the updated history back to the file
            load_save.save_history_to_file(history_data)

            # Update the in-memory history_entries list
            history_entries.append(new_entry)
        except Exception as e:
            messagebox.showerror("Error", f'Error saving history entry: {e}')
