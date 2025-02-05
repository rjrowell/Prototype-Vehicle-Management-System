"""A utility file for executing sql."""
import sqlite3

from all_veichles_window_scripts import all_veichles_build_classes


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


def execute_sql_select(filename: str) -> list:
    """Run an SQL select statement.

    Args:
        filename (str): path to sql file

    Returns:
        output (list): returns the result of the select
    """
    with open(filename, 'r') as sql_file:
        sql_script = sql_file.read()

    conn = sqlite3.connect('veichles.db')
    cursor = conn.cursor()

    output: list = cursor.execute(sql_script).fetchall()
    return output


output = execute_sql_select('src/sql/select_all_veichles.sql')
output = all_veichles_build_classes(output)
for x in output:
    print(x.veichle_type)
