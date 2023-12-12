from lab_work_7.file_operations import FileOperations  # Importing FileOperations class from a custom module
import json
import csv
from datetime import datetime
from tkinter import messagebox  # Importing messagebox module from tkinter for displaying dialog boxes

history_entries = []  # Global list to store history entries

class DataSaver:
    @staticmethod
    def save_data(users_data, file_format):
        # Save user data in the specified file format.

        try:
            # Check the specified file format and handle accordingly
            if file_format == "json":
                # Convert user data to JSON format with indentation
                json_representation = json.dumps(users_data, ensure_ascii=False, indent=4)
                # Save JSON representation using FileOperations class
                FileOperations.save_representation(json_representation, "JSON", file_format)
            elif file_format == "csv":
                # Write user data to a CSV file
                with open('data.csv', 'w', newline='', encoding='utf-8') as csv_file:
                    csv_writer = csv.DictWriter(csv_file, fieldnames=users_data[0].keys())
                    csv_writer.writeheader()  # Write header with column names
                    csv_writer.writerows(users_data)  # Write user data rows
                # Read the CSV file to obtain the representation
                with open('data.csv', 'r', encoding='utf-8') as csv_file:
                    csv_representation = csv_file.read()
                # Save CSV representation using FileOperations class
                FileOperations.save_representation(csv_representation, "CSV", file_format)
            elif file_format == "txt":
                # Convert user data to a plain text representation
                txt_representation = "\n".join(str(line) for line in users_data)
                # Save text representation using FileOperations class
                FileOperations.save_representation(txt_representation, "TXT", file_format)
            else:
                # Display a message for unsupported file formats
                messagebox.showinfo("Unsupported Format", "Unsupported file format.")
        except Exception as e:
            # Handle any exceptions that may occur during the file-saving process
            messagebox.showerror("Error", f'Error saving data: {e}')

    @staticmethod
    def save_history_entry(user_input):
        # Saves a history entry with a timestamp and user input

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_entry = {'timestamp': timestamp, 'user_input': user_input}
        try:
            # Load existing history from the file
            history_data = FileOperations.load_history_from_file()

            # Append the new entry to the existing history
            history_data.append(new_entry)

            # Save the updated history back to the file
            FileOperations.save_history_to_file(history_data)

            # Update the in-memory history_entries list
            history_entries.append(new_entry)
        except Exception as e:
            messagebox.showerror("Error", f'Error saving history entry: {e}')
