"""Scripts that are used by the 'display all vehicles' window."""
from .vehicle_classes import Car, Van, LorryOrPickup
from .run_sql import execute_sql_select
import tkinter as tk


def all_vehicles_build_classes():
    """Build the classes 'list all vehicles' window.

    Returns:
        output(list): a list of new classes for the window
    """
    output: list = []
    sql_output = execute_sql_select('src/sql/select_all_vehicles.sql')
    for row in sql_output:
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


def get_text_to_display(text_object: tk.Text, vehicles_list: list):
    """Insert rows of veichle information into TK.Text object.

    Args:
        text_object(tkinter.Text): The original text object
        vehicles_list(list): list of veichles to be inserted into text

    Returns:
        text_object(tkinter.Text): The modified text object
    """
    for i in vehicles_list:
        text_object.insert(tk.END, i.number_plate + ': ' + i.colour + ' ' +
                           i.vehicle_type + '\n')

    return text_object
