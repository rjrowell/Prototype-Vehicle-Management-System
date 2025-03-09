"""Run the prototype program."""
import os
import sys
import tkinter as tk

import src.database_setup as db_setup
from src.window_classes import MainWindow

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)


def main():
    """Initialise GUI."""
    #############
    # Reset DB
    db_setup.main()
    #############
    root = tk.Tk()
    app = MainWindow(root)
    app.build_window()
    root.mainloop()


if __name__ == '__main__':
    main()
