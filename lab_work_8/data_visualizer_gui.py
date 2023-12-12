import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog
import pandas as pd
from PIL import Image

class DataVisualizerGUI:
    def __init__(self, master, csv_file):
        # Initialize the GUI with the given master window and CSV file
        self.master = master
        self.master.title("Data Visualizer GUI")

        # Read data from the CSV file and store column information
        self.data = pd.read_csv(csv_file)
        self.columns = list(self.data.columns)
        self.info_label = None
        self.current_plot = None
        self.export_button = None

        # ComboBox for selecting the type of plot
        self.plot_types = ['Histogram (Age)', 'Bar (Department & Salary)', 'Scatter (Experience & Salary)',
                           'Pie (Gender)', 'Line (Salary & Time)', 'Bar (Department Distribution)']

        # ComboBox for selecting the type of plot
        self.plot_type_combobox = ttk.Combobox(self.master, values=self.plot_types)

        # Button to display the selected plot
        show_plot_button = tk.Button(self.master, text="Show Plot", command=self.show_selected_plot)

        # ComboBox for selecting the column
        self.column_combobox = ttk.Combobox(self.master, values=self.columns)

        # Button to show extreme values for the selected column
        show_extremes_button = tk.Button(self.master, text="Show Extreme Values", command=self.show_extremes)

        # Add a container for displaying the plot
        self.plot_container = tk.Frame(self.master)

        # Button to display multiple subplots
        show_multiple_subplots_button = tk.Button(self.master, text="Show Multiple Subplots", command=self.show_multiple_subplots)

        # Arrange elements on the window
        self.plot_type_combobox.pack(pady=5)
        show_plot_button.pack(pady=5)
        self.column_combobox.pack(pady=5)
        show_extremes_button.pack(pady=5)
        show_multiple_subplots_button.pack(pady=5)
        self.plot_container.pack(pady=5)

        # Button to export the current plot
        self.export_button = tk.Button(self.master, text="Export Plot", command=self.export_current_plot_as_image)

    def show_extremes(self):
        # Display extreme values for the selected column
        selected_column = self.column_combobox.get()

        if not selected_column:
            messagebox.showinfo("Error", "Please select a column for analysis.")  # Display message about selecting a column
            return

        if self.info_label:
            self.info_label.pack_forget()  # Hide the previous Label

        for widget in self.plot_container.winfo_children():
            widget.destroy()  # Remove the previous plot

        if self.data[selected_column].dtype == 'object':
            if selected_column == 'birth_date':
                # For the text field 'birth_date'
                min_date = self.data[selected_column].min()
                max_date = self.data[selected_column].max()
                extremes = pd.Series({
                    'Minimum Date': min_date,
                    'Maximum Date': max_date
                })
                # Display information about the text column
                info_text = f"Information about the column {selected_column}:\n"
                info_text += f"Minimum Date: {min_date}\n"
                info_text += f"Maximum Date: {max_date}"
                self.show_info_in_gui(info_text)  # Display information in the GUI
                self.plot_extremes_dates(extremes)  # Display the plot
            else:
                # For other text fields
                unique_values = len(self.data[selected_column].unique())
                most_common_value = self.data[selected_column].mode().iloc[0]
                most_common_count = self.data[selected_column].value_counts().iloc[0]
                extremes = pd.Series({
                    'Unique Values': unique_values,
                    'Most Common Value': f"{most_common_value} (Count: {most_common_count})"
                })
                # Display information about the text column
                info_text = f"Information about the column {selected_column}:\n"
                info_text += f"Number of unique values: {unique_values}\n"
                info_text += f"Most common value: {most_common_value} (Count: {most_common_count})"
                self.show_info_in_gui(info_text)  # Display information in the GUI
        else:
            extremes = self.data[selected_column].describe()  # For numeric fields
            self.plot_extremes_numeric(extremes)  # Display the plot

    def show_selected_plot(self):
        # Display the selected type of plot
        selected_plot_type = self.plot_type_combobox.get()

        if not selected_plot_type:
            # Display message about selecting the plot type and column
            messagebox.showinfo("Error", "Please select a plot type.")
            return

        if self.info_label:
            self.info_label.pack_forget()  # Hide the previous Label

        for widget in self.plot_container.winfo_children():
            widget.destroy()  # Remove the previous plot

        # Determine the selected type of plot and call the corresponding method
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
            self.plot_bar_department_distribution()  # Call the new method

    def show_info_in_gui(self, info_text):
        # Remove the previous plot and export button
        for widget in self.plot_container.winfo_children():
            widget.destroy()

        if self.export_button:
            self.export_button.destroy()  # Remove the previous button

        # Create a Label widget to display information
        self.info_label = tk.Label(self.plot_container, text=info_text)
        self.info_label.pack()

    def plot_extremes_dates(self, extremes):
        fig, ax = plt.subplots()  # Represents an object that creates a figure and a two-dimensional array of objects representing subplots

        # For the text field 'birth_date'
        min_date = pd.to_datetime(extremes['Minimum Date'])
        max_date = pd.to_datetime(extremes['Maximum Date'])

        ax.bar(['Minimum Date', 'Maximum Date'], [min_date, max_date])
        ax.set_title("Extreme Values (Text Field)")
        ax.set_ylabel("Date")
        ax.set_xlabel("Attribute")

        # Update the display of the plot in the container
        self.update_plot(fig)

    def plot_extremes_numeric(self, extremes):
        fig, ax = plt.subplots()

        # For numeric fields
        extremes.plot(kind='bar', ax=ax)
        ax.set_title("Extreme Values (Numeric Field)")
        ax.set_ylabel("Value")
        ax.set_xlabel("Attribute")

        # Update the display of the plot in the container
        self.update_plot(fig)

    def update_plot(self, fig):
        # Function to update the display of the plot in the container
        if self.current_plot:
            self.current_plot.get_tk_widget().forget()

        self.current_plot = FigureCanvasTkAgg(fig, master=self.plot_container)
        self.current_plot.draw()
        self.current_plot.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Update the export plot button state
        self.update_export_button_state()

        # Use tight_layout for automatic element alignment
        plt.tight_layout()

    def update_export_button_state(self):
        # Function to update the state of the export button
        if self.current_plot:
            if self.export_button:
                self.export_button.destroy()  # Remove the previous button
            # Create a button for exporting the plot
            self.export_button = tk.Button(self.master, text="Export Plot", command=self.export_current_plot_as_image)
            self.export_button.pack()
        else:
            # If no plot is selected or visible, the button is not displayed
            if self.export_button:
                self.export_button.destroy()  # Remove the previous button

    def plot_histogram_age(self):
        fig, ax = plt.subplots()

        # Histogram of age
        ax.hist(self.data['age'], bins=10, edgecolor='black', alpha=0.7)
        ax.set_title("Histogram of Employee Ages")
        ax.set_xlabel("Age")
        ax.set_ylabel("Number of Employees")

        # Update the display of the plot in the container
        self.update_plot(fig)

    def plot_bar_department_salary(self):
        fig, ax = plt.subplots()

        # Bar chart of departments and average salary
        department_avg_salary = self.data.groupby('department')['salary'].mean().sort_values(ascending=False)
        department_avg_salary.plot(kind='bar', ax=ax, color='skyblue')

        # Set custom labels for the x-axis
        ax.set_xticklabels(department_avg_salary.index, rotation=45, ha="right")

        ax.set_title("Average Salary by Departments")
        ax.set_xlabel("Department")
        ax.set_ylabel("Average Salary")

        # Update the display of the plot in the container
        self.update_plot(fig)

    def plot_scatter_experience_salary(self):
        fig, ax = plt.subplots()

        # Scatter plot of experience and salary
        ax.scatter(self.data['experience'], self.data['salary'], color='green', alpha=0.7)
        ax.set_title("Scatter Plot of Experience and Salary")
        ax.set_xlabel("Experience (years)")
        ax.set_ylabel("Salary")

        # Update the display of the plot in the container
        self.update_plot(fig)

    def plot_pie_gender(self):
        fig, ax = plt.subplots()

        # Pie chart for gender distribution
        gender_counts = self.data['gender'].value_counts()
        gender_counts.plot(kind='pie', autopct='%1.1f%%', colors=['lightcoral', 'lightblue'], ax=ax)
        ax.set_title("Gender Distribution")

        # Update the display of the plot in the container
        self.update_plot(fig)

    def plot_line_salary_time(self):
        fig, ax = plt.subplots()

        # Line plot of salary changes over time
        self.data['birth_date'] = pd.to_datetime(self.data['birth_date'])
        salary_time = self.data.groupby(self.data['birth_date'].dt.year)['salary'].mean()
        salary_time.plot(kind='line', marker='o', ax=ax, color='orange')
        ax.set_title("Line Plot of Salary Changes Over Time")
        ax.set_xlabel("Year")
        ax.set_ylabel("Average Salary")

        # Update the display of the plot in the container
        self.update_plot(fig)

    def plot_bar_department_distribution(self):
        fig, ax = plt.subplots()

        # Bar chart of distribution by departments
        department_distribution = self.data['department'].value_counts().sort_values(ascending=False)
        department_distribution.plot(kind='bar', ax=ax, color='salmon')

        # Set custom labels for the x-axis
        ax.set_xticklabels(department_distribution.index, rotation=45, ha="right")

        ax.set_title("Bar Chart\n(Distribution by Departments)")
        ax.set_xlabel("Department")
        ax.set_ylabel("Number of Employees")

        # Update the display of the plot in the container
        self.update_plot(fig)

    def show_multiple_subplots(self):
        # Hide the previous Label
        if self.info_label:
            self.info_label.pack_forget()

        # Create a subplot grid for multiple subplots
        fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12, 6))

        # For numeric fields. Subplot for histogram
        axes[0, 0].hist(self.data['age'], bins=10, edgecolor='black', alpha=0.7)
        axes[0, 0].set_title("Histogram of Employee Ages")

        # Subplot for scatter plot (relationship between age and salary)
        axes[0, 1].scatter(self.data['age'], self.data['salary'], color='purple', alpha=0.7)
        axes[0, 1].set_title("Scatter Plot\n(Age and Salary)")

        # Subplot for bar chart
        department_avg_salary = self.data.groupby('department')['salary'].mean().sort_values(ascending=False)
        bar_plot = department_avg_salary.plot(kind='bar', ax=axes[0, 2], color='skyblue')
        axes[0, 2].set_title("Bar Chart\n(Average Salary by Departments)")
        # Set the rotation angle for x-axis labels
        bar_plot.set_xticklabels(bar_plot.get_xticklabels(), rotation=45, ha="right")

        # For categorical fields
        # Subplot for pie chart (gender distribution)
        gender_counts = self.data['gender'].value_counts()
        gender_counts.plot(kind='pie', autopct='%1.1f%%', colors=['lightcoral', 'lightblue'], ax=axes[1, 0])
        axes[1, 0].set_title("Pie Chart\n(Gender Distribution)")

        # Subplot for bar chart (distribution by departments)
        department_counts = self.data['department'].value_counts()
        bar_plot = department_counts.plot(kind='bar', ax=axes[1, 1], color='salmon')
        axes[1, 1].set_title("Bar Chart\n(Distribution by Departments)")
        # Set the rotation angle for x-axis labels
        bar_plot.set_xticklabels(bar_plot.get_xticklabels(), rotation=45, ha="right")

        # Subplot for line plot (average salary over time)
        self.data['birth_date'] = pd.to_datetime(self.data['birth_date'])
        salary_time = self.data.groupby(self.data['birth_date'].dt.year)['salary'].mean()
        salary_time.plot(kind='line', marker='o', ax=axes[1, 2], color='orange')
        axes[1, 2].set_title("Line Plot\n(Average Salary Over Time)")

        plt.tight_layout()

        # Update the display of the plot in the container
        self.update_plot(fig)

    def export_current_plot_as_image(self):
        # Function to export the current plot as an image
        # Choose a path for saving
        if self.current_plot:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

        if file_path:
            # Save the current plot as an image
            self.current_plot.figure.savefig(file_path)
            messagebox.showinfo("Success", "Plot successfully saved as an image.")