"""File of classes for bulding the GUI."""
import tkinter as tk
from abc import abstractmethod


class AbstractWindow:
    """An abstract class to provide a framework for other window classes."""

    _master: object = None
    _frame: object = None

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

    _button1: object = None
    _button2: object = None

    def __init__(self, master):
        """Init class for main window.

        Args:
            master (Tk): the Tk object used to build the GUI
        """
        super().__init__(master)
        self._button1 = tk.Button(self._frame, text='Search By Number Plate', 
                                  width=25, 
                                  command=self.all_viechles_window)
        self._button2 = tk.Button(self._frame, text='List All Veichles', 
                                  width=25, 
                                  command=self.all_viechles_window)
        self._button3 = tk.Button(self._frame,
                                  text='Veichles With Tax Due', 
                                  width=25, 
                                  command=self.all_viechles_window)
        self._button4 = tk.Button(self._frame,
                                  text='Veichles With Service Due', 
                                  width=25, 
                                  command=self.all_viechles_window)
        self._button5 = tk.Button(self._frame,
                                  text='List Veichles By Fuel Type', 
                                  width=25, 
                                  command=self.all_viechles_window)

    def all_viechles_window(self):
        """Initialise new window when button is clicked."""
        self.newWindow = tk.Toplevel(self._master)
        self.app = ListAllVeichles(self.newWindow)
        self.app.build_window()

    def build_window(self):
        """Build main menu window from private variables."""
        self._button1.pack()
        self._button2.pack()
        self._button3.pack()
        self._button4.pack()
        self._button5.pack()
        self._frame.pack()


class ListAllVeichles(AbstractWindow):
    """Class representing secondary window."""

    _text: object = None
    _quit_button: object = None

    def __init__(self, master):
        """Init class for this window.

        Args:
            master (Tk): the Tk object used to build the window
        """
        super().__init__(master)
        self._text = tk.Text(self._frame, width=25, height=1)
        self._quit_button = tk.Button(self._frame, text='Exit', width=25, 
                                      command=self.close_windows)

    def build_window(self):
        """Build this window from private variables."""
        self._text.insert(tk.END, 'Test')
        self._text.pack()
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
