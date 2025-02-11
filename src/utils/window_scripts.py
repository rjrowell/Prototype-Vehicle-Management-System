"""Scripts that are used to generate different GUI windows."""
from .vehicle_classes import Car, Van, LorryOrPickup
from .run_sql import execute_sql_select
import tkinter as tk


def build_classes(filepath: str, window: str):
    """Build the classes 'list all vehicles' window.

    Args:
        filepath(str): the path to sql file
        window(str): name of the window

    Returns:
        output(list): a list of new classes for the window
    """
    sql_output: list = execute_sql_select(filepath)

    if window == 'all_vehicles':
        output: list = assign_all_vehicles_classes(sql_output)
    elif window == 'tax_due':
        output: list = assign_tax_due_classes(sql_output)

    return output


def get_text_to_display(text_object: tk.Text, vehicles_list: list):
    """Insert rows of veichle information into TK.Text object.

    Args:
        text_object(tkinter.Text): The original text object
        vehicles_list(list): list of veichles to be inserted into text

    Returns:
        text_object(tkinter.Text): The modified text object
    """
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
