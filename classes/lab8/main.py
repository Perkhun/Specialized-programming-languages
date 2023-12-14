import os
import tkinter as tk
from ui.menu.lab8.ui_lab8 import DataVisualizerGUI
from shared.runnable import Runnable

class App(Runnable):
    """
    Main application class for launching the Data Visualizer GUI.
    """
    def __init__(self, root):
        """
        Initialize the App.

        Parameters:
        - root (tk.Tk): The root Tkinter window.

        Returns:
        - None
        """
        # Initialize the main application
        self.root = root
        self.root.title("Main Application")
        self.root.focus_set()

        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Specify the correct relative path to employee_data.csv from the script's directory
        csv_file_path = os.path.join(script_dir, '..', '..', 'data', 'lab8', 'employee_data.csv')

        # Normalize the path to handle any path separators
        csv_file_path = os.path.normpath(csv_file_path)

        # Create an instance of the DataVisualizerGUI class
        self.data_visualizer = DataVisualizerGUI(self.root, csv_file_path)


    def run(self):
        """
        Run the main application loop.

        Returns:
        - None
        """
        # Run the main application event loop
        self.root.mainloop()

def main():
    """
    Main function to create the Tkinter root window and run the application.

    Returns:
    - None
    """
    # Entry point of the script
    root = tk.Tk()  # Create the main Tkinter window
    app = App(root)  # Create an instance of the App class
    app.run()  # Run the main application loop

if __name__ == "__main__":
    main()
