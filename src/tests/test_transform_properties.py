"""Test for the transform_properties util."""
from ..utils import transfrom_properties as tp


def test_transform_properties():
    """Test method for the util."""
    test = [None, 'yellow', 'pickup']
    expected = [None, 19, 4]

    error_message = 'transformed properties do not match expected'
    assert tp.transform_properties(test) == expected, error_message
