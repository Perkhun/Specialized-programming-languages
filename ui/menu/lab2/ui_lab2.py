"""
Module for creating the CalculatorUI class and UI related functionalities.
"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from classes.lab2.scientific_calculator import ScientificCalculator
from classes.lab2.en_localization import EnglishLocalization
from classes.lab2.ua_localization import UkrainianLocalization

class CalculatorUI:
    """
    Class for creating the calculator user interface.
    """
    def __init__(self, root):
        """
        Initialize the CalculatorUI.

        Parameters:
            root (tk.Tk): The Tkinter root window.
        """
        self.root = root
        self.root.title("Calculator")

        self.create_widgets()

    def create_widgets(self):
        """
        Create UI widgets.
        """
        ttk.Label(self.root, text="Choose language:").grid(row=0, column=0, pady=10)

        self.language_var = tk.StringVar()
        self.language_var.set("English")

        language_combobox = ttk.Combobox(self.root, textvariable=self.language_var, values=["English", "Ukrainian"])
        language_combobox.grid(row=0, column=1, pady=10)

        calculate_button = ttk.Button(self.root, text="Calculate", command=self.calculate)
        calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

    def calculate(self):
        """
        Perform calculation based on user input.
        """
        language_choice = self.language_var.get().lower()

        if language_choice == 'english':
            localization = EnglishLocalization()
        elif language_choice == 'ukrainian':
            localization = UkrainianLocalization()
        else:
            print("Invalid choice. Using English as default.")
            localization = EnglishLocalization()

        calculator = ScientificCalculator(localization)
        result = calculator.run_calculator()

        # Display the result in a messagebox
        messagebox.showinfo("Result", f"The result is: {result}")
