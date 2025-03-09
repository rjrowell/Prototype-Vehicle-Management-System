"""Tests the main window window class."""
import pytest
import tkinter as tk

from ..window_classes import MainWindow

main_window_instance = MainWindow(tk.Tk())

window_widgets = [
    main_window_instance._title,
    main_window_instance._button1,
    main_window_instance._button2,
    main_window_instance._button3,
    main_window_instance._button4,
    main_window_instance._button5,
    main_window_instance._button6,
    main_window_instance._button7,
]


def original_set_next_function(name: str):
    """Provide the original set next function to avoid recursion.

    Args:
        name (str): the name of the next window
    """
    main_window_instance.set_next_window(name)


def test_widgets():
    """Test that all widgets were created correctly."""
    expected_width = 25
    for widget in window_widgets:
        assert widget.cget('width') == expected_width


def test_build_window(monkeypatch):
    """Test that the build window function works correctly.

    Args:
        monkeypatch: library to allow patching of pack function
    """
    pack_calls = []

    def mock_pack():
        pack_calls.append(True)

    monkeypatch.setattr(main_window_instance._title, 'pack', mock_pack)
    monkeypatch.setattr(main_window_instance._button1, 'pack', mock_pack)
    monkeypatch.setattr(main_window_instance._button2, 'pack', mock_pack)
    monkeypatch.setattr(main_window_instance._button3, 'pack', mock_pack)
    monkeypatch.setattr(main_window_instance._button4, 'pack', mock_pack)
    monkeypatch.setattr(main_window_instance._button5, 'pack', mock_pack)
    monkeypatch.setattr(main_window_instance._button6, 'pack', mock_pack)
    monkeypatch.setattr(main_window_instance._button7, 'pack', mock_pack)
    monkeypatch.setattr(main_window_instance._frame, 'pack', mock_pack)

    main_window_instance.build_window()
    assert len(pack_calls) == 9


def test_next_window_function(monkeypatch):
    """Test the functions that build the next windows.

    Args:
        monkeypatch: library to allow patching of set next window function
    """
    window_name_list: list[str] = [
        'ListAllvehicles',
        'VehiclesWithTaxDue',
        'VehiclesWithServiceDue',
        'SearchByNumberPlate',
        'InsertVehicle',
        'UpdateVehicle',
        'RemoveVehicle',
    ]

    test_names_list: list[str] = []

    build_calls = []

    # Patch the set next window function and build window function
    # Set adds the name of next window to a list, we can check is as expected
    def patch_set(name):
        """Patch the set next window function.

        Args:
            name: the name of the window being called

        Returns:
            app: the next window as a class
        """
        test_names_list.append(name)
        return main_window_instance

    def mock_build():
        build_calls.append(True)

    monkeypatch.setattr(main_window_instance, 'set_next_window', patch_set)
    monkeypatch.setattr(main_window_instance, 'build_window', mock_build)

    main_window_instance.all_vehicles_window()
    main_window_instance.tax_due_window()
    main_window_instance.service_due_window()
    main_window_instance.num_plate_search_window()
    main_window_instance.insert_new_vehicle_window()
    main_window_instance.update_vehicle_window()
    main_window_instance.remove_vehicle_window()

    assert window_name_list == test_names_list
    assert len(build_calls) == 7
