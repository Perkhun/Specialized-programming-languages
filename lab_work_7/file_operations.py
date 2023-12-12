import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os

class FileOperations:
    @staticmethod
    def save_representation(representation: str, representation_type: str, file_format: str):
        #Save a textual representation to a file. The Tkinter root window is used to create a dialog for selecting the file path.
        
        try:
            root = tk.Tk()
            root.withdraw()

            # Open a dialog for selecting the file path to save the representation
            file_path = filedialog.asksaveasfilename(
                defaultextension=f".{file_format}",
                filetypes=[(f"{file_format.upper()} files", f"*.{file_format}"), ("All files", "*.*")],
                title=f"Save {representation_type} representation as"
            )

            if not file_path:
                return

            # Write the representation to the selected file
            with open(file_path, "w", encoding='utf-8') as file:
                file.write(representation)

            messagebox.showinfo("Success", f"{representation_type} representation saved successfully to {file_path}")
        except (PermissionError, FileNotFoundError) as e:
            # Show an error message if there is an issue saving the file
            messagebox.showerror("Error", str(e))
        finally:
            root.destroy()

    @staticmethod
    def load_history_from_file():
        # Load history data from a JSON file and return list containing history data.

        module_directory = os.path.dirname(os.path.abspath(__file__))
        history_file_path = os.path.join(module_directory, 'history.json')

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
        # Save history data to a JSON file and list containing history data.

        module_directory = os.path.dirname(os.path.abspath(__file__))
        history_file_path = os.path.join(module_directory, 'history.json')

        try:
            with open(history_file_path, 'w', encoding='utf-8') as history_file:
                # Save the history data to the JSON file
                json.dump(history_data, history_file, ensure_ascii=False, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f'Error saving history file: {e}')
