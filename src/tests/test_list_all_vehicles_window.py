"""Tests the list all vehicles window class."""
import tkinter as tk

from ..window_classes import ListAllvehicles

window_instance = ListAllvehicles(tk.Tk())

window_widgets = [
    window_instance._title,
    window_instance._text,
    window_instance._quit_button,
]


def test_widgets():
    """Test that all widgets were created correctly."""
    assert window_widgets[0].cget('text') == 'All Vehicles in the Fleet'
    assert window_widgets[1].cget('height') == 5
    assert window_widgets[2].cget('text') == 'Exit'


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
    monkeypatch.setattr(window_instance._quit_button, 'pack', mock_pack)
    monkeypatch.setattr(window_instance._frame, 'pack', mock_pack)
    window_instance.build_window()

    assert len(pack_calls) == 4