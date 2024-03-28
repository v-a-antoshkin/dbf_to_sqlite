# Imports
import logging
from config import dbf_directory, database_path
from modules.map_dbf import MapDBF
from modules.database import Database

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main() -> None:
    """
    Main function to process DBF files and save their contents to a SQLite database.
    """
    logging.info('Starting processing: %s', database_path)

    try:
        # Initialize the mapper to list DBF files
        dbf_mapper = MapDBF(dbf_directory)
        files = dbf_mapper.list_files()

        # Process and save the DBF files to the database
        db_processor = Database(dbf_directory, database_path, files)
        db_processor.save_to_database()

        logging.info('Processing completed successfully.')
    except Exception as e:
        # Log any exceptions that occur during the processing
        logging.error('An error occurred during processing: %s', e)
        raise  # Optionally re-raise the exception if you want it to propagate

if __name__ == '__main__':
    main()