import pandas as pd
import pyodbc
from sqlalchemy import create_engine

def convert_mdb_to_sqlite(access_path, sqlite_path):
    conn_str = (
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
        rf"DBQ={access_path};"
    )
    conn = pyodbc.connect(conn_str)
    
    tables = [table_info.table_name for table_info in conn.cursor().tables() if can_read_table(conn, table_info.table_name) and not is_system_table(table_info.table_name)]

    for table in tables:
        sql_query = f"SELECT * FROM [{table}]"
        df = pd.read_sql_query(sql_query, conn)
        
        engine = create_engine(f'sqlite:///{sqlite_path}')
        df.to_sql(table, engine, index=False, if_exists='replace')

    conn.close()

def can_read_table(conn, table_name):
    try:
        conn.cursor().execute(f"SELECT TOP 1 * FROM [{table_name}]")
        return True
    except pyodbc.Error:
        return False

def is_system_table(table_name):
    return table_name.lower().startswith('msys')

access_path = r'x:\x\x\x.accdb'
sqlite_path = 'x.sqlite'
convert_mdb_to_sqlite(access_path, sqlite_path)
