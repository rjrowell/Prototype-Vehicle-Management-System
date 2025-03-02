"""Package to define utilities."""
from .run_sql import (
           execute_sql,
           execute_sql_select,
           insert_vehicle_into_db,
           select_type_from_num_plate,
)
from .window_scripts import build_classes, get_text_to_display

__all__ = ['execute_sql', 'execute_sql_select', 'build_classes',
           'get_text_to_display', 'select_type_from_num_plate',
           'insert_vehicle_into_db']
