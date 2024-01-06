import random
import tkinter as tk
from tkinter import Label, Entry, Button, StringVar

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    nr_letters = int(entry_letters_var.get())
    nr_symbols = int(entry_symbols_var.get())
    nr_numbers = int(entry_numbers_var.get())

    password_list = []

    for char in range(1, nr_letters + 1):
        password_list.append(random.choice(letters))

    for char in range(1, nr_symbols + 1):
        password_list += random.choice(symbols)

    for char in range(1, nr_numbers + 1):
        password_list += random.choice(numbers)

    random.shuffle(password_list)
    generated_password = ''.join(password_list)
    result_label.config(text=f"Your password is: {generated_password}", fg='white', bg='green')  # Set text and background color
    copy_button.config(state=tk.NORMAL)  # Enable the copy button

def copy_to_clipboard():
    generated_password = result_label.cget("text").split(": ")[1]
    window.clipboard_clear()
    window.clipboard_append(generated_password)
    window.update()

# Create the main window
window = tk.Tk()
window.title("PyPassword Generator")
window.geometry("500x400")

# Set background color for the entire window
window.configure(bg='lightblue')

# Create and place the labels, entry widgets, and button with larger font size
Label(window, text="How many letters would you like in your password?", font=('Helvetica', 14), bg='lightblue').pack(pady=10)
entry_letters_var = StringVar()
entry_letters = Entry(window, textvariable=entry_letters_var, font=('Helvetica', 12), width=30, bg='lightyellow')
entry_letters.pack(pady=5)

Label(window, text="How many symbols would you like?", font=('Helvetica', 14), bg='lightblue').pack(pady=10)
entry_symbols_var = StringVar()
entry_symbols = Entry(window, textvariable=entry_symbols_var, font=('Helvetica', 12), width=30, bg='lightyellow')
entry_symbols.pack(pady=5)

Label(window, text="How many numbers would you like?", font=('Helvetica', 14), bg='lightblue').pack(pady=10)
entry_numbers_var = StringVar()
entry_numbers = Entry(window, textvariable=entry_numbers_var, font=('Helvetica', 12), width=30, bg='lightyellow')
entry_numbers.pack(pady=5)

Button(window, text="Generate Password", command=generate_password, font=('Helvetica', 14), bg='orange', fg='white').pack(pady=20)

# Create a label to display the generated password
result_label = Label(window, text="", font=('Helvetica', 14), bg='lightblue')
result_label.pack()

# Create a button to copy the password to clipboard
copy_button = Button(window, text="Copy to Clipboard", command=copy_to_clipboard, font=('Helvetica', 14), bg='blue', fg='white', state=tk.DISABLED)
copy_button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
