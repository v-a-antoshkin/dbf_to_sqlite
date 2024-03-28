import os


class MapDBF:
    """
    A class for mapping and listing .dbf files within a specified directory.

    Attributes:
        dbf_directory (str): The directory to search for .dbf files.
    """

    def __init__(self, dbf_directory):
        """
        Initializes the MapDBF class with a directory to search for .dbf files.

        Parameters:
            dbf_directory (str): The directory to search for .dbf files.
        """
        self.dbf_directory = dbf_directory

    def list_files(self):
        """
        Lists all .dbf files found in the specified directory.

        Returns:
            list: A list of .dbf filenames found in the specified directory.
        """
        files = [
            file
            for file in os.listdir(self.dbf_directory)
            if file.lower().endswith(".dbf")
        ]
        return files
