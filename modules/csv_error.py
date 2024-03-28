import pandas as pd
import sqlite3


class CSVError:
    """
    A class to manage and log errors to a SQLite database as a CSV format table.
    
    Attributes:
        errors (list): A list of error dictionaries to log.
        database_path (str): The path to the SQLite database file where the errors will be logged.
    """

    def __init__(self, errors, database_path):
        """
        Initializes the CSVError class with a list of errors and the database path.

        Parameters:
            errors (list): A list of error dictionaries to log.
            database_path (str): The path to the SQLite database file where the errors will be logged.
        """
        self.errors = errors
        self.database_path = database_path

    def generate(self):
        """
        Generates a log table in the SQLite database and logs the errors.
        The table is named 'log_errors_DBF_SQLite' and will append errors if it already exists.
        """
        errors_df = pd.DataFrame(self.errors)

        table_name = 'log_errors_DBF_SQLite'
        connection = sqlite3.connect(self.database_path)
        errors_df.to_sql(name=table_name, con=connection, if_exists='append', index=False)