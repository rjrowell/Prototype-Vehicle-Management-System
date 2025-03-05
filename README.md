# Yuma Vehicle Manager, Demonstration Application
## Student ID: 730096317

### Python Version:
To run this application please use Python version 3.10+. The reccomended version for this application is version 3.12.2
> Note: on macOS there is a known issue in Tkinter where text fails to load on older versions of python3,
> if you start the application and text is not loading correctly please use the reccomeneded version of python.

### Installing libraries:
This application makes use of Tkinter (For GUI), Flake8 (Linting) and PyTest (Unit testing), 
the final two can be installed through pip by issuing this command from a terminal:
```pip install flake8 pytest pytest-mock```
> Since Tkinter is not available through pip please ensure it is correctly installed in your python installation

### Starting the App:
To start the application run the file `main.py`. This will reset the db then open the application
> If you do not wish for the database to be reset to it's demo state before starting the app,
> you can easily remove the code by editing the main.py file - The code is surronded by the comment 'Reset DB'

#### Main Window:
Once started the app will open it's main window:


This contains all the 
