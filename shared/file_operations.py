"""Module for handling file operations."""
from tkinter import messagebox, Tk

class FileOperations:
    """
    Class for handling file operations.
    """
    @staticmethod
    def save_representation(representation: str, representation_type: str, file_format: str, file_path: str):
        """
        Save the representation to a file.

        Args:
            representation (str): The data to be saved.
            representation_type (str): Type of representation.
            file_format (str): Format of the file.
            file_path (str): Path where the file will be saved.
        """
        try:
            # Create a Tkinter root window (invisible)
            root = Tk()
            root.withdraw()

            # Check if the user canceled the file selection
            if not file_path:
                return

            # Write the representation to the selected file
            with open(file_path, "w", encoding='utf-8') as file:
                file.write(representation)

            # Display a success message
            messagebox.showinfo("Success", f"{representation_type} representation saved successfully to {file_path}")
        except (PermissionError, FileNotFoundError) as e:
            # Display an error message if an exception occurs during file saving
            messagebox.showerror("Error", str(e))
        finally:
            # Destroy the Tkinter root window to free resources
            root.destroy()
