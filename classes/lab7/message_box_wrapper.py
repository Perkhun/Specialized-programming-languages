"""
Module Docstring: A brief description of the module.
"""
from tkinter import messagebox

class MessageBoxWrapper:
    """
    A class providing a static method to show error messages using Tkinter's messagebox.
    """
    @staticmethod
    def show_error(title, message):
        """
        Display an error message using Tkinter's messagebox.

        Args:
            title (str): The title of the messagebox.
            message (str): The error message to be displayed.

        Returns:
            None
        """
        messagebox.showerror(title, message)
