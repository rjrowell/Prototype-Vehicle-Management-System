"""Run the prototype program."""
import tkinter as tk

import src.database_setup as db_setup
from src.window_classes import MainWindow


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
