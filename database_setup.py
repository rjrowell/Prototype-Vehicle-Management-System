"""Script that setups the prototype database."""
import sqlite3


def main():
    """Drop tables then creates the new prototype db."""
    drop_tables()
    create_tables()


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


def drop_tables():
    """Execute drop_tables.sql."""
    execute_sql('drop_tables.sql')


def create_tables():
    """Execute create_tables.sql."""
    execute_sql('create_tables.sql')


if __name__ == '__main__':
    main()
