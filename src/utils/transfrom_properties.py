"""Script to transform properties to be db friendly."""

valid_types = {
    'car': 1,
    'van': 2,
    'lorry': 3,
    'pickup:': 4,
}


def transform_properties(properties: list):
    """Transform the properties.

    Args:
        properties (list): the properties to be transformed
    """
    properties[2] = transform_type(properties[2])
    properties[3] = transform_colour[properties[1]]

def transform_type(vehicle_type: str):
    """Transform type from string to type id.

    Args:
        vehicle_type: the type string to be transformed

    Returns:
        converted_type: the vehicle type converted into an id
    """
    return valid_types[vehicle_type]
