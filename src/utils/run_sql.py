"""A utility file for executing sql."""
import sqlite3


def execute_sql(filename: str):
    """Read sql file then execute it.

    Args:
        filename (str): path to sql file
    """
    with open(filename, 'r') as sql_file:
        sql_script = sql_file.read()

    conn = sqlite3.connect('vehicles.db')
    cursor = conn.cursor()
    cursor.executescript(sql_script)
    conn.close()


def execute_sql_select(filename: str) -> list:
    """Run an SQL select statement.

    Args:
        filename (str): path to sql file

    Returns:
        output (list): returns the result of the select
    """
    with open(filename, 'r') as sql_file:
        sql_script = sql_file.read()

    conn = sqlite3.connect('vehicles.db')
    cursor = conn.cursor()

    output: list = cursor.execute(sql_script).fetchall()

    conn.close()
    return output


def select_from_num_plate(num_plate: str):
    """Select from the database a vehicle with a number plate.

    Args:
        num_plate(str): The number plate to attempt to retrieve from DB
    """
    filepath: str = 'src/sql/select_vehicle_type_from_numplate.sql'
    with open(filepath, 'r') as sql_file:
        sql_script: str = sql_file.read()
    # Programmatically insert number plate var into sql script
    sql_script: str = sql_script.replace('?NUM_PLATE?', num_plate)

    conn = sqlite3.connect('vehicles.db')
    cursor = conn.cursor()

    print(sql_script)
    # fetch the vehicle type of the vehicle with number plate
    vehicle_type: str = cursor.execute(sql_script).fetchone()[0]
    print(vehicle_type)

    conn.close()
