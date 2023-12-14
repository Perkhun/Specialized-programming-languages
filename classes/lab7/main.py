"""
Module Docstring: A brief description of the module.
"""
import tkinter as tk
from ui.menu.lab7.ui_lab7 import UIMenu

def main():
    """
    Main function to create a Tkinter window and run the UIMenu.

    This function creates a Tkinter window and initializes the UIMenu,
    then runs the main loop of Tkinter.

    Raises:
        None
    """
    # Створення вікна Tkinter
    root = tk.Tk()
    ui_menu = UIMenu(root)
    # Запуск головного циклу Tkinter
    ui_menu.run()

if __name__ == "__main__":
    main()
