# Convert Access Database to SQLite

This program aims to convert a Microsoft Access database to a SQLite database using Python.

## Requirements
- Python 3.x
- Python libraries: `pandas`, `pyodbc`, `sqlalchemy`

## Installation
1. Install the required Python libraries using a package manager or the following command:
    ```bash
    pip install pandas pyodbc sqlalchemy
    ```

## Usage
1. Download the Access database file (.mdb or .accdb).
2. Edit the `access_path` variable in the code to point to the appropriate Access database file path.
3. Specify a path for the SQLite database file you want to create by editing the `sqlite_path` variable.
4. Run the code, and the Access database will be converted to a SQLite database.

## Function `convert_mdb_to_sqlite`
This function converts the Access database to SQLite.

## Variables
- `access_path`: Path to the Access database file (.mdb or .accdb).
- `sqlite_path`: Path to the SQLite database file to be created.

## Notes
- Ensure you have the SQLite database engine (`sqlite3.dll`) available in your operating system.
- Make sure you have read and write permissions in the specified path for the SQLite database file.
