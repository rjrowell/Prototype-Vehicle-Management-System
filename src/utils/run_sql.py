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


def select_type_from_num_plate(num_plate: str) -> str:
    """Select from the database a vehicle with a number plate.

    Args:
        num_plate(str): The number plate to attempt to retrieve from DB

    Returns:
        vehicle_type (str): The type of selected vehicle
    """
    filepath: str = 'src/sql/select_vehicle_type_from_numplate.sql'
    with open(filepath, 'r') as sql_file:
        sql_script: str = sql_file.read()
    # Programmatically insert number plate var into sql script
    sql_script: str = sql_script.replace('?NUM_PLATE?', num_plate)

    conn = sqlite3.connect('vehicles.db')
    cursor = conn.cursor()

    # fetch the vehicle type of the vehicle with number plate
    vehicle_type: str = cursor.execute(sql_script).fetchone()[0]

    conn.close()
    return vehicle_type


def select_based_on_type(vehicle_type: str, num_plate: str) -> list:
    """Select from database a specific vehicle based on its type.

    Args:
        vehicle_type (str): The type of vehicle we are selecting.
        num_plate (str): The number plate of the vehicle we are selecting.

    Returns:
        list: The output of the SQL select statement.
    """
    if vehicle_type == 'car':
        filepath: str = 'src/sql/select_car.sql'
    elif vehicle_type == 'van':
        filepath: str = 'src/sql/select_van.sql'
    elif vehicle_type == 'lorry' or vehicle_type == 'pickup':
        filepath: str = 'src/sql/select_lorry.sql'

    with open(filepath, 'r') as sql_file:
        sql_script: str = sql_file.read()
    # Programmatically insert number plate var into sql script
    sql_script: str = sql_script.replace('?NUM_PLATE?', num_plate)

    conn = sqlite3.connect('vehicles.db')
    cursor = conn.cursor()

    output: list = cursor.execute(sql_script).fetchall()

    conn.close()
    return output
