"""File of classes representing the windows of the TK GUI.

The windows have been programmed in an object oriented way,
each window of the GUI inherits from the abstract window class.

This is an abstract class which provides a framework and base settings
for each other GUI window.
"""
import tkinter as tk
from sqlite3 import IntegrityError
from abc import abstractmethod

from .utils import build_classes as bc
from .utils import window_scripts as ws


class AbstractWindow(object):
    """An abstract class to provide a framework for other window classes."""

    _exit_string = 'Exit'
    _enter_string = 'Enter'
    _default_width: int = 25
    _title_width: int = 35
    _title: tk.Label = None
    _text: tk.Text = None

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

    def set_next_window(self, window_name: str):
        """Set the next window to be displayed.

        Args:
            window_name(str): The name of the window to be set

        Returns:
            app(object): The next window to be displayed

        """
        class_mapping = {
            'SearchByNumberPlate': SearchByNumberPlate,
            'ListAllvehicles': ListAllvehicles,
            'VehiclesWithTaxDue': VehiclesWithTaxDue,
            'VehiclesWithServiceDue': VehiclesWithServiceDue,
            'InsertVehicle': InsertVehicle,
            'UpdateVehicle': UpdateVehicle,
            'RemoveVehicle': RemoveVehicle,
        }

        self.newWindow = tk.Toplevel(self._master)
        self.app = class_mapping[window_name](self.newWindow)

        return self.app

    def process_text(self) -> str:
        """Get text from a text field.

        Returns:
            text_out(str): The text from the windows text field

        """
        return self._text.get('1.0', tk.END).strip()

    @abstractmethod
    def build_window(self):
        """Build a window based on classes variable.

        Each class will have its own implementation this
        is an abstract method
        """
        raise NotImplementedError('This method should be implemented')


class MainWindow(AbstractWindow):
    """Class representing the main window."""

    def __init__(self, root: tk.Tk):
        """Init class for main window.

        Args:
            root (Tk): the Tk object used to build the GUI

        """
        super().__init__(root)
        self._title = tk.Label(
            self._frame,
            text='Main Menu',
            width=self._default_width,
        )
        self._button1 = tk.Button(
            self._frame,
            text='Search By Number Plate',
            width=self._default_width,
            command=self.num_plate_search_window,
        )
        self._button2 = tk.Button(
            self._frame,
            text='List All vehicles',
            width=self._default_width,
            command=self.all_vehicles_window,
        )
        self._button3 = tk.Button(
            self._frame,
            text='Vehicles With Tax Due',
            width=self._default_width,
            command=self.tax_due_window,
        )
        self._button4 = tk.Button(
            self._frame,
            text='Vehicles With Service Due',
            width=self._default_width,
            command=self.service_due_window,
        )
        self._button5 = tk.Button(
            self._frame,
            text='Update Vehicle',
            width=self._default_width,
            command=self.update_vehicle_window,
        )
        self._button6 = tk.Button(
            self._frame,
            text='Insert New Vehicle',
            width=self._default_width,
            command=self.insert_new_vehicle_window,
        )
        self._button7 = tk.Button(
            self._frame,
            text='Remove Vehicle',
            width=self._default_width,
            command=self.remove_vehicle_window,
        )

    def all_vehicles_window(self):
        """Initialise new window when button is clicked."""
        self.app = self.set_next_window('ListAllvehicles')
        self.app.build_window()

    def tax_due_window(self):
        """Initialise new window when button is clicked."""
        self.app = self.set_next_window('VehiclesWithTaxDue')
        self.app.build_window()

    def service_due_window(self):
        """Initialise new window when button is clicked."""
        self.app = self.set_next_window('VehiclesWithServiceDue')
        self.app.build_window()

    def num_plate_search_window(self):
        """Initialise a search by num plate window."""
        self.app = self.set_next_window('SearchByNumberPlate')
        self.app.build_window()

    def insert_new_vehicle_window(self):
        """Initialise a search by insert vehicle window."""
        self.app = self.set_next_window('InsertVehicle')
        self.app.build_window()

    def update_vehicle_window(self):
        """Initialise an update vehicle window."""
        self.app = self.set_next_window('UpdateVehicle')
        self.app.build_window()

    def remove_vehicle_window(self):
        """Initialise a remove vehicle window."""
        self.app = self.set_next_window('RemoveVehicle')
        self.app.build_window()

    def build_window(self):
        """Build main menu window from private variables."""
        self._title.pack()
        self._button1.pack()
        self._button2.pack()
        self._button3.pack()
        self._button4.pack()
        self._button5.pack()
        self._button6.pack()
        self._button7.pack()
        self._frame.pack()


class ListAllvehicles(AbstractWindow):
    """Class representing secondary window."""

    def __init__(self, master: tk.Tk):
        """Init class for List all vehicles window.

        Args:
            master (Tk): the Tk object used to build the window

        """
        super().__init__(master)
        self._title = tk.Label(
            self._frame,
            text='All Vehicles in the Fleet',
            width=self._default_width,
        )
        self._text = tk.Text(self._frame, width=self._default_width, height=5)
        self._quit_button = tk.Button(
            self._frame,
            text=self._exit_string,
            width=self._default_width,
            command=self.close_windows,
        )

    def build_window(self):
        """Build list all window from private variables."""
        vehicles_list = bc.build_classes(
            'src/sql/select_all_vehicles.sql',
            'all_vehicles',
        )
        self._text = ws.get_text_to_display(self._text, vehicles_list)
        self._title.pack()
        self._text.pack()
        self._quit_button.pack()
        self._frame.pack()


class VehiclesWithTaxDue(AbstractWindow):
    """Class representing Vehicles With Tax Due window."""

    _text_width = 45

    def __init__(self, master: tk.Tk):
        """Init class for tax due window.

        Args:
            master (Tk): the Tk object used to build the window

        """
        super().__init__(master)
        self._title = tk.Label(
            self._frame,
            text='Vehicles With Tax Due in the Next Month',
            width=self._title_width,
        )
        self._text = tk.Text(self._frame, width=self._text_width, height=5)
        self._quit_button = tk.Button(
            self._frame,
            text=self._exit_string,
            width=self._default_width,
            command=self.close_windows,
        )

    def build_window(self):
        """Build tax due window from private variables."""
        vehicles_list = bc.build_classes(
            'src/sql/select_tax_due_vehicles.sql',
            'tax_due',
        )
        self._text = ws.get_text_to_display(self._text, vehicles_list)
        self._title.pack()
        self._text.pack()
        self._quit_button.pack()
        self._frame.pack()


class VehiclesWithServiceDue(AbstractWindow):
    """Class representing Vehicles With Service Due window."""

    _text_width = 55

    def __init__(self, master: tk.Tk):
        """Init class for service due window.

        Args:
            master (Tk): the Tk object used to build the window

        """
        super().__init__(master)
        title_text = 'Vehicles with Services Due in the Next Month'
        self._title = tk.Label(
            self._frame,
            text=title_text,
            width=self._title_width,
        )
        self._text = tk.Text(self._frame, width=self._text_width, height=5)
        self._quit_button = tk.Button(
            self._frame,
            text=self._exit_string,
            width=self._default_width,
            command=self.close_windows,
        )

    def build_window(self):
        """Build service due window from private variables."""
        vehicles_list = bc.build_classes(
            'src/sql/select_service_due_vehicles.sql',
            'service_due',
        )
        self._text = ws.get_text_to_display(self._text, vehicles_list)
        self._title.pack()
        self._text.pack()
        self._quit_button.pack()
        self._frame.pack()


class SearchByNumberPlate(AbstractWindow):
    """Class representing Vehicles With Service Due window."""

    _text_width = 55

    def __init__(self, master: tk.Tk):
        """Init class for search by number plate window.

        Args:
            master (Tk): the Tk object used to build the window

        """
        super().__init__(master)
        title_text = 'Please Enter a Vehicle Number Plate:'
        self._title = tk.Label(
            self._frame,
            text=title_text,
            width=self._title_width,
        )
        self._text = tk.Text(self._frame, width=self._text_width, height=1)
        self._enter_button = tk.Button(
            self._frame,
            text=self._enter_string,
            width=self._default_width,
            command=self.submit_text,
        )
        self._quit_button = tk.Button(
            self._frame,
            text=self._exit_string,
            width=self._default_width,
            command=self.close_windows,
        )

    def submit_text(self):
        """Run logic when enter button is pressed."""
        self._num_plate_to_search: str = self.process_text()
        extened_text_width: int = 105
        try:
            vehicles_list = bc.build_classes(
                self._num_plate_to_search,
                'num_plate',
            )
        except TypeError:
            error_text = 'No Vehicle found, Please enter a Valid Number Plate'
            self._title.config(text=error_text)
            self._text.config(width=self._text_width)

            self._title.pack()
            self._text.pack()
        else:
            self._text.config(width=extened_text_width)
            self._text = ws.get_text_to_display(self._text, vehicles_list)

            self._title.config(text='Number Plate Found:')

            self._title.pack()
            self._text.pack()

    def build_window(self):
        """Build number plate search window from private variables."""
        self._title.pack()
        self._text.pack()
        self._enter_button.pack()
        self._quit_button.pack()
        self._frame.pack()


class InsertVehicle(AbstractWindow):
    """Class representing Insert New Vehicle window."""

    def __init__(self, master: tk.Tk):
        """Init class for insert vehicle window.

        Args:
            master (Tk): the Tk object used to build the window

        """
        super().__init__(master)
        self.selected_value = tk.StringVar(self._frame)
        # Default value for dropdown
        self.selected_value.set('Select type of Vehicle to insert')

        self._options = ['Car', 'Van', 'Lorry', 'Pickup']
        self._option_menu = tk.OptionMenu(
            self._frame,
            self.selected_value,
            *self._options,
        )
        self._enter_button = tk.Button(
            self._frame,
            text=self._enter_string,
            width=self._default_width,
            command=self._submit_type,
        )
        self._quit_button = tk.Button(
            self._frame,
            text=self._exit_string,
            width=self._default_width,
            command=self.close_windows,
        )

    def build_window(self):
        """Build insert vehicle window from private variables."""
        self._option_menu.pack()
        self._enter_button.pack()
        self._quit_button.pack()
        self._frame.pack()

    def _submit_type(self):
        """Do actions after vehicle type is submitted.

        Generates next set of widgets

        Returns:
            bool: Returns true or false depending on if it completed
        """
        accepted_types = ['Car', 'Van', 'Lorry', 'Pickup']
        self._vehicle_type = self.selected_value.get()

        # Check if a type has been selected
        if self._vehicle_type in accepted_types:
            self._option_menu.destroy()
            self._enter_button.config(command=self._insert_text)
            self._enter_button.pack()

            # Generate elements for next window
            self._element_list: list = ws.generate_insert_widgets(
                self._frame,
                self._vehicle_type,
            )

            for inc in self._element_list:
                inc.pack()

            return True
        return False

    def _insert_text(self):
        try:
            ws.insert_values(self._element_list, self._vehicle_type)
        except TypeError:
            label_text = 'One or more entries is incorrect please re-enter'
            self._element_list[0].config(text=label_text)
        except KeyError:
            label_text = 'Ivalid colour entered'
            self._element_list[0].config(text=label_text)
        except IntegrityError:
            label_text = 'Vehicle with entered number plate already exists'
            self._element_list[0].config(text=label_text)
        else:
            self.close_windows()


class UpdateVehicle(AbstractWindow):
    """Class representing Update Vehicle window."""

    _text_width = 55

    def __init__(self, master: tk.Tk):
        """Init class for this window.

        Args:
            master (Tk): the Tk object used to build the window
        """
        super().__init__(master)
        title_text = 'Please Enter Number Plate of Vehicle to Update:'
        self._title = tk.Label(
            self._frame,
            text=title_text,
            width=self._title_width,
        )
        self._text = tk.Text(self._frame, width=self._text_width, height=1)
        self._enter_button = tk.Button(
            self._frame,
            text=self._enter_string,
            width=self._default_width,
            command=self._submit_text,
        )
        self._quit_button = tk.Button(
            self._frame,
            text=self._exit_string,
            width=self._default_width,
            command=self.close_windows,
        )

    def build_window(self):
        """Build update vehicle window from private variables."""
        self._title.pack()
        self._text.pack()
        self._enter_button.pack()
        self._quit_button.pack()
        self._frame.pack()

    def _submit_text(self):
        """Run the logic to get the vehicle type based on num plate entered."""
        self._number_plate = self.process_text()
        try:
            self._widgets: list = ws.get_update_widgets_from_plate(
                self._frame,
                self._number_plate,
            )
        except TypeError:
            error_text = 'No Vehicle found, Please enter a Valid Number Plate'
            self._title.config(text=error_text)
            self._text.config(width=self._text_width)
            self._title.pack()
            self._text.pack()
        else:
            self._widgets = self._widgets[:1] + self._widgets[2:]
            for inc in self._widgets:
                inc.pack()
            self._enter_button.config(command=self._submit_info)
            self._text.destroy()
            self._title.destroy()

    def _submit_info(self):
        if ws.update_changed_values(self._widgets, self._number_plate):
            self.close_windows()
        else:
            self._widgets[0].config(text='No Valid Options Set')
            self._widgets[0].pack()


class RemoveVehicle(AbstractWindow):
    """Window for removing a vehicle from db."""

    _text_width = 55

    def __init__(self, master: tk.Tk):
        """Init class for the vehicle removal window.

        Args:
            master (Tk): the Tk object used to build the window
        """
        super().__init__(master)
        title_text = 'Please Enter Number Plate of Vehicle to Remove:'
        self._title = tk.Label(
            self._frame,
            text=title_text,
            width=self._title_width,
        )
        self._text = tk.Text(self._frame, width=self._text_width, height=1)
        self._enter_button = tk.Button(
            self._frame,
            text=self._enter_string,
            width=self._default_width,
            command=self._submit_text,
        )
        self._quit_button = tk.Button(
            self._frame,
            text=self._exit_string,
            width=self._default_width,
            command=self.close_windows,
        )

    def build_window(self):
        """Build update vehicle window from private variables."""
        self._title.pack()
        self._text.pack()
        self._enter_button.pack()
        self._quit_button.pack()
        self._frame.pack()

    def _submit_text(self):
        """Remove the vehicle type with the num plate entered."""
        self._number_plate = self.process_text()
        try:
            ws.remove_vehicle_from_db(self._number_plate)
        except TypeError:
            self._title.config(text='Invalid Number Plate Entered')
            self._title.pack()
        else:
            self.close_windows()
