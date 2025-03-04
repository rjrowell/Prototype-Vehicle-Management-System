"""This module verifies inputs entered.

Throws type errors if they are incorrect.
"""
import re
from datetime import datetime

from .vehicle_classes import Car, LorryOrPickup, Van, Vehicle


def verify_inputs(vehicle: Vehicle):
    """Verify inputs from Vehicle object.

    Args:
        vehicle (Vehicle): Vehicle object to check

    """
    verify_numplate(vehicle.number_plate)
    verify_date(vehicle.service_due_date)
    verify_date(vehicle.tax_due_date)

    if vehicle.vehicle_type == 'car':
        vehicle: Car = vehicle
        verify_integer(vehicle.num_of_seats)
    elif vehicle.vehicle_type == 'van':
        vehicle: Van = vehicle
        verify_integer(vehicle.cargo_capacity)
    elif vehicle.vehicle_type == 'lorry' or vehicle.vehicle_type == 'pickup':
        vehicle: LorryOrPickup = vehicle
        verify_integer(vehicle.cargo_capacity)
        verify_cab_type(vehicle.cab_type, vehicle.vehicle_type)


def verify_numplate(num_plate: str):
    """Verify a numberplate is correct format.

    Args:
        num_plate (str): The number plate to check

    Raises:
        TypeError: if number plate is invalid
    
    Returns:
        True: if no error is thrown returns true

    """
    regex = r'^[A-Z]{2}[0-9]{2}[ ]?[A-Z]{3}$'
    if not bool(re.match(regex, num_plate)):
        raise TypeError

    return True


def verify_date(date: str):
    """Verify a date is correct format.

    Args:
        date (str): The date to check

    Raises:
        TypeError: if date is invalid

    Returns:
        True: if no error is thrown returns true
    """
    try:
        date: datetime = datetime.strptime(date, '%Y-%m-%d')
        today = datetime.today().date()

        # Ensure the entered date is in the future
        if not date.date() > today:
            raise TypeError

    except ValueError:
        raise TypeError

    return True


def verify_integer(input: int):
    """Verify a integer input is an integer.

    Args:
        input (int): The integer to check

    Raises:
        TypeError: if integer is not an int

    Returns:
        True: if no error is thrown returns true
    """
    try:
        int(input)
    except ValueError:
        raise TypeError

    return True


def verify_cab_type(cab_type: str, vehicle_type: str):
    """Verify a cab type is correct for vehicle type.

    Args:
        cab_type (str): The cab type to check
        vehicle_type (str): The vehicle type to check against

    Raises:
        TypeError: if cab type is invalid

    Returns:
        True: if no error is thrown returns true
    """
    if vehicle_type == 'lorry':
        if cab_type != 'sleeper' and cab_type != 'day':
            raise TypeError
    elif vehicle_type == 'pickup':
        if cab_type != 'single' and cab_type != 'double':
            raise TypeError

    return True
