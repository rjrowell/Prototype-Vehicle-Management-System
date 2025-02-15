"""Scripts that are used to generate different GUI windows."""
from .vehicle_classes import Car, Van, LorryOrPickup
from .run_sql import execute_sql_select, select_type_from_num_plate, select_based_on_type
import tkinter as tk


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


def get_text_to_display(text_object: tk.Text, vehicles_list: list):
    """Insert rows of veichle information into TK.Text object.

    Args:
        text_object(tkinter.Text): The original text object
        vehicles_list(list): list of veichles to be inserted into text

    Returns:
        text_object(tkinter.Text): The modified text object
    """
    if not vehicles_list:
        text_object.insert(tk.END, 'No vehicles found.\n')
    else:
        for i in vehicles_list:
            text_object.insert(tk.END, get_text_by_vehicle(i) + '\n')

    return text_object


def assign_all_vehicles_classes(sql_result: list) -> list:
    """Assign the classes for the 'list all vehicles window.

    Args:
        sql_result(list): The result of an sql select query
    
    Returns:
        output(list): list of classes with values assigned
    """
    output: list = []
    for row in sql_result:
        if row[1] == 'car':
            new_car = Car(row[0], row[2], row[1], None, None, None)
            output.append(new_car)
        elif row[1] == 'van':
            new_van = Van(row[0], row[2], row[1], None, None, None)
            output.append(new_van)
        elif row[1] == 'lorry' or row[1] == 'pickup':
            new_lorry = LorryOrPickup(row[0], row[2], row[1], None, None, None,
                                      None)
            output.append(new_lorry)
    return output


def get_text_by_vehicle(vehicle: object) -> str:
    """Given a vehicle, programmaticly generate its display text.

    Based on it's type and what variable it has assigned.

    Args:
        vehicle(object): The vehicle class to generate text from

    Returns:
        output(str): The generated text
    """
    output: str = vehicle.number_plate + ': ' + vehicle.colour + ' '
    output = output + vehicle.vehicle_type + ' '

    if vehicle.vehicle_type == 'car':
        if vehicle.num_of_seats is not None:
            output = output + ', ' + vehicle.num_of_seats + ' seater '
    elif vehicle.vehicle_type == 'van':
        if vehicle.cargo_capacity is not None:
            output = output + ', ' + vehicle.cargo_capacity
            output = output + 'l cargo capacity '
    elif vehicle.vehicle_type == 'lorry' or vehicle.vehicle_type == 'pickup':
        if vehicle.cargo_capacity is not None:
            output = output + ', ' + vehicle.cargo_capacity
            output = output + 'l cargo capacity '

        if vehicle.cab_type is not None:
            output = output + ', ' + vehicle.cab_type + ' cab'

    if vehicle.tax_due_date is not None:
        output = output + ',tax due: ' + vehicle.tax_due_date + ' '

    if vehicle.service_due_date is not None:
        output = output + ',service due: ' + vehicle.service_due_date + ' '

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
        if row[1] == 'car':
            new_car = Car(row[0], row[2], row[1], None, None, row[3])
            output.append(new_car)
        elif row[1] == 'van':
            new_van = Van(row[0], row[2], row[1], None, None, row[3])
            output.append(new_van)
        elif row[1] == 'lorry' or row[1] == 'pickup':
            new_lorry = LorryOrPickup(row[0], row[2], row[1], None, None, None,
                                      row[3])
            output.append(new_lorry)
    return output


def assign_service_due_classes(sql_result: list) -> list:
    """Assign values to classes for 'vehicles by tax due' window.

    Args:
        sql_result(list): The result of an SQL select query

    Returns:
        output(list): list of classes with assigned values
    """
    output: list = []
    for row in sql_result:
        if row[1] == 'car':
            new_car = Car(row[0], row[2], row[1], None, row[3], None)
            output.append(new_car)
        elif row[1] == 'van':
            new_van = Van(row[0], row[2], row[1], None, row[3], None)
            output.append(new_van)
        elif row[1] == 'lorry' or row[1] == 'pickup':
            new_lorry = LorryOrPickup(row[0], row[2], row[1], None, None,
                                      row[3],
                                      None)
            output.append(new_lorry)
    return output


def assign_num_plate_classes(num_plate: str) -> object:
    vehicle_type = select_type_from_num_plate(num_plate)
    sql_result: list = select_based_on_type(vehicle_type, num_plate)

    output: list = []
    for row in sql_result:
        if vehicle_type == 'car':
            new_car = Car(num_plate, row[0], vehicle_type, row[3], row[2],
                          row[1])
            output.append(new_car)
        elif vehicle_type == 'van':
            new_van = Van(row[0], row[2], row[1], None, row[3], None)
            output.append(new_van)
        elif vehicle_type == 'lorry' or vehicle_type == 'pickup':
            new_lorry = LorryOrPickup(row[0], row[2], row[1], None, None,
                                      row[3],
                                      None)
            output.append(new_lorry)
    return output
