from tkinter import messagebox

class MessageBoxWrapper:
    @staticmethod
    def show_error(title, message):
        messagebox.showerror(title, message)