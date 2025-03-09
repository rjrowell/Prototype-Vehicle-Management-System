"""Module that tests the updata changed values part of window scripts."""
import sqlite3
import tkinter as tk

import pytest

from ..utils import run_sql
from ..utils.window_scripts import update_changed_values

colour_text = tk.Text()
number_text = tk.Text()
cab_type_text = tk.Text()
date_text = tk.Text()

colour_text.insert(tk.END, 'brown')
number_text.insert(tk.END, '99')
cab_type_text.insert(tk.END, 'day')
date_text.insert(tk.END, '2026-05-05')


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


def test_update_changed_values(mock_db_connection, reset_db):
    """Test for the update changed values method.

    Args:
        mock_db_connection: The fixture to connect to test db
        reset_db: Fixture that resets db at start of test
    """
    car_elements = [
        None,
        colour_text,
        date_text,
        date_text,
        number_text,
    ]

    lorry_elements = [
        None,
        colour_text,
        date_text,
        date_text,
        number_text,
        cab_type_text,
    ]

    empty_elements = [
        cab_type_text,
        cab_type_text,
        cab_type_text,
        cab_type_text,
        cab_type_text,
    ]

    update_changed_values(car_elements, 'HC56XPQ')
    update_changed_values(car_elements, 'HC62XAC')
    update_changed_values(lorry_elements, 'QS52BCG')

    test_results = []
    test_results.append(run_sql.select_based_on_type('car', 'HC56XPQ'))
    test_results.append(run_sql.select_based_on_type('van', 'HC62XAC'))
    test_results.append(run_sql.select_based_on_type('lorry', 'QS52BCG'))

    car_colour = test_results[0][0][0]
    van_colour = test_results[1][0][0]
    lorry_colour = test_results[2][0][0]

    num = 99

    assert car_colour == 'brown' and test_results[0][0][3] == num
    assert van_colour == 'brown' and test_results[1][0][3] == num
    assert lorry_colour == 'brown' and test_results[2][0][4] == 'day'
    assert update_changed_values(empty_elements, 'HC56XPQ') is False
