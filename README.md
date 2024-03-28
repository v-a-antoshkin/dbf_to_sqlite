# DBF to SQLite Conversion Tool

This Python-based tool automates the process of converting data from DBF (DataBase File) formats to a SQLite database. It's designed to help users easily transfer and query data stored in DBF files by utilizing the efficient and widely-supported SQLite database system.

## Features :sparkles:

- **Automated Discovery**: Automatically identifies all DBF files within a specified directory.
- **Efficient Conversion**: Seamlessly converts data from DBF files into a SQLite database, preserving the integrity and structure of the original data.
- **Error Logging**: Captures and logs any errors that occur during the conversion process for troubleshooting and audit purposes.

## Prerequisites :rocket:

Before you begin, ensure you have the following requirements installed on your system:

- Python 3.6 or newer
- Required Python libraries: `pandas`, `sqlite3`, and `tqdm`

## Installation :zap:

1. **Clone the Repository** :floppy_disk:

   Start by cloning this repository to your local machine using the following command:

    ```bash
    git clone https://example.com/your-repo.git
    ```

2. **Install Dependencies** :package:

   Install the required Python libraries using the following command:

    ```bash
    pip install -r requirements.txt
    ```

## Usage :computer:

To convert all DBF files in the specified directory, run the following command:

```bash
python main.py
```

## License

Este projeto é licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) no repositório para mais detalhes.
