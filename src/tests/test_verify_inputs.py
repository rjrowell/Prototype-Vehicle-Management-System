"""Module testing verify inputs and it's helper functions."""
import pytest

from ..utils import vehicle_classes, verify_inputs


def test_verify_numplate():
    """Test the verify numplate helper function."""
    assert verify_inputs.verify_numplate('TE57ING') is True

    with pytest.raises(TypeError):
        verify_inputs.verify_numplate('invalid')


def test_verify_integer():
    """Test the verify integer helper function."""
    assert verify_inputs.verify_integer(10) is True

    with pytest.raises(TypeError):
        verify_inputs.verify_integer('hello')


def test_verify_date():
    """Test the verify date helper function."""
    assert verify_inputs.verify_date('2025-12-25') is True

    # Assert date in the past throws error
    with pytest.raises(TypeError):
        verify_inputs.verify_date('2024-12-25')

    # Assert non-date throws error
    with pytest.raises(TypeError):
        verify_inputs.verify_date('fizzbuzz')


def test_verify_cab_type():
    """Test the verify cab type helper function."""
    # assert all valid paths work
    assert verify_inputs.verify_cab_type('day', 'lorry') is True
    assert verify_inputs.verify_cab_type('sleeper', 'lorry') is True

    assert verify_inputs.verify_cab_type('single', 'pickup') is True
    assert verify_inputs.verify_cab_type('double', 'pickup') is True

    # assert invalid paths fail
    with pytest.raises(TypeError):
        verify_inputs.verify_cab_type('day', 'pickup')

    with pytest.raises(TypeError):
        verify_inputs.verify_cab_type('single', 'lorry')


def test_verify_inputs():
    """Test integration of heper functions through verify input function."""
    test_car = vehicle_classes.Car(
        'TE57ING',
        'red',
        'car',
        5,
        '2025-12-25',
        '2025-12-25',
    )

    test_van = vehicle_classes.Van(
        'TE57ING',
        'red',
        'van',
        5,
        '2025-12-25',
        '2025-12-25',
    )

    test_lorry = vehicle_classes.LorryOrPickup(
        'TE57ING',
        'red',
        'lorry',
        35000,
        'sleeper',
        '2025-12-25',
        '2025-12-25',
    )

    assert verify_inputs.verify_inputs(test_car) is None
    assert verify_inputs.verify_inputs(test_van) is None
    assert verify_inputs.verify_inputs(test_lorry) is None
