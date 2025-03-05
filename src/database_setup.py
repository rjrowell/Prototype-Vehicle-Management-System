"""Script that setups the prototype database."""
from .utils import execute_sql


def main():
    """Drop tables then creates the new prototype db."""
    drop_tables()
    create_tables()
    insert_into()


def drop_tables():
    """Execute drop_tables.sql."""
    execute_sql('src/sql/drop_tables.sql')


def create_tables():
    """Execute create_tables.sql."""
    execute_sql('src/sql/create_tables.sql')


def insert_into():
    """Execute insert_into_tables.sql."""
    execute_sql('src/sql/insert_into_tables.sql')


if __name__ == '__main__':
    main()
