"""Test the run_sql util module."""
import sqlite3

import pytest

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


@pytest.fixture()
def reset_db(mock_db_connection):
    """Reset the database before each test.

    Args:
        mock_db_connection: The mock connection
    """
    run_sql.execute_sql('src/sql/drop_tables.sql')
    run_sql.execute_sql('src/sql/create_tables.sql')
    run_sql.execute_sql('src/sql/insert_into_tables.sql')


def test_read_sql_file(mock_db_connection, reset_db):
    """Test the read_sql_file function.

    Args:
        mock_db_connection: The mock connection
        reset_db: resets the database
    """
    expected = 'INSERT INTO van(number_plate, cargo_capacity)'
    expected = expected + '\n' + 'VALUES (?, ?);'
    test = run_sql.read_sql_file('src/sql/insert_van.sql')
    assert test == expected, 'The SQL script was not read correctly'


def test_execute_sql(mock_db_connection, reset_db):
    """Test the execute_sql function.

    Args:
        mock_db_connection: The mock connection
        reset_db: resets the database
    """
    sql_file = 'src/tests/resources/test_run_sql/test_insert.sql'
    run_sql.execute_sql(sql_file)

    conn = sqlite3.connect('vehicles.db')
    cursor = conn.cursor()

    sql_file = 'src/tests/resources/test_run_sql/test_select_car.sql'
    sql_file = run_sql.read_sql_file(sql_file)
    output = cursor.execute(sql_file, ('TE57ING',)).fetchone()

    conn.close()

    assert output[0] == 'TE57ING', 'SQL file not executed correctly'


def test_execute_sql_select(mock_db_connection, reset_db):
    """Test the execute_sql_select function.

    Args:
        mock_db_connection: The mock connection
        reset_db: resets the database
    """
    output = run_sql.execute_sql_select('src/sql/select_all_vehicles.sql')
    assert output[0][0] == 'HC56XPQ', 'SQL select not executed correctly'


def test_select_type_from_num_plate(mock_db_connection, reset_db):
    """Test the select type from num plate function.

    Args:
        mock_db_connection: The mock connection
        reset_db: resets the database
    """
    test_type = run_sql.select_type_from_num_plate('HC56XPQ')
    expected_type = 'car'

    assert test_type == expected_type, 'Incorrect type returned'


def test_select_based_on_type(mock_db_connection, reset_db):
    """Test the select based on type function.

    Args:
        mock_db_connection: The mock connection
        reset_db: resets the database
    """
    car = run_sql.select_based_on_type('car', 'HC56XPQ')
    van = run_sql.select_based_on_type('van', 'HC62XAC')
    lorry = run_sql.select_based_on_type('lorry', 'QS52BCG')

    error_text = 'Incorrect sql output returned'
    assert car[0][0] == 'red', error_text
    assert van[0][0] == 'white', error_text
    assert lorry[0][0] == 'blue', error_text


def test_insert_car_helper(mock_db_connection, reset_db):
    """Test the helper function for insert car into db.

    Args:
        mock_db_connection: The mock connection
        reset_db: resets the database
    """
    test_car_properties = ['TE57ING', None, None, None, None, 5]
    run_sql.insert_car(test_car_properties)

    sql_file_car = 'src/tests/resources/test_run_sql/test_select_car.sql'
    sql_file_car = run_sql.read_sql_file(sql_file_car)

    conn = sqlite3.connect('vehicles.db')
    cursor = conn.cursor()

    output_car = cursor.execute(sql_file_car, ('TE57ING',)).fetchone()

    assert output_car[1] == 5, 'Incorrect value inserted'


def test_insert_van_helper(mock_db_connection, reset_db):
    """Test the helper function for insert van into db.

    Args:
        mock_db_connection: The mock connection
        reset_db: resets the database
    """
    test_van_properties = ['TE57ING', None, None, None, None, 100]
    run_sql.insert_van(test_van_properties)

    sql_file_van = 'src/tests/resources/test_run_sql/test_select_van.sql'
    sql_file_van = run_sql.read_sql_file(sql_file_van)

    conn = sqlite3.connect('vehicles.db')
    cursor = conn.cursor()

    output_van = cursor.execute(sql_file_van, ('TE57ING',)).fetchone()

    assert output_van[1] == 100, 'Incorrect value inserted'


def test_insert_lorry_helper(mock_db_connection, reset_db):
    """Test the helper function for insert lorry into db.

    Args:
        mock_db_connection: The mock connection
        reset_db: resets the database
    """
    test_lorry_properties = ['TE57ING', None, None, None, None, 20000, 'day']
    run_sql.insert_lorry(test_lorry_properties)

    sql_file_lorry = 'src/tests/resources/test_run_sql/test_select_lorry.sql'
    sql_file_lorry = run_sql.read_sql_file(sql_file_lorry)

    conn = sqlite3.connect('vehicles.db')
    cursor = conn.cursor()

    output_lorry = cursor.execute(sql_file_lorry, ('TE57ING',)).fetchone()
    assert output_lorry[1] == 20000, 'Incorrect value inserted'


def test_insert_vehicle_into_db(mock_db_connection, reset_db):
    """Test the helper function for insert lorry into db.

    Also testing the integration with helper functions:
    insert_car, insert_van, insert_lorry

    Args:
        mock_db_connection: The mock connection
        reset_db: resets the database
    """
    test_properties_car = ['TE57ING', 'red', 'car', '2025-09-03', '2025-09-04', 5]
    test_properties_van = ['TE57INK', 'red', 'van', '2025-09-03', '2025-09-04', 10]
    test_properties_pickup = [
        'TE57INL',
        'red',
        'pickup',
        '2025-09-03',
        '2025-09-04',
        1000,
        'single',
        ]

    expected_values = ('TE57ING', 'TE57INK', 'TE57INL', 'red')
    run_sql.insert_vehicle_into_db(test_properties_car)
    run_sql.insert_vehicle_into_db(test_properties_van)
    run_sql.insert_vehicle_into_db(test_properties_pickup)

    output = run_sql.execute_sql_select('src/sql/select_all_vehicles.sql')
    error_text = 'insert incorrect'

    assert output[4][0] and output[4][2] in expected_values, error_text
    assert output[5][0] and output[5][2] in expected_values, error_text
    assert output[6][0] and output[6][2] in expected_values, error_text


def test_update_vehicle(mock_db_connection, reset_db):
    """Test the update vehicle function.

    Args:
        mock_db_connection: The mock connection
        reset_db: resets the database
    """
    test_car_values: dict = {
        'colour_id': 'green',
        'tax_due_date': False,
        'service_due_date': False,
        'extra1': 99,
        'cab_type': False,
    }

    test_lorry_values = {
        'colour_id': 'blue',
        'tax_due_date': False,
        'service_due_date': False,
        'extra1': 99,
        'cab_type': 'day',
    }

    test_pickup_values = {
        'colour_id': 'Silver',
        'tax_due_date': False,
        'service_due_date': False,
        'extra1': 99,
        'cab_type': 'single',
    }

    test_van_values: dict = {
        'colour_id': 'brown',
        'tax_due_date': '2025-04-03',
        'service_due_date': False,
        'extra1': 99,
        'cab_type': False,
    }

    run_sql.update_vehicle(test_car_values, 'car', 'HC56XPQ')
    run_sql.update_vehicle(test_van_values, 'van', 'HC62XAC')
    run_sql.update_vehicle(test_lorry_values, 'lorry', 'QS52BCG')
    run_sql.update_vehicle(test_pickup_values, 'pickup', 'BG70LKM')

    test_output = run_sql.execute_sql_select('src/sql/select_all_vehicles.sql')
    error_text = 'Details not correct for updated vehicle'

    assert test_output[0][2] == 'green', error_text
    assert test_output[1][2] == 'brown', error_text
    assert test_output[2][2] == 'blue', error_text
    assert test_output[3][2] == 'silver', error_text
