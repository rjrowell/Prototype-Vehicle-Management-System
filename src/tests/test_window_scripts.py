"""Tests the window_scripts module."""
import sqlite3
import tkinter as tk

import pytest

from ..utils import run_sql
from ..utils import vehicle_classes as vc
from ..utils import window_scripts as ws

mock_root = tk.Tk()
mock_frame = tk.Frame(mock_root)


# Fixture to mock sqlite3.connect
@pytest.fixture
def mock_db_connection(monkeypatch):
    """Fixture to mock sqlite3.connect to use the test database.

    Args:
        monkeypatch: pytest feature to allow mocking of connect
    """
    original_connect = sqlite3.connect

    def mock_connect(db_name):
        return original_connect('src/tests/resources/test_vehicles.db')

    # Replace sqlite3.connect with our mock function
    monkeypatch.setattr(sqlite3, 'connect', mock_connect)


@pytest.fixture()
def reset_db(mock_db_connection):
    """Reset the database before each test.

    Args:
        mock_db_connection: The mock connection
    """
    run_sql.execute_sql('src/sql/drop_tables.sql')
    run_sql.execute_sql('src/sql/create_tables.sql')
    run_sql.execute_sql('src/sql/insert_into_tables.sql')


def test_get_text_to_display():
    """Test the get text to display function."""
    test_text1 = tk.Text(height=1, width=10)
    test_text2 = tk.Text(height=1, width=10)

    test_vehicles_list1 = False

    test_vehicles_list2 = [vc.Car('HC56XPQ', 'red', 'car', 5, None, None)]

    test_output1: tk.Text = ws.get_text_to_display(
        test_text1,
        test_vehicles_list1,
    )

    test_output2: tk.Text = ws.get_text_to_display(
        test_text2,
        test_vehicles_list2,
    )

    test_output1 = test_output1.get('1.0', tk.END).strip()
    test_output2 = test_output2.get('1.0', tk.END).strip()

    assert test_output1 == 'No vehicles found.'
    assert test_output2 == 'HC56XPQ: red car, 5 seater'


def test_generate_insert_widgets():
    """Test the get text by vehicle method."""
    test_element_list_car = ws.generate_insert_widgets(mock_frame, 'car')
    test_element_list_van = ws.generate_insert_widgets(mock_frame, 'van')
    test_element_list_lorry = ws.generate_insert_widgets(mock_frame, 'lorry')

    test_text_car = test_element_list_car[5].get('1.0', 'end-1c')
    test_text_van = test_element_list_van[5].get('1.0', 'end-1c')
    test_text_lorry = test_element_list_lorry[6].get('1.0', 'end-1c')

    car_expected = 'Number of Seats'
    van_expected = 'Cargo Capacity'
    l_expected = 'Cab Type'

    assert len(test_element_list_car) == 6 and test_text_car == car_expected
    assert len(test_element_list_car) == 6 and test_text_van == van_expected
    assert len(test_element_list_lorry) == 7 and test_text_lorry == l_expected


def test_insert_values():
    """Test the insert values method."""
    # Do not need to explicitly test if inserts in db since that is
    # covered in test_run_sql
    test_element_list_car = ws.generate_insert_widgets(mock_frame, 'car')
    test_element_list_van = ws.generate_insert_widgets(mock_frame, 'van')
    test_element_list_lorry = ws.generate_insert_widgets(mock_frame, 'lorry')

    with pytest.raises(TypeError):
        ws.insert_values(test_element_list_car, 'Car')

    with pytest.raises(TypeError):
        ws.insert_values(test_element_list_van, 'Van')

    with pytest.raises(TypeError):
        ws.insert_values(test_element_list_lorry, 'Lorry')


def test_get_update_widgets(reset_db):
    """Method for testing the get update widgets method.

    Args:
        reset_db: fixture that resets the test db before test
    """
    test_car = ws.get_update_widgets_from_plate(mock_frame, 'HC56XPQ')
    test_van = ws.get_update_widgets_from_plate(mock_frame, 'HC62XAC')
    test_lorry = ws.get_update_widgets_from_plate(mock_frame, 'BG70LKM')

    assert test_car[5].get('1.0', 'end-1c') == 'Number of Seats'
    assert test_van[5].get('1.0', 'end-1c') == 'Cargo Capacity'
    assert test_lorry[6].get('1.0', 'end-1c') == 'Cab Type'


def test_remove_vehicle_from_db(reset_db):
    """Test the remove vehicle from db method.

    Args:
        reset_db: fixture that resets the test db before test
    """
    ws.remove_vehicle_from_db('HC56XPQ')
    test_output = run_sql.select_based_on_type('car', 'HC56XPQ')

    assert not test_output, 'select was not empty'
