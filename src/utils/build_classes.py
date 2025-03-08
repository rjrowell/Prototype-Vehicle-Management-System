"""Code to build the vehicle classes used by some GUI windows."""
from .run_sql import (execute_sql_select, select_based_on_type,
                      select_type_from_num_plate)
from .vehicle_classes import Car, LorryOrPickup, Van

vehicle_mapping: dict = {
    'car': Car,
    'van': Van,
    'lorry': LorryOrPickup,
    'pickup': LorryOrPickup,
}

check = ('lorry', 'pickup')


def build_classes(filepath: str, window: str):
    """Build the classes for some GUI windows.

    Args:
        filepath(str): the path to sql file
        window(str): name of the window

    Returns:
        output(list): a list of new classes for the window

    """
    # We pass in the filepath, but on select occasions we pass in
    # information to be used directly, this try catch detects such scenarios
    try:
        sql_output: list = execute_sql_select(filepath)
    except FileNotFoundError:
        sql_output: str = filepath

    if window == 'all_vehicles':
        output: list = assign_all_vehicles_classes(sql_output)
    elif window == 'tax_due':
        output: list = assign_tax_due_classes(sql_output)
    elif window == 'service_due':
        output: list = assign_service_due_classes(sql_output)
    elif window == 'num_plate':
        output: list = assign_num_plate_classes(sql_output)

    return output


def assign_all_vehicles_classes(sql_result: list) -> list:
    """Assign the classes for the 'list all vehicles window.

    Args:
        sql_result(list): The result of an sql select query

    Returns:
        output(list): list of classes with values assigned

    """
    output: list = []

    for row in sql_result:
        vehicle_type = row[1]
        if vehicle_type in vehicle_mapping:
            vehicle_class = vehicle_mapping.get(vehicle_type)
            if vehicle_type in check:
                output.append(vehicle_class(
                    row[0],
                    row[2],
                    vehicle_type,
                    None,
                    None,
                    None,
                    None,
                ),
                )
            else:
                output.append(vehicle_class(
                    row[0],
                    row[2],
                    vehicle_type,
                    None,
                    None,
                    None,
                ),
                )
    return output


def assign_tax_due_classes(sql_result: list) -> list:
    """Assign values to classes for 'vehicles by tax due' window.

    Args:
        sql_result(list): The result of an SQL select query

    Returns:
        output(list): list of classes with assigned values
    """
    output: list = []

    for row in sql_result:
        vehicle_type = row[1]
        vehicle_args = [row[0], row[2], row[1], None, None]

        if vehicle_type in check:
            vehicle_args.append(None)
            vehicle_args.append(row[3])
        else:
            vehicle_args.append(row[3])
        output.append(vehicle_mapping[vehicle_type](*vehicle_args))

    return output


def assign_service_due_classes(sql_result: list) -> list:
    """Assign values to classes for 'vehicles by service due' window.

    Args:
        sql_result(list): The result of an SQL select query

    Returns:
        output(list): list of classes with assigned values

    """
    output: list = []

    for row in sql_result:
        vehicle_type = row[1]
        vehicle_args = [row[0], row[2], row[1], None]

        if vehicle_type in check:
            vehicle_args.append(None)
            vehicle_args.append(row[3])
            vehicle_args.append(None)
        else:
            vehicle_args.append(row[3])
            vehicle_args.append(None)
        output.append(vehicle_mapping[vehicle_type](*vehicle_args))

    return output


def assign_num_plate_classes(num_plate: str) -> list:
    """Assign values to classes for 'vehicles by number plate' window.

    Args:
        num_plate(str): the number plate of the vehicle

    Returns:
         output(list): list of classes with assigned values

    """
    output: list = []

    vehicle_type = select_type_from_num_plate(num_plate)
    sql_result: list = select_based_on_type(vehicle_type, num_plate)

    for row in sql_result:
        vehicle_args = [num_plate, row[0], vehicle_type, row[3]]

        if vehicle_type in check:
            vehicle_args.append(row[4])
            vehicle_args.append(row[2])
            vehicle_args.append(row[1])
        else:
            vehicle_args.append(row[2])
            vehicle_args.append(row[1])
        output.append(vehicle_mapping[vehicle_type](*vehicle_args))

    return output
