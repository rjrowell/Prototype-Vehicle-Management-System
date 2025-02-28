"""Script to transform properties to be db friendly."""

valid_types = {
    'car': 1,
    'van': 2,
    'lorry': 3,
    'pickup:': 4,
}

valid_colours = {
    'beige': 1,
    'black': 2,
    'blue': 3,
    'bronze': 4,
    'brown': 5,
    'cream': 6,
    'green': 7,
    'grey': 8,
    'gold': 9,
    'maroon': 10,
    'multicoloured': 11,
    'orange': 12,
    'pink': 13,
    'purple': 14,
    'red': 15,
    'silver': 16,
    'turquoise': 17,
    'white': 18,
    'yellow': 19,
}


def transform_properties(properties: list) -> list:
    """Transform the properties.

    Args:
        properties (list): the properties to be transformed

    Returns:
        properties (list): properties with type and colour transformed to IDs
    """
    properties[2] = transform_type(properties[2])
    properties[1] = transform_colour(properties[1])
    return properties


def transform_type(vehicle_type: str):
    """Transform type from string to type id.

    Args:
        vehicle_type: the type string to be transformed

    Returns:
        converted_type: the vehicle type converted into an id
    """
    return valid_types[vehicle_type]


def transform_colour(colour: str):
    """Transform colour from string to id.

    Args:
        colour (str): the colour to be converted

    Returns:
        converted_colour: the colour converted to an id
    """
    return valid_colours[colour.lower()]
