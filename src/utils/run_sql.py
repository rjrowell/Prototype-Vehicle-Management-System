"""A utility file for executing sql."""
import sqlite3


def execute_sql(filename: str):
    """Read sql file then execute it.

    Args:
        filename (str): path to sql file
    """
    with open(filename, 'r') as sql_file:
        sql_script = sql_file.read()

    conn = sqlite3.connect('veichles.db')
    cursor = conn.cursor()
    cursor.executescript(sql_script)