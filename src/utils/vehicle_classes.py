"""Defines classes to be used in this project."""


class Vehicle:
    """vehicle class, defines methods and variables to be inherited."""

    _vehicle_type: str = None
    _number_plate: str = None
    _colour: str = None
    _service_due_date: str = None
    _tax_due_date: str = None

    def __init__(self, number_plate: str, 
                 colour: str, vehicle_type: str,
                 service_due_date: str, tax_due_date: str):
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
        vehicle_properties: list = [self._number_plate, self._colour,
                                    self._vehicle_type, self._service_due_date,
                                    self._tax_due_date]
        return vehicle_properties

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

    __num_of_seats: int = None

    def __init__(self, number_plate: str, colour: str, 
                 vehicle_type: str, num_of_seats: int,
                 mot_due_date: str, tax_due_date: str):
        """Initialise car class.

        Args:
            number_plate (str): The cars number plate.
            colour (str): The cars colour.
            num_of_seats (int): The number of seats in the car.
            vehicle_type (str): The type of vehicle being represented as string
            mot_due_date (str): The cars mot due date.
            tax_due_date (str): The cars tax due date.
        """
        super().__init__(number_plate, colour, vehicle_type, mot_due_date,
                         tax_due_date)
        self.__num_of_seats = num_of_seats

    @property
    def properties(self) -> list:
        """Get all car properties as a list.

        Returns:
            vehicle_properties (list): The list of the vehicles properties
        """
        vehicle_properties: list = super().properties
        vehicle_properties.append(self.__num_of_seats)
        return vehicle_properties

    @property
    def num_of_seats(self) -> int:
        """Get current number of seats.

        Returns:
            current number of seats.
        """
        return self.__num_of_seats


class Van(Vehicle):
    """Van class that inherits from vehicle."""

    __cargo_capacity: int = None

    def __init__(self, number_plate: str, colour: str, 
                 vehicle_type: str, cargo_capacity: int,
                 mot_due_date: str, tax_due_date: str):
        """Initialise car class.

        Args:
            number_plate (str): The cars number plate.
            colour (str): The cars colour.
            vehicle_type (str): The type of vehicle being represented as string
            cargo_capacity (int): The capcity in litres of the van.
            mot_due_date (str): The cars mot due date.
            tax_due_date (str): The cars tax due date.
        """
        super().__init__(number_plate, colour, vehicle_type, mot_due_date,
                         tax_due_date)
        self.__cargo_capacity = cargo_capacity

    @property
    def properties(self) -> list:
        """Get all van properties as a list.

        Returns:
            vehicle_properties (list): The list of the vehicles properties
        """
        vehicle_properties: list = super().properties
        vehicle_properties.append(self.__cargo_capacity)
        return vehicle_properties

    @property
    def cargo_capacity(self) -> int:
        """Get cargo capacity of van.

        Returns:
            Vans cargo capacity
        """
        return self.__cargo_capacity


class LorryOrPickup(Vehicle):
    """Lorry class that inherits from vehicle."""

    __cargo_capacity: int = None
    __cab_type: str = None

    def __init__(self, number_plate: str, colour: str, 
                 vehicle_type: str, cargo_capacity: int,
                 cab_type: str,
                 mot_due_date: str, tax_due_date: str):
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
        super().__init__(number_plate, colour, vehicle_type, mot_due_date,
                         tax_due_date)
        self.__cargo_capacity = cargo_capacity
        self.__cab_type = cab_type

    @property
    def properties(self) -> list:
        """Get all car properties as a list.

        Returns:
            vehicle_properties (list): The list of the vehicles properties
        """
        vehicle_properties: list = super().properties
        vehicle_properties.append(self.__cargo_capacity)
        vehicle_properties.append(self.__cab_type)
        return vehicle_properties

    @property
    def cargo_capacity(self) -> int:
        """Get cargo capacity of lorry.

        Returns:
            Lorry's cargo capacity
        """
        return self.__cargo_capacity

    @property
    def cab_type(self) -> int:
        """Get cab type of lorry.

        Returns:
            Lorry's cargo capacity
        """
        return self.__cab_type
