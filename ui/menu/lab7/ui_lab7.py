import tkinter as tk
from tkinter import Menu, messagebox
import unittest
import time
from classes.lab7.api_handler import APIHandler
from classes.lab7.data_saver import DataSaver
from classes.lab7.display_handler import DisplayHandler
from classes.lab7.input_parser import InputParser
from classes.lab7.file_operations import FileOperations
from classes.lab7.tests import TestAPIHandler
from shared.runnable import Runnable
from ui.menu_builder import Menu
from logs.logger import setup_logger, logger

class UIMenu(Menu):
    """A menu class for interacting with user data."""
    def __init__(self, root):
        """
        Initialize the UIMenu object.

        This method sets up the main graphical user interface by creating Tkinter variables
        and building the interface using the create_interface method.

        Parameters:
        - root (Tk): The root Tkinter window.

        """
        setup_logger()
        logger.info("Get API program started.")
        self.root = root
        self.root.title("Menu")
        # Розгорнути вікно на весь екран
        self.root.state('zoomed')

        # Initialize Tkinter variables
        self.init_tkinter_vars()

        # Create the interface
        self.create_interface()

    def init_tkinter_vars(self):
        """
        Initializes Tkinter variables used for GUI customization.
        """
        self.header_color_var = tk.StringVar()
        self.header_color_var.set("black")  # Значення за замовчуванням

        self.table_bg_color_var = tk.StringVar()
        self.table_bg_color_var.set("white")  # Значення за замовчуванням

        self.item_color_var = tk.StringVar()
        self.item_color_var.set("black")  # Значення за замовчуванням

        self.list_bg_color_var = tk.StringVar()
        self.list_bg_color_var.set("white")  # Значення за замовчуванням

        self.file_format_var = tk.StringVar()
        self.file_format_var.set("json")  # Значення за замовчуванням

    def create_interface(self):
        """
        Creates the main graphical user interface.
        """
        logger.info("Creating the main graphical user interface.")

        display_button = tk.Button(
            self.root,
            text="Display as a table",
            command=self.on_display_table
        )

        display_button.pack()

        # Кнопка для відображення списку
        display_button = tk.Button(
            self.root,
            text="Display as a list",
            command=self.on_display_list
        )
        display_button.pack()

        # Створення випадаючого меню для кольорів заголовків таблиці
        header_color_label = tk.Label(self.root, text="Choose a color for the table headers:")
        header_color_label.pack()

        header_color_menu = tk.OptionMenu(
            self.root,
            self.header_color_var,
            "black",
            "red",
            "green",
            "blue"
        )
        header_color_menu.pack()

        # Створення випадаючого меню для кольорів фону таблиці
        table_bg_color_label = tk.Label(self.root, text="Select the background color of the table:")
        table_bg_color_label.pack()

        table_bg_color_menu = tk.OptionMenu(
            self.root,
            self.table_bg_color_var,
            "white",
            "lightgray",
            "lightblue",
            "lightgreen"
        )
        table_bg_color_menu.pack()

        # Створення випадаючого меню для кольорів елементів списку
        item_color_label = tk.Label(self.root, text="Choose a color for the list items:")
        item_color_label.pack()

        item_color_menu = tk.OptionMenu(
            self.root,
            self.item_color_var,
            "black",
            "red",
            "green",
            "blue"
        )
        item_color_menu.pack()

        # Створення випадаючого меню для кольорів фону списку
        list_bg_color_label = tk.Label(self.root, text="Select the background color of the list:")
        list_bg_color_label.pack()

        list_bg_color_menu = tk.OptionMenu(
            self.root,
            self.list_bg_color_var,
            "white",
            "lightgray",
            "lightblue",
            "lightgreen"
        )
        list_bg_color_menu.pack()

        user_input_label = tk.Label(self.root, text="Enter a custom string:")
        user_input_label.pack()

        self.user_input_entry = tk.Entry(self.root)
        self.user_input_entry.pack()

        parse_button = tk.Button(self.root, text="Parse input", command=self.on_parse)
        parse_button.pack()

        self.result_text = tk.Text(self.root, wrap=tk.WORD, height=10, width=80)
        self.result_text.pack()

        # Додати поле введення для ID користувача
        self.entry_user_id = tk.Entry(self.root)
        self.entry_user_id.pack()

        # Додати кнопку для виклику функції get_user_by_id
        btn_get_user_by_id = tk.Button(
            self.root,
            text="Get User by ID",
            command=self.get_user_by_id
        )
        btn_get_user_by_id.pack()

        # Додайте кнопку, яка викликає функцію show_history
        show_history_button = tk.Button(
            self.root,
            text="Show history",
            command=self.show_history
        )
        show_history_button.pack()

        # Створення випадаючого меню для вибору формату
        format_label = tk.Label(self.root, text="Choose a format to save:")
        format_label.pack()

        file_format_menu = tk.OptionMenu(self.root, self.file_format_var, "json", "csv", "txt")
        file_format_menu.pack()

         # Кнопка для збереження даних
        save_button = tk.Button(self.root, text="Save", command=self.on_save)
        save_button.pack()

        # Кнопка для запуску тестів
        run_tests_button = tk.Button(self.root, text="Run the tests", command=self.run_tests)
        run_tests_button.pack()

        exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy)
        exit_button.pack()

    def on_display_table(self):
        """
        Displays data in a table format using DisplayHandler.
        """
        logger.info("Displaying data in a table format.")
        try:
            users_data = APIHandler.get_users()

            if not users_data:
                raise ValueError("No data.")

            DisplayHandler.display_table(self.root, users_data, self.header_color_var.get(), self.table_bg_color_var.get())
        except Exception as e:
            # Обробка помилок, виведення інформативного повідомлення
            logger.error(f"Error displaying data: {e}")
            self.show_result(f"Error displaying data {e}")

    def on_display_list(self):
        """
        Display data in list format using DisplayHandler.

        This method retrieves user data using the APIHandler, and if data is available, it calls DisplayHandler to display the data in a list format.
        If there is an error, it catches the exception and shows an informative message using the show_result method.

        """
        logger.info("Displaying data in a list format.")
        try:
            users_data = APIHandler.get_users()

            if not users_data:
                raise ValueError("No data.")

            DisplayHandler.display_list(self.root, users_data, self.item_color_var.get(), self.list_bg_color_var.get())
        except Exception as e:
            # Обробка помилок, виведення інформативного повідомлення
            logger.error(f"Error displaying data: {e}")
            self.show_result(f"Error displaying data: {e}")

    def on_parse(self):
        """
        Parse user input and display the result in a message box.

        This method retrieves the user input, parses it using the InputParser class, and shows the result in a message box.

        """
        user_input = self.user_input_entry.get()
        result = InputParser.parse_user_input(user_input)
        messagebox.showinfo("Result", result)

    def on_save(self):
        """
        Save user data in the selected format.

        This method retrieves user data using the APIHandler, gets the selected file format, and saves the data using the DataSaver class.

        """
        logger.info("Save API data to file.")
        users_data = APIHandler.get_users()
        selected_format = self.file_format_var.get()
        DataSaver.save_data(users_data, selected_format)

    def show_history(self):
        """
        Display the user input history.

        This method loads the user input history from a file using FileOperations and displays it in a message box.

        """
        logger.info("Show history.")
        history_data = FileOperations.load_history_from_file()
        if not history_data:
            messagebox.showinfo("History", "History is empty.")
        else:
            formatted_history = ""
            for entry in history_data:
                formatted_history += f"{entry['timestamp']} - {entry['user_input']}\n"

            messagebox.showinfo("Історія", formatted_history)

    def get_user_by_id(self):
        """
        Get user data by ID and display the result.

        This method retrieves the user ID, gets user data using the APIHandler, and shows the result using the show_result method.

        """
        user_id = self.entry_user_id.get()
        if user_id.isdigit():
            user_data = APIHandler.get_user_by_id(int(user_id))
            self.show_result(user_data)
        else:
            messagebox.showerror("Error", "Please enter a valid numeric user ID.")

    def show_result(self, result):
        """
        Display the result in the GUI.

        Args:
            result (str): The result to be displayed in the GUI.
        """
        self.result_text.config(state=tk.NORMAL)  # Дозволити редагування текстового поля
        self.result_text.delete(1.0, tk.END)  # Очистити текстове поле перед виведенням нових результатів
        self.result_text.insert(tk.END, result)
        self.result_text.config(state=tk.DISABLED)  # Заборонити редагування текстового поля

    def run_tests(self):
        """
        Run the test suite and display the results.

        This method runs the unit tests, calculates the execution time, and displays the test results in a message box.
        """
        logger.info("Running the test suite.")
        start_time = time.time()

        loader = unittest.TestLoader()
        suite = loader.loadTestsFromTestCase(TestAPIHandler)
        runner = unittest.TextTestRunner()
        result = runner.run(suite)

        # Обчислення часу виконання тестів
        end_time = time.time()
        execution_time = end_time - start_time

        # Викликайте show_test_results з об'єктом TestResult та часом виконання
        self.show_test_results(result, execution_time)

    def show_test_results(self, result, execution_time):
        """
        Display the results of the test run.

        Args:
            result (unittest.TestResult): The result object containing information about the test run.
            execution_time (float): The time taken for the test run in seconds.
        """
        if result.wasSuccessful():
            message = f"All tests were successfully passed!\n"
        else:
            message = f"{result.errors} errors, {result.failures} failure\n"

        message += f"Passed tests: {result.testsRun}\n"
        message += f"Test execution time: {execution_time:.3f} s"

        tk.messagebox.showinfo("Test results", message)

        logger.info("Get API program completed.")

    def run(self):
        """
        Runs the Tkinter main loop.
        """
        self.root.mainloop()
