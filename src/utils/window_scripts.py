"""Scripts that are called by the GUI windows.

The idea is that these functions 'connect' the front-end to the backend.
They handle logic for when an operation is requested by the user, and then call
run_sql to get and modify data from the db.
"""

import tkinter as tk

from .do_nothing import do_nothing
from .run_sql import (delete_from_db, insert_vehicle_into_db,
                      select_type_from_num_plate, update_vehicle)
from .valid_inputs import valid_colours
from .vehicle_classes import Car, LorryOrPickup, Van
from .verify_inputs import (verify_cab_type, verify_date, verify_inputs,
                            verify_integer)

vehicle_mapping: dict = {
    'car': Car,
    'van': Van,
    'lorry': LorryOrPickup,
    'pickup': LorryOrPickup,
}

text_object_start = '1.0'

check = ('lorry', 'pickup')


def get_text_to_display(text_object: tk.Text, vehicles_list: list):
    """Insert rows of veichle information into TK.Text object.

    Args:
        text_object(tkinter.Text): The original text object
        vehicles_list(list): list of veichles to be inserted into text

    Returns:
        text_object(tkinter.Text): The modified text object

    """
    # Clears all text from the Text widget
    text_object.delete(text_object_start, 'end')

    if vehicles_list is False:
        text_object.insert(tk.END, 'No vehicles found.\n')
    else:
        for inc in vehicles_list:
            display_text: str = get_text_by_vehicle(inc)
            text_object.insert(tk.END, display_text)

    return text_object


def get_text_by_vehicle(vehicle: object) -> str:
    """Given a vehicle, programmaticly generate its display text.

    Based on it's type and what variable it has assigned.

    Args:
        vehicle(object): The vehicle class to generate text from

    Returns:
        output(str): The generated text

    """
    vlp = ('van', 'lorry', 'pickup')
    output = '{0}: {1}'.format(vehicle.number_plate, vehicle.colour)
    output = '{0} {1}'.format(output, vehicle.vehicle_type)

    # Add num of seats or cargo capacity based on vehicle type
    if vehicle.vehicle_type == 'car' and vehicle.num_of_seats is not None:
        output = '{0}, {1} seater '.format(output, vehicle.num_of_seats)
    elif vehicle.vehicle_type in vlp and vehicle.cargo_capacity is not None:
        output = '{0}, {1}l cargo capacity '.format(
            output,
            vehicle.cargo_capacity,
        )

    # Add cab type for applicable vehicles
    if vehicle.vehicle_type in check and vehicle.cab_type is not None:
        output = '{0}, {1} cab'.format(output, vehicle.cab_type)

    # Add maintenance information
    if vehicle.tax_due_date is not None:
        output = '{0}, tax due: {1} '.format(output, vehicle.tax_due_date)

    if vehicle.service_due_date is not None:
        output = '{0}, service due: {1} '.format(
            output,
            vehicle.service_due_date,
        )

    return '{0}{1}'.format(output, '\n')


def generate_insert_widgets_from_type(
    frame: tk.Frame,
    vehicle_type: str,
    element_list: list,
) -> list:
    """Generate widgets based on the type of vehicle.

    Helper function to generate_insert_widgets

    Args:
        frame (tk.Frame): The frame used in the widgets
        vehicle_type (str): The selected vehicle type
        element_list (list): The list of elements to be appended to

    Returns:
        element_list (list): The list with vehicle specific widgets appended
    """
    default_width = 55

    if vehicle_type == 'car':
        num_of_seats = tk.Text(frame, width=default_width, height=1)
        num_of_seats.insert(tk.END, 'Number of Seats')
        element_list.append(num_of_seats)
    elif vehicle_type == 'van':
        cargo_capacity = tk.Text(frame, width=default_width, height=1)
        cargo_capacity.insert(tk.END, 'Cargo Capacity')
        element_list.append(cargo_capacity)
    elif vehicle_type in check:
        cargo_capacity = tk.Text(frame, width=default_width, height=1)
        cargo_capacity.insert(tk.END, 'Cargo Capacity')
        element_list.append(cargo_capacity)

        cab_type = tk.Text(frame, width=default_width, height=1)
        cab_type.insert(tk.END, 'Cab Type')
        element_list.append(cab_type)

    return element_list


def generate_insert_widgets(frame: tk.Frame, vehicle_type: str) -> list:
    """Generate the widgets to be used in the insert vehicle window.

    Args:
        frame (tk.Frame): The frame used in the widgets
        vehicle_type (str): The selected vehicle type

    Returns:
        element_list (list): The list of generated widgets

    """
    element_list: list = []
    widths = [35, 55]
    title = tk.Label(
        frame,
        text='Write information into text boxes',
        width=widths[0],
    )
    element_list.append(title)

    num_plate = tk.Text(frame, width=widths[1], height=1)
    num_plate.insert(tk.END, 'Number Plate')
    element_list.append(num_plate)

    colour = tk.Text(frame, width=widths[1], height=1)
    colour.insert(tk.END, 'Colour')
    element_list.append(colour)

    tax_date = tk.Text(frame, width=widths[1], height=1)
    tax_date.insert(tk.END, 'Tax Due Date (YYYY-MM-DD)')
    element_list.append(tax_date)

    service_date = tk.Text(frame, width=widths[1], height=1)
    service_date.insert(tk.END, 'Service Date (YYYY-MM-DD)')
    element_list.append(service_date)

    return generate_insert_widgets_from_type(
        frame,
        vehicle_type.lower(),
        element_list,
    )


def insert_values(element_list: list[tk.Text], vehicle_type: str):
    """Assign the values entered to a vehicle and insert into db.

    Verify entered data is all correct.

    Args:
        element_list (list[tk.Text]): The list of elements in the window
        vehicle_type (str): Selected type of vehicle

    """
    # Assign each text entry to a vehicle object
    vehicle: object = None
    number_plate: str = element_list[1].get(text_object_start, tk.END).strip()
    colour: str = element_list[2].get(text_object_start, tk.END).strip()
    tax_date: str = element_list[3].get(text_object_start, tk.END).strip()
    service_date: str = element_list[4].get(text_object_start, tk.END).strip()
    # Vehicle specific assignment
    if vehicle_type == 'Car':
        num_of_seats = element_list[5].get(text_object_start, tk.END).strip()
        vehicle = Car(
            number_plate.upper(),
            colour,
            vehicle_type.lower(),
            num_of_seats,
            service_date,
            tax_date,
        )

    elif vehicle_type == 'Van':
        cargo_capacity = element_list[5].get(text_object_start, tk.END).strip()
        vehicle = Van(
            number_plate.upper(),
            colour,
            vehicle_type.lower(),
            cargo_capacity,
            service_date,
            tax_date,
        )

    elif vehicle_type.lower() in check:
        cargo_capacity = element_list[5].get(text_object_start, tk.END).strip()
        cab_type = element_list[6].get(text_object_start, tk.END).strip()
        vehicle = LorryOrPickup(
            number_plate.upper(),
            colour,
            vehicle_type.lower(),
            cargo_capacity,
            cab_type.lower(),
            service_date,
            tax_date,
        )

    verify_inputs(vehicle)

    insert_vehicle_into_db(vehicle.properties)


def get_update_widgets_from_plate(frame: tk.Frame, num_plate: str) -> list:
    """Return a list of elements for the update car window.

    Returned elements is based on the number plate entered

    Args:
        frame (tk.Frame): The window frame for the elements
        num_plate(str): The plate to base the elements on

    Returns:
        widgets (list): The widgets for the update vehicle window
    """
    vehicle_type: str = select_type_from_num_plate(num_plate)
    return generate_insert_widgets(frame, vehicle_type)


def update_changed_values(
    element_list: list[tk.Text],
    num_plate: str,
):
    """Find what values of a car should be changed then update them.

    Args:
        element_list (list[tk.Text]): The list of text elements from window
        num_plate (str): The number plate of the vehicle to be updated

    Returns:
        flag (bool): Return true if succesful false if it is not
    """
    changed_values: dict = {
        'colour_id': False,
        'tax_due_date': False,
        'service_due_date': False,
        'extra1': False,
        'cab_type': False,
    }
    vehicle_type = select_type_from_num_plate(num_plate).lower()

    colour = element_list[1].get(text_object_start, tk.END).strip()
    if colour.lower() in valid_colours:
        changed_values['colour_id'] = colour

    tax_date = element_list[2].get(text_object_start, tk.END).strip()
    try:
        verify_date(tax_date)
    except TypeError:
        do_nothing()
    else:
        changed_values['tax_due_date'] = tax_date

    service_date = element_list[3].get(text_object_start, tk.END).strip()
    try:
        verify_date(service_date)
    except TypeError:
        do_nothing()
    else:
        changed_values['service_due_date'] = service_date

    extra1 = element_list[4].get(text_object_start, tk.END).strip()
    try:
        verify_integer(extra1)
    except TypeError:
        do_nothing()
    else:
        changed_values['extra1'] = int(extra1)

    if vehicle_type in check:
        extra2 = element_list[5].get(text_object_start, tk.END).strip()
        try:
            verify_cab_type(extra2.lower(), vehicle_type)
        except TypeError:
            do_nothing()
        else:
            changed_values['cab_type'] = extra2

    # check if all values are still false
    if all(element is False for element in changed_values.values()):
        return False

    update_vehicle(changed_values, vehicle_type, num_plate)
    return True


def remove_vehicle_from_db(num_plate: str):
    """Remove the vehicle from the database.

    Args:
        num_plate(str): The number plate of the vehicle to remove.
    """
    vehicle_type = select_type_from_num_plate(num_plate)
    delete_from_db(num_plate, vehicle_type)
