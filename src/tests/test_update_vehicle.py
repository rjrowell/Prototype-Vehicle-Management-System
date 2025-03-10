"""Module to test the update vehicle window."""
import tkinter as tk
import pytest
import sqlite3

from ..window_classes import UpdateVehicle
from ..utils import run_sql


window_instance = UpdateVehicle(tk.Tk())

window_widgets = [
    window_instance._title,
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
    expected_text = 'Please Enter Number Plate of Vehicle to Update:'
    assert window_widgets[0].cget('text') == expected_text
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

    pack_string = 'pack'

    monkeypatch.setattr(window_instance._title, pack_string, mock_pack)
    monkeypatch.setattr(window_instance._text, pack_string, mock_pack)
    monkeypatch.setattr(window_instance._enter_button, pack_string, mock_pack)
    monkeypatch.setattr(window_instance._quit_button, pack_string, mock_pack)
    monkeypatch.setattr(window_instance._frame, pack_string, mock_pack)
    window_instance.build_window()

    assert len(pack_calls) == 5


def test_submit_text(reset_db, monkeypatch):
    """Test the submit text method.

    Args:
        reset_db: fixture to reset the database before test
        monkeypatch" library to allow patching of destroy method
    """

    destroy_flag = False

    def mock_destroy():
        nonlocal destroy_flag
        destroy_flag = True

    monkeypatch.setattr(window_instance._title, 'destroy', mock_destroy)

    window_instance._text.insert(tk.END, 'TE57ING')
    window_instance._submit_text()
    expected = 'No Vehicle found, Please enter a Valid Number Plate'
    assert window_instance._title.cget('text') == expected

    window_instance._text.delete('1.0', tk.END)
    window_instance._text.insert(tk.END, 'HC56XPQ')
    window_instance._submit_text()

    assert destroy_flag is True


def test_submit_info(reset_db, monkeypatch):
    """Test the submit info method.

    Args:
        reset_db: fixture to reset the database before test
        monkeypatch: library to allow patching of destroy method
    """
    close_flag = False

    def mock_close():
        print('here')
        nonlocal close_flag
        close_flag = True

    monkeypatch.setattr(window_instance, 'close_windows', mock_close)

    label = tk.Label()
    blank_text = tk.Text()
    seat_number = tk.Text()
    seat_number.insert(tk.END, '99')

    error_widgets = [
        label,
        blank_text,
        blank_text,
        blank_text,
        blank_text,
    ]

    success_widgets = [
        label,
        blank_text,
        blank_text,
        blank_text,
        seat_number,
    ]

    window_instance._number_plate = ('HC56XPQ')
    window_instance._widgets = error_widgets

    window_instance._submit_info()
    assert error_widgets[0].cget('text') == 'No Valid Options Set'

    window_instance._widgets = success_widgets
    window_instance._submit_info()
    assert close_flag is True
