"""Module to test the update vehicle window."""
import tkinter as tk
import pytest
import sqlite3

from ..window_classes import RemoveVehicle
from ..utils import run_sql


window_instance = RemoveVehicle(tk.Tk())

window_widgets = [
    window_instance._title,
    window_instance._text,
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
    expected_text = 'Please Enter Number Plate of Vehicle to Remove:'
    assert window_widgets[0].cget('text') == expected_text
    assert window_widgets[1].cget('height') == 1
    assert window_widgets[2].cget('text') == 'Enter'
    assert window_widgets[3].cget('text') == 'Exit'


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
        monkeypatch: library to allow patching of destroy method
    """
    close_flag = False

    def mock_close():
        nonlocal close_flag
        close_flag = True

    monkeypatch.setattr(window_instance, 'close_windows', mock_close)

    window_instance._text.insert(tk.END, 'TE57ING')
    window_instance._submit_text()
    expected = 'Invalid Number Plate Entered'
    assert window_instance._title.cget('text') == expected

    window_instance._text.delete('1.0', tk.END)
    window_instance._text.insert(tk.END, 'HC56XPQ')
    window_instance._submit_text()

    assert close_flag is True