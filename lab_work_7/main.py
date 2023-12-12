import tkinter as tk
from tkinter import messagebox
import unittest
import time
from lab_work_7.api_handler import APIHandler
from lab_work_7.data_saver import DataSaver
from lab_work_7.display_handler import DisplayHandler
from lab_work_7.input_parser import InputParser
from lab_work_7.file_operations import FileOperations
from lab_work_7.tests import TestAPIHandler

class App:
    def __init__(self, root):
        # Initialize the Tkinter application
        self.root = root
        self.root.title("Data Display Menu")
        # Expand the window to full screen
        self.root.state('zoomed')

        # Initialize Tkinter variables
        self.init_tkinter_vars()

        # Create the graphical user interface
        self.create_interface()

    def init_tkinter_vars(self):
        # Initialize Tkinter variables for color options and file format
        self.header_color_var = tk.StringVar()
        self.header_color_var.set("black")  # Default value

        self.table_bg_color_var = tk.StringVar()
        self.table_bg_color_var.set("white")  # Default value

        self.item_color_var = tk.StringVar()
        self.item_color_var.set("black")  # Default value

        self.list_bg_color_var = tk.StringVar()
        self.list_bg_color_var.set("white")  # Default value

        self.file_format_var = tk.StringVar()
        self.file_format_var.set("json")  # Default value

    def create_interface(self):
        # Create interface elements
        # Button to display data in a table
        display_button_table = tk.Button(self.root, text="Display as Table", command=self.on_display_table)
        display_button_table.pack()

        # Button to display data in a list
        display_button_list = tk.Button(self.root, text="Display as List", command=self.on_display_list)
        display_button_list.pack()

        # Dropdown menu for text color in the table
        header_color_label = tk.Label(self.root, text="Select text color in the table:")
        header_color_label.pack()
        header_color_menu = tk.OptionMenu(self.root, self.header_color_var, "black", "red", "green", "blue")
        header_color_menu.pack()

        # Dropdown menu for background color in the table
        table_bg_color_label = tk.Label(self.root, text="Select background color in the table:")
        table_bg_color_label.pack()
        table_bg_color_menu = tk.OptionMenu(self.root, self.table_bg_color_var, "white", "lightgray", "lightblue", "lightgreen")
        table_bg_color_menu.pack()

        # Dropdown menu for text color in the list
        item_color_label = tk.Label(self.root, text="Select text color for list items:")
        item_color_label.pack()
        item_color_menu = tk.OptionMenu(self.root, self.item_color_var, "black", "red", "green", "blue")
        item_color_menu.pack()

        # Dropdown menu for background color in the list
        list_bg_color_label = tk.Label(self.root, text="Select background color for the list:")
        list_bg_color_label.pack()
        list_bg_color_menu = tk.OptionMenu(self.root, self.list_bg_color_var, "white", "lightgray", "lightblue", "lightgreen")
        list_bg_color_menu.pack()

        # Label and Entry for user input
        user_input_label = tk.Label(self.root, text="Enter user input:")
        user_input_label.pack()
        self.user_input_entry = tk.Entry(self.root)
        self.user_input_entry.pack()

        # Button to parse user input
        parse_button = tk.Button(self.root, text="Parse Input", command=self.on_parse)
        parse_button.pack()

        # Text widget to display results
        self.result_text = tk.Text(self.root, wrap=tk.WORD, height=10, width=80)
        self.result_text.pack()

        # Entry for user ID
        self.entry_user_id = tk.Entry(self.root)
        self.entry_user_id.pack()

        # Button to get user by ID
        btn_get_user_by_id = tk.Button(self.root, text="Get User by ID", command=self.get_user_by_id)
        btn_get_user_by_id.pack()

        # Button to show history
        show_history_button = tk.Button(self.root, text="Show History", command=self.show_history)
        show_history_button.pack()

        # Dropdown menu for file format
        format_label = tk.Label(self.root, text="Select format for saving:")
        format_label.pack()
        file_format_menu = tk.OptionMenu(self.root, self.file_format_var, "json", "csv", "txt")
        file_format_menu.pack()

        # Button to save data
        save_button = tk.Button(self.root, text="Save", command=self.on_save)
        save_button.pack()

       

        # Button to exit the application
        exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy)
        exit_button.pack()

    def on_display_table(self):
        # Callback function for displaying data in a table
        try:
            users_data = APIHandler.get_users()
            if not users_data:
                raise ValueError("No data to display.")
            DisplayHandler.display_table(self.root, users_data, self.header_color_var.get(), self.table_bg_color_var.get())
        except Exception as e:
            # Handle errors and display an informative message
            self.show_result(f"Error displaying data: {e}")

    def on_display_list(self):
        # Callback function for displaying data in a list
        try:
            users_data = APIHandler.get_users()
            if not users_data:
                raise ValueError("No data to display.")
            DisplayHandler.display_list(self.root, users_data, self.item_color_var.get(), self.list_bg_color_var.get())
        except Exception as e:
            # Handle errors and display an informative message
            self.show_result(f"Error displaying data: {e}")

    def on_parse(self):
        # Callback function for parsing user input
        user_input = self.user_input_entry.get()
        result = InputParser.parse_user_input(user_input)
        messagebox.showinfo("Result", result)

    def on_save(self):
        # Callback function for saving data
        users_data = APIHandler.get_users()
        selected_format = self.file_format_var.get()
        DataSaver.save_data(users_data, selected_format)

    def show_history(self):
        # Callback function to show history
        history_data = FileOperations.load_history_from_file()
        if not history_data:
            messagebox.showinfo("History", "History is empty.")
        else:
            formatted_history = ""
            for entry in history_data:
                formatted_history += f"{entry['timestamp']} - {entry['user_input']}\n"
            messagebox.showinfo("History", formatted_history)

    def get_user_by_id(self):
        # Callback function to get a user by ID and display the result
        user_id = self.entry_user_id.get()
        if user_id.isdigit():
            user_data = APIHandler.get_user_by_id(int(user_id))
            self.show_result(user_data)
        else:
            messagebox.showerror("Error", "Please enter a valid numeric user ID.")

    def show_result(self, result):
        # Function to display results in the text widget
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)
        self.result_text.config(state=tk.DISABLED)

    def run_tests(self):
        # Function to run tests
        start_time = time.time()
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromTestCase(TestAPIHandler)
        runner = unittest.TextTestRunner()
        result = runner.run(suite)
        end_time = time.time()
        execution_time = end_time - start_time
        self.show_test_results(result, execution_time)

    def show_test_results(self, result, execution_time):
        # Function to display test results
        if result.wasSuccessful():
            message = f"All tests passed!\n"
        else:
            message = f"{result.errors} errors, {result.failures} failures\n"

        message += f"Total tests run: {result.testsRun}\n"
        message += f"Execution time: {execution_time:.3f} seconds"

        tk.messagebox.showinfo("Test Results", message)

def main():
    # Create the Tkinter window
    root = tk.Tk()
    app = App(root)
    # Run the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()
