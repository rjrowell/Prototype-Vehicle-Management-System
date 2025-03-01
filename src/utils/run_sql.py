"""A utility file for executing sql."""
import sqlite3

from .transfrom_properties import transform_properties


def read_sql_file(filepath: str) -> str:
    """Read an sql file from a filepath into a str.

    Args:
        filepath (str): the filepath of the SQL file

    Returns:
        sql_script (str): the str contaning the SQL script
    """
    with open(filepath, 'r') as sql_file:
        sql_script: str = sql_file.read()

    return sql_script


def execute_sql(filename: str):
    """Read sql file then execute it.

    Args:
        filename (str): path to sql file
    """
    sql_script = read_sql_file(filename)

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
    sql_script = read_sql_file(filename)

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
    sql_script = read_sql_file(filepath)

    conn = sqlite3.connect('vehicles.db')
    cursor = conn.cursor()

    # fetch the vehicle type of the vehicle with number plate
    vehicle_type: str = cursor.execute(sql_script, (num_plate,)).fetchone()[0]

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

    sql_script = read_sql_file(filepath)

    conn = sqlite3.connect('vehicles.db')
    cursor = conn.cursor()

    output: list = cursor.execute(sql_script, (num_plate,)).fetchall()

    conn.close()
    return output


def insert_car(properties: list):
    """Insert a new entry into the car table of the DB.

    Args:
        properties (list): The properties of the car to be inserted
    """
    filepath: str = 'src/sql/insert_car.sql'
    sql_script = read_sql_file(filepath)

    conn = sqlite3.connect('vehicles.db')
    cursor = conn.cursor()

    cursor.execute(sql_script, (properties[0], properties[5]))

    conn.commit()
    conn.close()


def insert_van(properties: list):
    """Insert a new entry into the van table of the DB.

    Args:
        properties (list): The properties of the van to be inserted
    """
    filepath: str = 'src/sql/insert_van.sql'
    sql_script = read_sql_file(filepath)

    conn = sqlite3.connect('vehicles.db')
    cursor = conn.cursor()

    cursor.execute(sql_script, (properties[0], properties[5]))

    conn.commit()
    conn.close()


def insert_lorry(properties: list):
    """Insert a new entry into the lorry table of the DB.

    Args:
        properties (list): The properties of the lorry or pickup to be inserted
    """
    filepath: str = 'src/sql/insert_lorry.sql'
    sql_script = read_sql_file(filepath)

    conn = sqlite3.connect('vehicles.db')
    cursor = conn.cursor()

    cursor.execute(sql_script, (properties[0], properties[5], properties[6]))

    conn.commit()
    conn.close()


def insert_vehicle_into_db(properties: list):
    """Take parameters from a Vehicle properties and insert into db.

    Args:
        properties (list): The vehicle properties to be inserted
    """
    vehicle_type: str = properties[2]
    properties = transform_properties(properties)

    sql_script = read_sql_file('src/sql/insert_vehicle.sql')

    conn = sqlite3.connect('vehicles.db')
    cursor = conn.cursor()

    print(sql_script)

    cursor.execute(sql_script, (properties[0], properties[2], properties[1],
                   properties[4], properties[3]))

    conn.commit()
    conn.close()

    # TODO run vehicle sql then run each individual type sql
    if vehicle_type == 'car':
        insert_car(properties)
    elif vehicle_type == 'van':
        insert_van(properties)
    elif vehicle_type == 'lorry' or vehicle_type == 'pickup':
        insert_lorry(properties)
