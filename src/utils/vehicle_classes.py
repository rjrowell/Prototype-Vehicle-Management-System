"""Defines classes that represent the vehicles in the system.

There are four 'specialised' vehicles: Car, Van, Lorry, Pickup,
these are represented in an object oriented way by the three
classes in this module.

All 'specialised' vehicles inherit from the base class Vehicle,
which provides common methods and properties for each vehicle.
"""


class Vehicle(object):
    """vehicle class, defines methods and variables to be inherited."""

    def __init__(
        self,
        number_plate: str,
        colour: str,
        vehicle_type: str,
        service_due_date: str,
        tax_due_date: str,
    ):
        """Initialise car class.

        Args:
            number_plate (str): The cars number plate.
            colour (str): The cars colour.
            vehicle_type (str): The type of vehicle being represented as string
            service_due_date (str): The cars service due date.
            tax_due_date (str): The cars tax due date.

        """
        self._number_plate = number_plate
        self._colour = colour
        self._vehicle_type = vehicle_type
        self._service_due_date = service_due_date
        self._tax_due_date = tax_due_date

    @property
    def properties(self) -> list:
        """Get all vehicle properties as a list.

        Returns:
            vehicle_properties (list): The list of the vehicles properties

        """
        return [
            self._number_plate,
            self._colour,
            self._vehicle_type,
            self._service_due_date,
            self._tax_due_date,
        ]

    @property
    def number_plate(self) -> str:
        """Get current plate.

        Returns:
            number plate.

        """
        return self._number_plate

    @property
    def colour(self) -> str:
        """Get current colour.

        Returns:
            colour.

        """
        return self._colour

    @property
    def vehicle_type(self) -> str:
        """Get current vehicle type.

        Returns:
            vehicle type.

        """
        return self._vehicle_type

    @property
    def service_due_date(self) -> str:
        """Get mot due date.

        Returns:
            MOT due date

        """
        return self._service_due_date

    @property
    def tax_due_date(self) -> str:
        """Get tax due date.

        Returns:
            tax due date

        """
        return self._tax_due_date


class Car(Vehicle):
    """Car class that inherits from vehicle."""

    def __init__(
        self,
        number_plate: str,
        colour: str,
        vehicle_type: str,
        num_of_seats: int,
        mot_due_date: str,
        tax_due_date: str,
    ):
        """Initialise car class.

        Args:
            number_plate (str): The cars number plate.
            colour (str): The cars colour.
            num_of_seats (int): The number of seats in the car.
            vehicle_type (str): The type of vehicle being represented as string
            mot_due_date (str): The cars mot due date.
            tax_due_date (str): The cars tax due date.

        """
        super().__init__(
            number_plate,
            colour,
            vehicle_type,
            mot_due_date,
            tax_due_date,
        )
        self._num_of_seats = num_of_seats

    @property
    def properties(self) -> list:
        """Get all car properties as a list.

        Returns:
            vehicle_properties (list): The list of the vehicles properties

        """
        vehicle_properties: list = super().properties
        vehicle_properties.append(self._num_of_seats)
        return vehicle_properties

    @property
    def num_of_seats(self) -> int:
        """Get current number of seats.

        Returns:
            current number of seats.

        """
        return self._num_of_seats


class Van(Vehicle):
    """Van class that inherits from vehicle."""

    def __init__(
        self,
        number_plate: str,
        colour: str,
        vehicle_type: str,
        cargo_capacity: int,
        mot_due_date: str,
        tax_due_date: str,
    ):
        """Initialise car class.

        Args:
            number_plate (str): The cars number plate.
            colour (str): The cars colour.
            vehicle_type (str): The type of vehicle being represented as string
            cargo_capacity (int): The capcity in litres of the van.
            mot_due_date (str): The cars mot due date.
            tax_due_date (str): The cars tax due date.

        """
        super().__init__(
            number_plate,
            colour,
            vehicle_type,
            mot_due_date,
            tax_due_date,
        )
        self._cargo_capacity = cargo_capacity

    @property
    def properties(self) -> list:
        """Get all van properties as a list.

        Returns:
            vehicle_properties (list): The list of the vehicles properties

        """
        vehicle_properties: list = super().properties
        vehicle_properties.append(self._cargo_capacity)
        return vehicle_properties

    @property
    def cargo_capacity(self) -> int:
        """Get cargo capacity of van.

        Returns:
            Vans cargo capacity

        """
        return self._cargo_capacity


class LorryOrPickup(Vehicle):
    """Class that represents both lorries and pickups.

    Inherits from vehicle.
    """

    def __init__(
        self,
        number_plate: str,
        colour: str,
        vehicle_type: str,
        cargo_capacity: int,
        cab_type: str,
        mot_due_date: str,
        tax_due_date: str,
    ):
        """Initialise lorry class.

        Args:
            number_plate (str): The cars number plate.
            colour (str): The cars colour.
            vehicle_type (str): The type of vehicle being represented as string
            cargo_capacity (int): The capcity in litres of the lorry.
            cab_type (str): The type of cab for the lorry or pickup
            mot_due_date (str): The cars mot due date.
            tax_due_date (str): The cars tax due date.

        """
        super().__init__(
            number_plate,
            colour,
            vehicle_type,
            mot_due_date,
            tax_due_date,
        )
        self._cargo_capacity = cargo_capacity
        self._cab_type = cab_type

    @property
    def properties(self) -> list:
        """Get all car properties as a list.

        Returns:
            vehicle_properties (list): The list of the vehicles properties

        """
        vehicle_properties: list = super().properties
        vehicle_properties.append(self._cargo_capacity)
        vehicle_properties.append(self._cab_type)
        return vehicle_properties

    @property
    def cargo_capacity(self) -> int:
        """Get cargo capacity of lorry.

        Returns:
            Lorry's cargo capacity

        """
        return self._cargo_capacity

    @property
    def cab_type(self) -> int:
        """Get cab type of lorry.

        Returns:
            Lorry's cab type

        """
        return self._cab_type
