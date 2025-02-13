"""File of classes for bulding the GUI."""
import tkinter as tk
from abc import abstractmethod
from utils import window_scripts as ws


class AbstractWindow:
    """An abstract class to provide a framework for other window classes."""

    _master: object = None
    _frame: object = None
    _title: object = None

    def __init__(self, master: tk.Tk):
        """Init default method for GUI windows.

        Args:
            master (Tk): the Tk object used to build the GUI
        """
        self._master = master
        self._frame = tk.Frame(self._master)
        master.title('Yuma Council Vehicle Manager')

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

    def __init__(self, master: tk.Tk):
        """Init class for main window.

        Args:
            master (Tk): the Tk object used to build the GUI
        """
        super().__init__(master)
        self._title = tk.Label(self._frame, text='Main Menu', width=25)
        self._button1 = tk.Button(self._frame, text='Search By Number Plate', 
                                  width=25, 
                                  command=self.all_vehicles_window)
        self._button2 = tk.Button(self._frame, text='List All vehicles', 
                                  width=25, 
                                  command=self.all_vehicles_window)
        self._button6 = tk.Button(self._frame,
                                  text='Search By Vehicle Type', 
                                  width=25, 
                                  command=self.all_vehicles_window)
        self._button3 = tk.Button(self._frame,
                                  text='Vehicles With Tax Due', 
                                  width=25, 
                                  command=self.tax_due_window)
        self._button4 = tk.Button(self._frame,
                                  text='Vehicles With Service Due', 
                                  width=25, 
                                  command=self.service_due_window)
        self._button5 = tk.Button(self._frame,
                                  text='Update Vehicle', 
                                  width=25, 
                                  command=self.all_vehicles_window)
        self._button6 = tk.Button(self._frame,
                                  text='Insert New Vehicle', 
                                  width=25, 
                                  command=self.all_vehicles_window)

    def all_vehicles_window(self):
        """Initialise new window when button is clicked."""
        self.newWindow = tk.Toplevel(self._master)
        self.app = ListAllvehicles(self.newWindow)
        self.app.build_window()

    def tax_due_window(self):
        """Initialise new window when button is clicked."""
        self.newWindow = tk.Toplevel(self._master)
        self.app = VehiclesWithTaxDue(self.newWindow)
        self.app.build_window()

    def service_due_window(self):
        """Initialise new window when button is clicked."""
        self.newWindow = tk.Toplevel(self._master)
        self.app = VehiclesWithServiceDue(self.newWindow)
        self.app.build_window()

    def build_window(self):
        """Build main menu window from private variables."""
        self._title.pack()
        self._button1.pack()
        self._button2.pack()
        self._button3.pack()
        self._button4.pack()
        self._button5.pack()
        self._frame.pack()


class ListAllvehicles(AbstractWindow):
    """Class representing secondary window."""

    _text: object = None
    _quit_button: object = None

    def __init__(self, master: tk.Tk):
        """Init class for this window.

        Args:
            master (Tk): the Tk object used to build the window
        """
        super().__init__(master)
        self._title = tk.Label(self._frame, text='All Vehicles in the Fleet',
                               width=25)
        self._text = tk.Text(self._frame, width=25, height=5)
        self._quit_button = tk.Button(self._frame, text='Exit', width=25, 
                                      command=self.close_windows)

    def build_window(self):
        """Build this window from private variables."""
        vehicles_list = ws.build_classes('src/sql/select_all_vehicles.sql',
                                         'all_vehicles')
        self._text = ws.get_text_to_display(self._text, vehicles_list)
        self._title.pack()
        self._text.pack()
        self._quit_button.pack()
        self._frame.pack()


class VehiclesWithTaxDue(AbstractWindow):
    """Class representing Vehicles With Tax Due window."""

    _text: object = None
    _quit_button: object = None

    def __init__(self, master: tk.Tk):
        """Init class for this window.

        Args:
            master (Tk): the Tk object used to build the window
        """
        super().__init__(master)
        self._title = tk.Label(self._frame, 
                               text='Vehicles With Tax Due in the Next Month',
                               width=35)
        self._text = tk.Text(self._frame, width=45, height=5)
        self._quit_button = tk.Button(self._frame, text='Exit', width=25, 
                                      command=self.close_windows)

    def build_window(self):
        """Build this window from private variables."""
        vehicles_list = ws.build_classes('src/sql/select_tax_due_vehicles.sql',
                                         'tax_due')
        self._text = ws.get_text_to_display(self._text, vehicles_list)
        self._title.pack()
        self._text.pack()
        self._quit_button.pack()
        self._frame.pack()


class VehiclesWithServiceDue(AbstractWindow):
    """Class representing Vehicles With Service Due window."""

    _text: object = None
    _quit_button: object = None

    def __init__(self, master: tk.Tk):
        """Init class for this window.

        Args:
            master (Tk): the Tk object used to build the window
        """
        super().__init__(master)
        title_text = 'Vehicles with Services Due in the Next Month'
        self._title = tk.Label(self._frame, text=title_text, width=35)
        self._text = tk.Text(self._frame, width=55, height=5)
        self._quit_button = tk.Button(self._frame, text='Exit', width=25, 
                                      command=self.close_windows)

    def build_window(self):
        """Build this window from private variables."""
        vehicles_list = ws.build_classes(
            'src/sql/select_service_due_vehicles.sql',
            'service_due')
        self._text = ws.get_text_to_display(self._text, vehicles_list)
        self._title.pack()
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
