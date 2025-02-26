"""Scripts that are used to generate different GUI windows."""
from .vehicle_classes import Car, Van, LorryOrPickup
from .run_sql import execute_sql_select, select_type_from_num_plate
from .run_sql import select_based_on_type
from .verify_inputs import verify_inputs
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
    # Clears all text from the Text widget
    text_object.delete('1.0', 'end')

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
            output = output + ', ' + str(vehicle.num_of_seats) + ' seater '
    elif vehicle.vehicle_type == 'van':
        if vehicle.cargo_capacity is not None:
            output = output + ', ' + str(vehicle.cargo_capacity)
            output = output + 'l cargo capacity '
    elif vehicle.vehicle_type == 'lorry' or vehicle.vehicle_type == 'pickup':
        if vehicle.cargo_capacity is not None:
            output = output + ', ' + str(vehicle.cargo_capacity)
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
    """Assign values to classes for 'vehicles by service due' window.

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


def assign_num_plate_classes(num_plate: str) -> list:
    """Assign values to classes for 'vehicles by number plate' window.

    Args:
        num_plate(str): the number plate of the vehicle

    Returns:
         output(list): list of classes with assigned values
    """
    vehicle_type = select_type_from_num_plate(num_plate)
    sql_result: list = select_based_on_type(vehicle_type, num_plate)

    output: list = []
    for row in sql_result:
        if vehicle_type == 'car':
            new_car = Car(num_plate, row[0], vehicle_type, row[3], row[2],
                          row[1])
            output.append(new_car)
        elif vehicle_type == 'van':
            new_van = Van(num_plate, row[0], vehicle_type, row[3], row[2],
                          row[1])
            output.append(new_van)
        elif vehicle_type == 'lorry' or vehicle_type == 'pickup':
            new_lorry = LorryOrPickup(num_plate, row[0], vehicle_type, row[3],
                                      row[4],
                                      row[2],
                                      row[1])
            output.append(new_lorry)
    return output


def generate_insert_widgets(frame: tk.Frame, vehicle_type: str):
    """Generate the widgets to be used in the insert vehicle window.

    Args:
        frame (tk.Frame): The frame used in the widgets
        vehicle_type (str): The selected vehicle type

    Returns:
        element_list (list): The list of generated widgets
    """
    element_list: list = []

    title = tk.Label(frame,
                     text='Write information into text boxes',
                     width=35)
    element_list.append(title)

    num_plate = tk.Text(frame, width=55, height=1)
    num_plate.insert(tk.END, 'Number Plate')
    element_list.append(num_plate)

    colour = tk.Text(frame, width=55, height=1)
    colour.insert(tk.END, 'Colour')
    element_list.append(colour)

    tax_date = tk.Text(frame, width=55, height=1)
    tax_date.insert(tk.END, 'Tax Due Date (YYYY-MM-DD)')
    element_list.append(tax_date)

    service_date = tk.Text(frame, width=55, height=1)
    service_date.insert(tk.END, 'Service Date (YYYY-MM-DD)')
    element_list.append(service_date)

    if vehicle_type == 'Car':
        num_of_seats = tk.Text(frame, width=55, height=1)
        num_of_seats.insert(tk.END, 'Number of Seats')
        element_list.append(num_of_seats)
    elif vehicle_type == 'Van':
        cargo_capacity = tk.Text(frame, width=55, height=1)
        cargo_capacity.insert(tk.END, 'Cargo Capacity')
        element_list.append(cargo_capacity)
    elif vehicle_type == 'Lorry' or vehicle_type == 'Pickup':
        cargo_capacity = tk.Text(frame, width=55, height=1)
        cargo_capacity.insert(tk.END, 'Cargo Capacity')
        element_list.append(cargo_capacity)

        cab_type = tk.Text(frame, width=55, height=1)
        cab_type.insert(tk.END, 'Cab Type')
        element_list.append(cab_type)

    return element_list


def set_insert_values(element_list: list[tk.Text], vehicle_type: str):
    vehicle: object = None
    number_plate: str = element_list[1].get('1.0', tk.END).strip()
    colour: str = element_list[2].get('1.0', tk.END).strip()
    tax_date: str = element_list[3].get('1.0', tk.END).strip()
    service_date: str = element_list[4].get('1.0', tk.END).strip()
    # TODO write colour conversion to convert colour into id
    if vehicle_type == 'Car':
        num_of_seats = element_list[5].get('1.0', tk.END).strip()
        vehicle = Car(number_plate.upper(), colour, vehicle_type.lower(),
                      num_of_seats,
                      service_date, tax_date)
    elif vehicle_type == 'Van':
        cargo_capacity = element_list[5].get('1.0', tk.END).strip()
        vehicle = Van(number_plate.upper(), colour, vehicle_type.lower(),
                      cargo_capacity,
                      service_date, tax_date)
    elif vehicle_type == 'Lorry' or vehicle_type == 'Pickup':
        cargo_capacity = element_list[5].get('1.0', tk.END).strip()
        cab_type = element_list[6].get('1.0', tk.END).strip()
        vehicle = LorryOrPickup(number_plate.upper(), colour,
                                vehicle_type.lower(),
                                cargo_capacity, cab_type.lower(),
                                service_date, tax_date)

    verify_inputs(vehicle)

    return vehicle
