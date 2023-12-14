import pandas as pd

class DataLoader:
    """
    A utility class for loading data from CSV files using pandas.

    Methods:
    --------
    load_csv(file_path):
        Load data from a CSV file and return a pandas DataFrame.

    """
    @staticmethod
    def load_csv(file_path):
        """
        Load data from a CSV file and return a pandas DataFrame.

        Parameters:
        -----------
        file_path (str): The path to the CSV file.

        Returns:
        --------
        pd.DataFrame: The loaded data.
        """
        return pd.read_csv(file_path)
