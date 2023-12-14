from matplotlib import pyplot as plt
import pandas as pd

class PlotGenerator:
    """
    A class containing static methods to generate various types of plots.
    """
    @staticmethod
    def generate_histogram_age(data, gui_instance):
        """
        Generate and display a histogram of employee ages.

        Parameters:
        - data (pd.DataFrame): The DataFrame containing employee data.
        - gui_instance: An instance of the DataVisualizerGUI class.

        Returns:
        - None
        """
        fig, ax = plt.subplots()

        # Гістограма віку
        ax.hist(data['age'], bins=10, edgecolor='black', alpha=0.7)
        ax.set_title("Гістограма віку співробітників")
        ax.set_xlabel("Вік")
        ax.set_ylabel("Кількість співробітників")

        # Оновлення відображення графіку в контейнері
        gui_instance.update_plot(fig)

    @staticmethod
    def generate_bar_department_salary(data, gui_instance):
        fig, ax = plt.subplots()

        department_avg_salary = data.groupby('department')['salary'].mean().sort_values(ascending=False)
        department_avg_salary.plot(kind='bar', ax=ax, color='skyblue')

        ax.set_xticklabels(department_avg_salary.index, rotation=45, ha="right")

        ax.set_title("Середня зарплата за підрозділами")
        ax.set_xlabel("Підрозділ")
        ax.set_ylabel("Середня зарплата")

        gui_instance.update_plot(fig)

    @staticmethod
    def generate_scatter_experience_salary(data, gui_instance):
        fig, ax = plt.subplots()

        ax.scatter(data['experience'], data['salary'], color='green', alpha=0.7)
        ax.set_title("Діаграма розсіювання між досвідом та зарплатою")
        ax.set_xlabel("Досвід (роки)")
        ax.set_ylabel("Зарплата")

        gui_instance.update_plot(fig)

    @staticmethod
    def generate_pie_gender(data, gui_instance):
        fig, ax = plt.subplots()

        gender_counts = data['gender'].value_counts()
        gender_counts.plot(kind='pie', autopct='%1.1f%%', colors=['lightcoral', 'lightblue'], ax=ax)
        ax.set_title("Розподіл за статтю")

        gui_instance.update_plot(fig)

    @staticmethod
    def generate_line_salary_time(data, gui_instance):
        fig, ax = plt.subplots()

        data['birth_date'] = pd.to_datetime(data['birth_date'])
        salary_time = data.groupby(data['birth_date'].dt.year)['salary'].mean()
        salary_time.plot(kind='line', marker='o', ax=ax, color='orange')
        ax.set_title("Лінійний графік змін зарплати з часом")
        ax.set_xlabel("Рік")
        ax.set_ylabel("Середня зарплата")

        gui_instance.update_plot(fig)

    @staticmethod
    def generate_bar_department_distribution(data, gui_instance):
        fig, ax = plt.subplots()

        department_distribution = data['department'].value_counts().sort_values(ascending=False)
        department_distribution.plot(kind='bar', ax=ax, color='salmon')

        ax.set_xticklabels(department_distribution.index, rotation=45, ha="right")

        ax.set_title("Стовпчикова діаграма\n(Розподіл за підрозділами)")
        ax.set_xlabel("Підрозділ")
        ax.set_ylabel("Кількість співробітників")

        gui_instance.update_plot(fig)

    @staticmethod
    def generate_multiple_subplots(data, gui_instance):
        """
        Generate and display multiple subplots.

        Parameters:
        - data (pd.DataFrame): The DataFrame containing employee data.
        - gui_instance: An instance of the DataVisualizerGUI class.

        Returns:
        - None
        """
        # Hide the previous Label
        if gui_instance.info_label:
            gui_instance.info_label.pack_forget()
        # Create a subplot grid for multiple subplots
        fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12, 6))

        # For numeric fields. Subplot for histogram
        axes[0, 0].hist(data['age'], bins=10, edgecolor='black', alpha=0.7)
        axes[0, 0].set_title("Гістограма віку співробітників")

        # Subplot for scatter plot (relationship between age and salary)
        axes[0, 1].scatter(data['age'], data['salary'], color='purple', alpha=0.7)
        axes[0, 1].set_title("Діаграма розсіювання\n(Вік та зарплата)")

        # Subplot for bar chart
        department_avg_salary = data.groupby('department')['salary'].mean().sort_values(ascending=False)
        bar_plot = department_avg_salary.plot(kind='bar', ax=axes[0, 2], color='skyblue')
        axes[0, 2].set_title("Стовпчикова діаграма\n(Середня зарплата за підрозділами)")
        # Set the rotation angle for x-axis labels
        bar_plot.set_xticklabels(bar_plot.get_xticklabels(), rotation=45, ha="right")

        # For categorical fields
        # Subplot for pie chart (gender distribution)
        gender_counts = data['gender'].value_counts()
        gender_counts.plot(kind='pie', autopct='%1.1f%%', colors=['lightcoral', 'lightblue'], ax=axes[1, 0])
        axes[1, 0].set_title("Кругова діаграма\n(Розподіл за статтю)")

        # Subplot for bar chart (distribution by departments)
        department_counts = data['department'].value_counts()
        bar_plot = department_counts.plot(kind='bar', ax=axes[1, 1], color='salmon')
        axes[1, 1].set_title("Стовпчикова діаграма\n(Розподіл за підрозділами)")
        # Set the rotation angle for x-axis labels
        bar_plot.set_xticklabels(bar_plot.get_xticklabels(), rotation=45, ha="right")

        # Subplot for line plot (average salary over time)
        data['birth_date'] = pd.to_datetime(data['birth_date'])
        salary_time = data.groupby(data['birth_date'].dt.year)['salary'].mean()
        salary_time.plot(kind='line', marker='o', ax=axes[1, 2], color='orange')
        axes[1, 2].set_title("Лінійний графік\n(Середня зарплата з часом)")

        plt.tight_layout()

        # Update the display of the plot in the container
        gui_instance.update_plot(fig)
