"""Defines classes to be used in this project."""


class Veichle:
    """Veichle class, defines methods and variables to be inherited."""

    _veichle_type: str = None
    _number_plate: str = None
    _colour: str = None

    def __init__(self, number_plate: str, 
                 colour: str, veichle_type: str):
        """Initialise car class.

        Args:
            number_plate (str): The cars number plate.
            colour (str): The cars colour.
            veichle_type (str): The type of veichle being represented as string
        """
        self._number_plate = number_plate
        self._colour = colour
        self._veichle_type = veichle_type

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
    def veichle_type(self) -> str:
        """Get current veichle type.

        Returns:
            veichle type.
        """
        return self._veichle_type


class Car(Veichle):
    """Car class that inherits from Veichle."""

    __num_of_seats: int = None

    def __init__(self, number_plate: str, colour: str, 
                 veichle_type: str, num_of_seats: int):
        """Initialise car class.

        Args:
            number_plate (str): The cars number plate.
            colour (str): The cars colour.
            num_of_seats (int): The number of seats in the car.
            veichle_type (str): The type of veichle being represented as string
        """
        super().__init__(number_plate, colour, veichle_type)
        self.__num_of_seats = num_of_seats

    @property
    def num_of_seats(self) -> int:
        """Get current number of seats.

        Returns:
            current number of seats.
        """
        return self.__num_of_seats


class Van(Veichle):
    """Van class that inherits from Veichle."""

    __cargo_capacity: int = None

    def __init__(self, number_plate: str, colour: str, 
                 veichle_type: str, cargo_capacity: int):
        """Initialise car class.

        Args:
            number_plate (str): The cars number plate.
            colour (str): The cars colour.
            veichle_type (str): The type of veichle being represented as string
            cargo_capacity (int): The capcity in litres of the van.
        """
        super().__init__(number_plate, colour), veichle_type
        self.__cargo_capacity = cargo_capacity

    @property
    def cargo_capacity(self) -> int:
        """Get cargo capacity of van.

        Returns:
            Vans cargo capacity
        """
        return self.__cargo_capacity


class LorryOrPickup(Veichle):
    """Lorry class that inherits from veichle."""
    
    __cargo_capacity: int = None
    __cab_type: str = None

    def __init__(self, number_plate: str, colour: str, 
                 veichle_type: str, cargo_capacity: int,
                 cab_type: str):
        """Initialise lorry class.

        Args:
            number_plate (str): The cars number plate.
            colour (str): The cars colour.
            veichle_type (str): The type of veichle being represented as string
            cargo_capacity (int): The capcity in litres of the lorry.
            cab_type (str): The type of cab for the lorry (Sleeper, Day)
        """
        super().__init__(number_plate, colour, veichle_type)
        self.__cargo_capacity = cargo_capacity
        self.__cab_type = cab_type

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
