"""
This is the main module for the calculator program.
It handles user input for language choice and initializes the calculator.
"""
from logs.logger import setup_logger, logger
from ui.menu.lab2.ui_lab2 import CalculatorUI
import tkinter as tk

def main():
    setup_logger()
    root = tk.Tk()
    app = CalculatorUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()