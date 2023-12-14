"""
DataVisualizerGUI Module

This module defines the DataVisualizerGUI class, which is a graphical user interface
for visualizing and analyzing data from a CSV file. It uses Tkinter for the GUI, Matplotlib
for plotting, and includes functionalities for displaying various types of plots and
analyzing data characteristics.

Author: Ira

Usage:
    Create an instance of DataVisualizerGUI by providing a Tkinter master window and
    a CSV file path. The GUI allows users to choose different types of plots, analyze data
    characteristics, and export plots as images.

Note: This module depends on the following external libraries:
    - Tkinter
    - Matplotlib
    - Pandas
"""
from tkinter import ttk, messagebox
import tkinter as tk
from matplotlib import pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from classes.lab8.data_loader import DataLoader
from classes.lab8.plot_generator import PlotGenerator
from classes.lab8.file_exporter import FileExporter
from logs.logger import setup_logger, logger

class DataVisualizerGUI:
    """
    A class for creating a GUI to visualize data from a CSV file.
    """
    def __init__(self, master, csv_file):
        """
        Initializes the DataVisualizerGUI.

        Parameters:
        - master (tk.Tk): The root Tkinter window.
        - csv_file (str): Path to the CSV file containing data.

        """
        setup_logger()
        logger.info("Visualizer program started.")
        self.master = master
        self.master.title("Data Visualizer GUI")

        self.data = DataLoader.load_csv(csv_file)
        self.columns = list(self.data.columns)
        self.info_label = None
        self.current_plot = None
        self.export_button = None

        self.plot_types = ['Histogram (Age)', 'Bar (Department & Salary)', 'Scatter (Experience & Salary)',
                           'Pie (Gender)', 'Line (Salary & Time)', 'Bar (Department Distribution)']

        self.plot_type_combobox = ttk.Combobox(self.master, values=self.plot_types)

        show_plot_button = tk.Button(self.master, text="Display the graph", command=self.show_selected_plot)

        self.column_combobox = ttk.Combobox(self.master, values=self.columns)

        show_extremes_button = tk.Button(self.master, text="Show extreme values", command=self.show_extremes)

        self.plot_container = tk.Frame(self.master)

        show_multiple_subplots_button = tk.Button(self.master, text="Show multiple subplots", command=self.show_multiple_subplots)

        self.plot_type_combobox.pack(pady=5)
        show_plot_button.pack(pady=5)
        self.column_combobox.pack(pady=5)
        show_extremes_button.pack(pady=5)
        show_multiple_subplots_button.pack(pady=5)
        self.plot_container.pack(pady=5)

        self.export_button = tk.Button(self.master, text="Export graph", command=self.export_current_plot_as_image)

    def show_extremes(self):
        """
        Shows extreme values for the selected column.

        """
        logger.info("Shows extreme values.")
        selected_column = self.column_combobox.get()

        if not selected_column:
            messagebox.showinfo("Error", "Please select a column to analyze.")
            return

        if self.info_label:
            self.info_label.pack_forget()

        for widget in self.plot_container.winfo_children():
            widget.destroy()

        if self.data[selected_column].dtype == 'object':
            if selected_column == 'birth_date':
                min_date = self.data[selected_column].min()
                max_date = self.data[selected_column].max()

                extremes = pd.Series({
                    'Minimum date': min_date,
                    'Maximum date': max_date
                })

                info_text = f"Column information {selected_column}:\n"
                info_text += f"Minimum date: {min_date}\n"
                info_text += f"Maximum date: {max_date}"

                self.show_info_in_gui(info_text)

                self.plot_extremes_dates(extremes)
            else:
                unique_values = len(self.data[selected_column].unique())
                most_common_value = self.data[selected_column].mode().iloc[0]
                most_common_count = self.data[selected_column].value_counts().iloc[0]

                extremes = pd.Series({
                    'Unique Values': unique_values,
                    'Most Common Value': f"{most_common_value} (Number: {most_common_count})"
                })

                info_text = f"Column information {selected_column}:\n"
                info_text += f"Number of unique values: {unique_values}\n"
                info_text += f"The most common value: {most_common_value} (Number: {most_common_count})"

                self.show_info_in_gui(info_text)
        else:
            extremes = self.data[selected_column].describe()
            self.plot_extremes_numeric(extremes)

    def show_selected_plot(self):
        """
        Show  based on the chosen plot type.

        This method retrieves the selected plot type from the ComboBox,
        clears existing widgets in the plot container, and calls the
        corresponding plot generation method.

        """
        selected_plot_type = self.plot_type_combobox.get()
        logger.info(f"Show the selected plot type: {selected_plot_type}")

        if not selected_plot_type :
            messagebox.showinfo("Error", "Please select a chart type.")
            return

        if self.info_label:
            self.info_label.pack_forget()

        for widget in self.plot_container.winfo_children():
            widget.destroy()

        if selected_plot_type == 'Histogram (Age)':
            self.plot_histogram_age()
        elif selected_plot_type == 'Bar (Department & Salary)':
            self.plot_bar_department_salary()
        elif selected_plot_type == 'Scatter (Experience & Salary)':
            self.plot_scatter_experience_salary()
        elif selected_plot_type == 'Pie (Gender)':
            self.plot_pie_gender()
        elif selected_plot_type == 'Line (Salary & Time)':
            self.plot_line_salary_time()
        elif selected_plot_type == 'Bar (Department Distribution)':
            self.plot_bar_department_distribution()

    def show_info_in_gui(self, info_text):
        """
        Display information in the GUI.

        This method clears existing widgets in the plot container and, if
        applicable, destroys the export button. Then, it creates a new
        label with the provided information text and displays it in the plot
        container.

        :param info_text: The information text to display in the GUI.
        :type info_text: str
        """
        for widget in self.plot_container.winfo_children():
            widget.destroy()

        if self.export_button:
            self.export_button.destroy()

        self.info_label = tk.Label(self.plot_container, text=info_text)
        self.info_label.pack()

    def plot_extremes_dates(self, extremes):
        """
        Plot extremes for date values.

        This method generates a bar plot for the provided extremes, where
        the extremes include the minimum and maximum dates.

        :param extremes: The extremes containing minimum and maximum dates.
        :type extremes: pd.Series
        """
        fig, ax = plt.subplots()

        min_date = pd.to_datetime(extremes['Minimum date'])
        max_date = pd.to_datetime(extremes['Maximum date'])

        ax.bar(['Minimum date', 'Maximum date'], [min_date, max_date])
        ax.set_title("Extreme Values (Text Box)")
        ax.set_ylabel("Date")
        ax.set_xlabel("Characteristic")

        self.update_plot(fig)

    def plot_extremes_numeric(self, extremes):
        """
        Plot numeric extremes.

        This method generates a bar plot for the provided numeric extremes.

        :param extremes: The extremes containing numeric values.
        :type extremes: pd.Series
        """
        fig, ax = plt.subplots()

        extremes.plot(kind='bar', ax=ax)
        ax.set_title("Extreme values (Numeric field)")
        ax.set_ylabel("Value")
        ax.set_xlabel("Characteristic")

        self.update_plot(fig)

    def update_plot(self, fig):
        """
        Update the plot in the GUI.

        This method updates the current plot in the GUI with the provided
        Matplotlib figure.

        :param fig: The Matplotlib figure to update in the GUI.
        :type fig: matplotlib.figure.Figure
        """
        if self.current_plot:
            self.current_plot.get_tk_widget().forget()

        self.current_plot = FigureCanvasTkAgg(fig, master=self.plot_container)
        self.current_plot.draw()
        self.current_plot.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.update_export_button_state()

        plt.tight_layout()

    def update_export_button_state(self):
        """
        Update the state of the export button.

        This method updates the state of the export button based on the
        presence of the current plot. If there is a current plot, it
        creates and displays the export button. Otherwise, it destroys
        the export button if it exists.
        """
        if self.current_plot:
            if self.export_button:
                self.export_button.destroy()
                self.export_button = tk.Button(self.master, text="Export grapth", command=self.export_current_plot_as_image)
                self.export_button.pack()
        else:
            if self.export_button:
                self.export_button.destroy()

    def plot_histogram_age(self):
        """
        Plot histogram based on age.

        This method generates a histogram plot based on the age column
        of the provided data.

        """
        PlotGenerator.generate_histogram_age(self.data, self)

    def plot_bar_department_salary(self):
        """
        Plot bar chart for department and salary.

        This method generates a bar chart for the distribution of salary
        based on department from the provided data.

        """
        PlotGenerator.generate_bar_department_salary(self.data, self)

    def plot_scatter_experience_salary(self):
        """
        Plot scatter plot for experience and salary.

        This method generates a scatter plot for the relationship between
        experience and salary from the provided data.

        """
        PlotGenerator.generate_scatter_experience_salary(self.data, self)

    def plot_pie_gender(self):
        """
        Plot pie chart for gender distribution.

        This method generates a pie chart for the distribution of gender
        from the provided data.

        """
        PlotGenerator.generate_pie_gender(self.data, self)

    def plot_line_salary_time(self):
        """
        Plot line chart for salary over time.

        This method generates a line chart for the trend of salary over
        time from the provided data.

        """
        PlotGenerator.generate_line_salary_time(self.data, self)

    def plot_bar_department_distribution(self):
        """
        Plot bar chart for department distribution.

        This method generates a bar chart for the distribution of
        departments from the provided data.

        """
        PlotGenerator.generate_bar_department_distribution(self.data, self)

    def show_multiple_subplots(self):
        """
        Show multiple subplots.

        This method generates and displays multiple subplots based on the
        provided data.

        """
        logger.info("Show multiple subplots.")
        if self.info_label:
            self.info_label.pack_forget()

        PlotGenerator.generate_multiple_subplots(self.data, self)

    def export_current_plot_as_image(self):
        """
        Export the current plot as an image.

        This method exports the current plot in the GUI as an image and
        shows a success message.

        """
        if self.current_plot:
            FileExporter.export_plot_as_image(self.current_plot)
            messagebox.showinfo("Success", "The graph was successfully saved as an image.")
            logger.info("Graph saved successfully.")
    logger.info("Visualizer program completed.")
