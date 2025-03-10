"""Tests the insert vehicle window class."""
import pytest
import sqlite3
import tkinter as tk

from ..window_classes import InsertVehicle
from ..utils import run_sql

window_instance = InsertVehicle(tk.Tk())

window_widgets = [
    window_instance.selected_value,
    window_instance._enter_button,
    window_instance._quit_button,
]


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


def test_widgets():
    """Test that all widgets were created correctly."""
    assert window_widgets[0].get() == 'Select type of Vehicle to insert'
    assert window_widgets[1].cget('text') == 'Enter'
    assert window_widgets[2].cget('text') == 'Exit'


def test_build_window(monkeypatch):
    """Test that the build window function works correctly.

    Args:
        monkeypatch: library to allow patching of pack function
    """
    pack_calls = []

    def mock_pack():
        pack_calls.append(True)

    monkeypatch.setattr(window_instance._option_menu, 'pack', mock_pack)
    monkeypatch.setattr(window_instance._enter_button, 'pack', mock_pack)
    monkeypatch.setattr(window_instance._quit_button, 'pack', mock_pack)
    monkeypatch.setattr(window_instance._frame, 'pack', mock_pack)
    window_instance.build_window()

    assert len(pack_calls) == 4


def test_submit_type():
    """Test the submit type method."""
    assert window_instance._submit_type() is False

    window_instance.selected_value.set('Pickup')
    assert window_instance._submit_type() is True


def test_insert_text(monkeypatch, reset_db):
    """Test for the insert text method.

    Args:
        monkeypatch: library to allow patching of close window function
        reset_db: fixture that resets the database before testing
    """
    # Check if close windows has been reached
    close_flag = False

    def mock_close():
        nonlocal close_flag
        close_flag = True

    monkeypatch.setattr(window_instance, 'close_windows', mock_close)
    # Tk objects for element lists
    label = tk.Label()
    num_plate = tk.Text()
    colour = tk.Text()
    error_colour = tk.Text()
    dates = tk.Text()
    cargo_capacity = tk.Text()

    num_plate.insert(tk.END, 'TE57ING')
    colour.insert(tk.END, 'green')
    error_colour.insert(tk.END, 'noColour')
    dates.insert(tk.END, '2026-03-03')
    cargo_capacity.insert(tk.END, '999')

    incorrect_entries_list = [
        label,
        dates,
        colour,
        num_plate,
        dates,
        cargo_capacity,
    ]

    incorrect_colour_list = [
        label,
        num_plate,
        error_colour,
        dates,
        dates,
        cargo_capacity,
    ]

    correct_list = [
        label,
        num_plate,
        colour,
        dates,
        dates,
        cargo_capacity,
    ]

    window_instance._vehicle_type = 'Van'
    window_instance._element_list = incorrect_entries_list

    window_instance._insert_text()
    expected = 'One or more entries is incorrect please re-enter'
    assert window_instance._element_list[0].cget('text') == expected

    window_instance._element_list = incorrect_colour_list
    window_instance._insert_text()
    expected = 'Ivalid colour entered'
    assert window_instance._element_list[0].cget('text') == expected

    window_instance._element_list = correct_list
    window_instance._insert_text()
    assert close_flag is True
