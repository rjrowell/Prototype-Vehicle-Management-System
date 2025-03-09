"""Tests the list all vehicles window class."""
import pytest
import tkinter as tk
import sqlite3

from ..window_classes import SearchByNumberPlate
from ..utils import run_sql

window_instance = SearchByNumberPlate(tk.Tk())

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
    expected_title_text = 'Please Enter a Vehicle Number Plate:'
    assert window_widgets[0].cget('text') == expected_title_text
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

    monkeypatch.setattr(window_instance._title, 'pack', mock_pack)
    monkeypatch.setattr(window_instance._text, 'pack', mock_pack)
    monkeypatch.setattr(window_instance._enter_button, 'pack', mock_pack)
    monkeypatch.setattr(window_instance._quit_button, 'pack', mock_pack)
    monkeypatch.setattr(window_instance._frame, 'pack', mock_pack)
    window_instance.build_window()

    assert len(pack_calls) == 5


def test_submit_text(reset_db):
    """Test the submit text method.

    Try a failing entry then a passing one

    Args:
        reset_db: reset the database before testing
    """
    window_instance._text.insert(tk.END, 'Test')
    window_instance.submit_text()
    test_text = window_instance._title.cget('text')
    assert test_text == 'No Vehicle found, Please enter a Valid Number Plate'

    window_instance._text.delete("1.0", tk.END)
    window_instance._text.insert(tk.END, 'HC56XPQ')
    window_instance.submit_text()
    test_text = window_instance._title.cget('text')
    assert test_text == 'Number Plate Found:'
