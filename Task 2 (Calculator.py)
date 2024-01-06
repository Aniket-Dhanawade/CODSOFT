import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        messagebox.showerror("Error", "Cannot divide by zero.")
        return None

def click_button(value):
    current_text = entry_var.get()
    if current_text == 'Error':
        entry_var.set(value)
    else:
        entry_var.set(current_text + value)

def clear_entry():
    entry_var.set("")

def backspace():
    current_text = entry_var.get()
    entry_var.set(current_text[:-1])

def square():
    try:
        expression = entry_var.get()
        result = eval(expression) ** 2
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

def square_root():
    try:
        expression = entry_var.get()
        result = eval(expression) ** 0.5
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

def calculate():
    expression = entry_var.get()
    try:
        result = eval(expression)
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")

# Entry widget for display
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=('Helvetica', 14), justify='right')
entry.grid(row=0, column=0, columnspan=6, ipadx=8, ipady=8)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'AC', '⌫', 'x²', '√'
]

# Button creation and layout
row_val = 1
col_val = 0

for button in buttons:
    if button == 'AC':
        tk.Button(root, text=button, padx=20, pady=20, font=('Helvetica', 12), command=clear_entry).grid(row=row_val, column=col_val)
    elif button == '⌫':
        tk.Button(root, text=button, padx=20, pady=20, font=('Helvetica', 12), command=backspace).grid(row=row_val, column=col_val)
    elif button == 'x²':
        tk.Button(root, text=button, padx=20, pady=20, font=('Helvetica', 12), command=square).grid(row=row_val, column=col_val)
    elif button == '√':
        tk.Button(root, text=button, padx=20, pady=20, font=('Helvetica', 12), command=square_root).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=('Helvetica', 12), command=lambda btn=button: click_button(btn) if btn != '=' else calculate()).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the GUI
root.mainloop()
