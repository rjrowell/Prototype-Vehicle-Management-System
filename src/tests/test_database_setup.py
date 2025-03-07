"""Test the database stup script."""
import sqlite3

import pytest

from src import database_setup

from ..utils import run_sql


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


def test_database_setup(mock_db_connection):
    """Run the database setup script.

    Args:
        mock_db_connection: The mock database connection to the test db
    """
    run_sql.execute_sql('src/tests/resources/test_run_sql/test_insert.sql')
    database_setup.main()

    conn = sqlite3.connect('vehicles.db')
    cursor = conn.cursor()

    sql_file = 'src/tests/resources/test_run_sql/test_select_car.sql'
    sql_file = run_sql.read_sql_file(sql_file)

    output = cursor.execute(sql_file, ('TE57ING',)).fetchone()

    conn.close()

    assert output is None, 'DB not reset corrctly'
