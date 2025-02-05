"""Scripts that are used by the 'display all veichles' window."""
from classes import Car, Van, LorryOrPickup


def all_veichles_build_classes(sql_output: list):
    """Build the classes 'list all veichles' window.

    Args:
        sql_output(list): the output of an sql select statement

    Returns:
        output(list): a list of new classes for the window
    """
    output: list = []

    for row in sql_output:
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