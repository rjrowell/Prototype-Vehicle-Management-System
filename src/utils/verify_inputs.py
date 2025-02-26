from .vehicle_classes import Vehicle, Car, Van, LorryOrPickup
from datetime import datetime
import re


def verify_inputs(vehicle: Vehicle):
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
    regex = r"^[A-Z]{2}[0-9]{2}[ ]?[A-Z]{3}$"
    if not bool(re.match(regex, num_plate)):
        raise TypeError


def verify_date(date: str):
    try:
        date: datetime = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today().date()

        # Ensure the entered date is in the future
        if not date.date() > today:
            raise TypeError

    except ValueError:
        raise TypeError


def verify_integer(input: int):
    try:
        int(input)
    except ValueError:
        raise TypeError


def verify_cab_type(cab_type, vehicle_type):
    if vehicle_type == 'lorry':
        if not cab_type == 'sleeper' and not cab_type == 'day':
            raise TypeError
    elif vehicle_type == 'pickup':
        if not cab_type == 'single' and not cab_type == 'double':
            raise TypeError
