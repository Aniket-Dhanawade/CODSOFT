import tkinter as tk
from tkcalendar import Calendar

# Create main window with visual enhancements
root = tk.Tk()
root.title("Student To-Do List")
root.geometry("400x400")
root.configure(bg="gray")  # gray background

# Task list using Text widget with wrapping enabled (read-only)
task_listbox = tk.Text(root, width=50, height=15, wrap=tk.WORD, bg="#f0f8ff", state=tk.DISABLED)
task_listbox.pack(pady=10)

# Colorful title label
title_label = tk.Label(root, text="Student To-Do List", font=("Arial", 20), bg="#333333", fg="#3498db")
title_label.pack(pady=20)

# Input fields and labels with consistent formatting
task_label = tk.Label(root, text="Enter task:", font=("Arial", 12), bg="#333333", fg="white")
task_label.pack()

task_entry = tk.Entry(root, width=40)
task_entry.pack()

# Define the selected_date variable
selected_date = tk.StringVar()

# Radio button for daily tasks
daily_radio = tk.Radiobutton(root, text="Daily Task", variable=selected_date, value="Daily", bg="#333333", fg="white")
daily_radio.pack()

# Calendar section with border
calendar_frame = tk.Frame(root, bg="#333333", borderwidth=1, relief="solid")
calendar_frame.pack(pady=10)

calendar_label = tk.Label(calendar_frame, text="Select Date:", font=("Arial", 12), bg="#333333", fg="white")
calendar_label.pack()

calendar_widget = Calendar(calendar_frame, selectmode="day", year=2023, month=12, day=25)
calendar_widget.pack()

def grab_date():
    global selected_date
    selected_date.set(calendar_widget.get_date())

choose_date_button = tk.Button(root, text="Choose Date", command=grab_date, bg="#3498db", fg="white")
choose_date_button.pack()

# Define functions before using them in button creation
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.configure(state=tk.NORMAL)  # Enable editing temporarily
        task_listbox.insert(tk.END, f"{task} - {selected_date.get()}\n")  # Add newline for separation
        task_listbox.configure(state=tk.DISABLED)  # Set back to read-only
        task_entry.delete(0, tk.END)
    else:
        tk.messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    # Adjust to use Text widget methods for selection and deletion
    try:
        start = task_listbox.index("sel.first")
        end = task_listbox.index("sel.last")
        task_listbox.configure(state=tk.NORMAL)  # Enable editing temporarily
        task_listbox.delete(start, end)
        task_listbox.configure(state=tk.DISABLED)  # Set back to read-only
    except tk.TclError:  # Handle no selection
        tk.messagebox.showwarning("Warning", "Please select a task to delete.")

# Use a frame for horizontal layout with padding
button_frame = tk.Frame(root, pady=10)
button_frame.pack()

add_button = tk.Button(button_frame, text="Add Task", command=add_task, bg="#3498db", fg="white")
add_button.pack(side=tk.LEFT)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, bg="#e74c3c", fg="white")
delete_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
