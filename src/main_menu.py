import tkinter as tk

root = tk.Tk()

def main():
    create_main_window()
    create_label()
    create_button()
    create_exit_button()
    root.mainloop()

def on_button_click():
    new_window = tk.Toplevel(root)  # Creates a new top-level window
    new_window.title("New Window")
    new_window.geometry("300x200")

    label = tk.Label(new_window, text="Welcome to the New Window!", font=("Arial", 12))
    label.grid(row=0, column=0, padx=20, pady=10)

    back_button = tk.Button(new_window, text="Back", command=new_window.destroy)  # Close new window
    back_button.grid(row=1, column=0, padx=0, pady=10)

def create_main_window():
    root.title("Tkinter Button Example")
    root.geometry("300x200")

def create_label():
    label = tk.Label(root, text="Click the button", font=("Arial", 12))
    label.grid(row=0, column=0, padx=20, pady=0)

def create_button():
    button = tk.Button(root, text="Click Me", command=on_button_click)
    button.grid(row=1, column=0, padx=0, pady=10)

def create_exit_button():
    exit_button = tk.Button(root, text="Exit", command=root.quit)
    exit_button.grid(row=2, column=0, padx=10, pady=10)

if __name__ == '__main__':
    main()
