import os
import tkinter as tk
from lab_work_8.data_visualizer_gui import DataVisualizerGUI

class App:
    def __init__(self, master):
        # Initialize the main application
        self.master = master
        self.master.title("Main Application")

        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Construct the path to the CSV file (employee_data.csv)
        csv_file_path = os.path.join(script_dir, 'employee_data.csv')

        # Create an instance of the DataVisualizerGUI class
        self.data_visualizer = DataVisualizerGUI(self.master, csv_file_path)

    def run(self):
        # Run the main application event loop
        self.master.mainloop()

def main():
    # Entry point of the script
    root = tk.Tk()  # Create the main Tkinter window
    app = App(root)  # Create an instance of the App class
    app.run()  # Run the main application loop

if __name__ == "__main__":
    # Check if the script is run as the main module
    main()  # Call the main function to start the application
