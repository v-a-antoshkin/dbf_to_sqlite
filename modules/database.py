import os
import pandas as pd
import sqlite3
from dbfread import DBF
from tqdm import tqdm
from modules.csv_error import CSVError  # Assuming ErroCSV class was also translated and renamed to CSVError


class Database:
    """
    A class to manage DBF file processing and database operations.
    
    Attributes:
        dbf_directory (str): The directory where DBF files are stored.
        database_path (str): The path to the SQLite database file.
        files (list): A list of DBF filenames to process.
        errors (list): A list to track errors encountered during processing.
    """

    def __init__(self, dbf_directory, database_path, files):
        """
        Initializes the Database class with directory, database path, and files.

        Parameters:
            dbf_directory (str): The directory where DBF files are stored.
            database_path (str): The path to the SQLite database file.
            files (list): A list of DBF filenames to process.
        """
        self.dbf_directory = dbf_directory + os.sep  # Using os.sep ensures OS compatibility
        self.database_path = database_path
        self.files = files
        self.errors = []

    def save_to_database(self):
        """
        Processes and saves data from DBF files into an SQLite database.
        Records errors encountered during processing.
        """
        for file in tqdm(self.files, desc='Processing DBF files'):
            table_name = file.split('.')[0].lower()
            file_path = self.dbf_directory + file

            if os.path.exists(file_path):
                dbf_table = DBF(file_path)
                df = pd.DataFrame(iter(dbf_table))

                try:
                    connection = sqlite3.connect(self.database_path)
                    df.to_sql(name=table_name, con=connection, if_exists='append', index=False)
                except Exception as e:
                    self.errors.append({'File': file, 'Error': str(e)})
            else:
                print(f'File does not exist: {file}, Table: {table_name}')

        # Assuming CSVError class is responsible for handling and exporting errors to a CSV file
        CSVError(self.errors, self.database_path).generate()