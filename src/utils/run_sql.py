"""A utility file for executing sql."""
import sqlite3

from .do_nothing import do_nothing
from .transfrom_properties import transform_colour, transform_properties

db_name = 'vehicles.db'

lp = ('lorry', 'pickup')

cab_type_string = 'cab_type'


def get_conn():
    """Get connection to the databse.

    Returns:
        connection: the database connection
    """
    return sqlite3.connect(db_name)


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

    conn = get_conn()
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

    conn = get_conn()
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

    conn = get_conn()
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
    elif vehicle_type in lp:
        filepath: str = 'src/sql/select_lorry.sql'

    sql_script = read_sql_file(filepath)

    conn = get_conn()
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

    conn = get_conn()
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

    conn = get_conn()
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

    conn = get_conn()
    cursor = conn.cursor()

    properties_dict = {
        'num_plate': properties[0],
        'cargo': properties[5],
        cab_type_string: properties[6],
    }

    cursor.execute(sql_script, (
        properties_dict['num_plate'],
        properties_dict['cargo'],
        properties_dict[cab_type_string],
        ))

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

    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute(
        sql_script,
        (
            properties[0],
            properties[2],
            properties[1],
            properties[4],
            properties[3],
        ),
    )

    conn.commit()
    conn.close()

    if vehicle_type == 'car':
        insert_car(properties)
    elif vehicle_type == 'van':
        insert_van(properties)
    elif vehicle_type in lp:
        insert_lorry(properties)


def update_specific_type(
    changed_values: dict,
    vehicle_type: str,
    number_plate: str,
):
    """Update a specific type of vehicle in the database.

    Args:
        changed_values (dict): The dictionary with the values to upate in them
        vehicle_type (str): The vehicle type of the vehicle to update
        number_plate (str): The number plate of the vehicle be updated
    """
    value_string: str = ''

    if vehicle_type == 'car':
        sql_script = read_sql_file('src/sql/update_car.sql')
        extra = 'number_of_seats'
    elif vehicle_type == 'van':
        sql_script = read_sql_file('src/sql/update_van.sql')
        extra = 'cargo_capacity'
    else:
        sql_script = read_sql_file('src/sql/update_lorry.sql')
        extra = 'cargo_capacity'

    # re-size dictionary
    changed_values = {
        extra: changed_values['extra1'],
        cab_type_string: changed_values[cab_type_string],
    }

    for column, element in changed_values.items():
        if element:
            value_string = '{0}{1}'.format(value_string, column)
            value_string = '{0} = "{1}", '.format(value_string, element)

    value_string = value_string[:-2]  # remove trailing comma from end of str

    sql_script = sql_script.replace('(value_string)', value_string)

    if value_string:
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql_script,
            (
                number_plate,
            ),
        )
        conn.commit()
        conn.close()


def update_vehicle(changed_values: dict, vehicle_type: str, number_plate: str):
    """Update the vehicle's details based on values in dictionary.

    Args:
        changed_values (dict): The dictionary with the values to upate in them
        vehicle_type (str): The vehicle type of the vehicle to update
        number_plate (str): The number plate of the vehicle be updated
    """
    value_string: str = ''
    colour_string = changed_values['colour_id']
    check_column = ('extra1', cab_type_string)
    # If colour is not None, transform it to an integer
    if colour_string:
        changed_values['colour_id'] = transform_colour(colour_string)

    for column, element in changed_values.items():
        # If the value is not None, add it to the string
        if column in check_column:
            do_nothing()
        elif element:
            value_string = '{0}{1}'.format(value_string, column)
            value_string = '{0} = "{1}", '.format(value_string, element)

    value_string = value_string[:-2]  # remove trailing comma from end of str

    # TODO: execute the update vehicle sql and set update car,van,lorry,pickup
    sql_script = read_sql_file('src/sql/update_vehicle.sql')
    sql_script = sql_script.replace('(value_string)', value_string)

    if value_string:
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql_script,
            (
                number_plate,
            ),
        )
        conn.commit()
        conn.close()

    update_specific_type(changed_values, vehicle_type, number_plate)
