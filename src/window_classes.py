"""File of classes for bulding the GUI."""
import tkinter as tk
from abc import abstractmethod


class AbstractWindow:
    """An abstract class to provide a framework for other window classes."""

    _master = None
    _frame = None

    def __init__(self, master):
        """Init default method for GUI windows.

        Args:
            master (Tk): the Tk object used to build the GUI
        """
        self._master = master
        self._frame = tk.Frame(self._master)

    def close_windows(self):
        """Destroys a window."""
        self._master.destroy()

    @abstractmethod
    def build_window(self):
        """Build a window based on classes variable.

        Each class will have its own implementation this
        is an abstract method
        """
        pass


class MainWindow(AbstractWindow):
    """Class representing the main window."""

    _button1 = None

    def __init__(self, master):
        """Init class for main window.

        Args:
            master (Tk): the Tk object used to build the GUI
        """
        super().__init__(master)
        self._button1 = tk.Button(self._frame, text='New Window', width=25, 
                                  command=self.new_window)

    def new_window(self):
        """Initialise new window when button is clicked."""
        self.newWindow = tk.Toplevel(self._master)
        self.app = Window2(self.newWindow)
        self.app.build_window()

    def build_window(self):
        """Build main menu window from private variables."""
        self._button1.pack()
        self._frame.pack()


class Window2(AbstractWindow):
    """Class representing secondary window."""

    _quit_button = None

    def __init__(self, master):
        """Init class for this window.

        Args:
            master (Tk): the Tk object used to build the window
        """
        super().__init__(master)
        self._quit_button = tk.Button(self._frame, text='Quit', width=25, 
                                      command=self.close_windows)

    def build_window(self):
        """Build this window from private variables."""
        self._quit_button.pack()
        self._frame.pack()


def main():
    """Initialise GUI."""
    root = tk.Tk()
    app = MainWindow(root)
    app.build_window()
    root.mainloop()


if __name__ == '__main__':
    main()
