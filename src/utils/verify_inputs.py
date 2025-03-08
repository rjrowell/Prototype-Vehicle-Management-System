"""This module verifies inputs entered.

Throws type errors if they are incorrect.
"""
import re
from datetime import datetime

from .do_nothing import do_nothing
from .vehicle_classes import Vehicle

lp = ('lorry', 'pickup')


def verify_inputs(vehicle: Vehicle):
    """Verify inputs from Vehicle object.

    Args:
        vehicle (Vehicle): Vehicle object to check

    """
    verify_numplate(vehicle.number_plate)
    verify_date(vehicle.service_due_date)
    verify_date(vehicle.tax_due_date)

    if vehicle.vehicle_type == 'car':
        verify_integer(vehicle.num_of_seats)
    elif vehicle.vehicle_type == 'van':
        verify_integer(vehicle.cargo_capacity)
    elif vehicle.vehicle_type in lp:
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
    regex = '^[A-Z]{2}[0-9]{2}[ ]?[A-Z]{3}$'
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
    today = datetime.today().date()
    try:
        date: datetime = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        do_nothing()
        raise TypeError

    # Ensure the entered date is in the future
    if date.date() <= today:
        raise TypeError

    return True


def verify_integer(number: int):
    """Verify a integer input is an integer.

    Args:
        number (int): The integer to check

    Raises:
        TypeError: if integer is not an int

    Returns:
        True: if no error is thrown returns true
    """
    try:
        int(number)
    except ValueError:
        do_nothing()
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
    lorry_cabs = ('sleeper', 'day')
    pickup_cabs = ('single', 'double')

    if vehicle_type == 'lorry':
        if cab_type not in lorry_cabs:
            raise TypeError
    elif cab_type not in pickup_cabs:
        raise TypeError

    return True
