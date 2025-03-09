"""Test the build classes utility module."""
import sqlite3

import pytest

from ..utils import build_classes as bc
from ..utils import run_sql
from ..utils import vehicle_classes as vc


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


def test_build_classes(mock_db_connection, reset_db):
    """Test the build classes function.

    Args:
        mock_db_connection: The mock connection
        reset_db: resets the database
    """
    output1: list[vc.Vehicle] = bc.build_classes(
        'src/sql/select_all_vehicles.sql',
        'all_vehicles',
    )

    output2: list[vc.Vehicle] = bc.build_classes(
        'src/sql/select_tax_due_vehicles.sql',
        'tax_due',
    )

    output3: list[vc.Vehicle] = bc.build_classes(
        'src/sql/select_service_due_vehicles.sql',
        'service_due',
    )

    output4: list[vc.Vehicle] = bc.build_classes(
        'BG70LKM',
        'num_plate',
    )

    assert output1[0].number_plate == 'HC56XPQ'
    assert output2[0].number_plate == 'QS52BCG'
    assert output3[0].number_plate == 'QS52BCG'
    assert output4[0].number_plate == 'BG70LKM'
