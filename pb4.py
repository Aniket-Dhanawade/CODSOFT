import tkinter as tk
from tkinter import messagebox, simpledialog

contact = {}
contact_list_window = None

def display_contact():
    global contact_list_window

    # Destroy the existing Toplevel window if it exists
    if contact_list_window:
        contact_list_window.destroy()

    # Create a new Toplevel window
    contact_list_window = tk.Toplevel(root)
    contact_list_window.title("Contact List")
    contact_list_window.geometry("600x400")

    contact_list = tk.Text(contact_list_window, height=20, width=60, font=("Helvetica", 12))
    contact_list.insert(tk.END, "Name\t\tContact Number\n")

    for key in contact:
        contact_list.insert(tk.END, "{}\t\t{}\n".format(key, contact[key]))

    contact_list.pack(padx=20, pady=20)

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()

    if name and phone:
        contact[name] = phone
        display_contact()
        clear_entries()
    else:
        messagebox.showwarning("Error", "Name and phone number are required.")

def search_contact():
    if not contact:
        messagebox.showinfo("Empty Contact Book", "There are no contacts to search.")
        return

    search_dialog = tk.Toplevel(root)
    search_dialog.title("Search Contact")
    search_dialog.geometry("400x150")

    label = tk.Label(search_dialog, text="Enter the contact name to search:", font=("Helvetica", 14))
    label.pack(pady=10)

    search_name = tk.Entry(search_dialog, font=("Helvetica", 12))
    search_name.pack(pady=10)

    ok_button = tk.Button(search_dialog, text="OK", command=lambda: search_contact_action(search_name.get(), search_dialog), font=("Helvetica", 14))
    ok_button.pack(side="left", padx=10)

    cancel_button = tk.Button(search_dialog, text="Cancel", command=search_dialog.destroy, font=("Helvetica", 14))
    cancel_button.pack(side="right", padx=10)

def search_contact_action(search_name, search_dialog):
    search_dialog.destroy()
    if search_name:
        if search_name in contact:
            messagebox.showinfo("Contact Found", "{}'s contact number is {}".format(search_name, contact[search_name]))
        else:
            messagebox.showinfo("Contact Not Found", "Name is not found in the contact book")

def edit_contact():
    if not contact:
        messagebox.showinfo("Empty Contact Book", "There are no contacts to edit.")
        return

    edit_dialog = tk.Toplevel(root)
    edit_dialog.title("Edit Contact")
    edit_dialog.geometry("400x150")

    label = tk.Label(edit_dialog, text="Enter the contact name to edit:", font=("Helvetica", 14))
    label.pack(pady=10)

    edit_name = tk.Entry(edit_dialog, font=("Helvetica", 12))
    edit_name.pack(pady=10)

    ok_button = tk.Button(edit_dialog, text="OK", command=lambda: edit_contact_action(edit_name.get(), edit_dialog), font=("Helvetica", 14))
    ok_button.pack(side="left", padx=10)

    cancel_button = tk.Button(edit_dialog, text="Cancel", command=edit_dialog.destroy, font=("Helvetica", 14))
    cancel_button.pack(side="right", padx=10)

def edit_contact_action(edit_name, edit_dialog):
    edit_dialog.destroy()
    if edit_name in contact:
        edit_choice_dialog = tk.Toplevel(root)
        edit_choice_dialog.title("Edit Choice")
        edit_choice_dialog.geometry("400x150")

        label = tk.Label(edit_choice_dialog, text="Choose what to edit:", font=("Helvetica", 14))
        label.pack(pady=10)

        name_button = tk.Button(edit_choice_dialog, text="Name", command=lambda: edit_name_option(edit_name, edit_choice_dialog), font=("Helvetica", 14))
        name_button.pack(pady=10)

        contact_button = tk.Button(edit_choice_dialog, text="Contact", command=lambda: edit_contact_option(edit_name, edit_choice_dialog), font=("Helvetica", 14))
        contact_button.pack(pady=10)
    else:
        messagebox.showinfo("Contact Not Found", "Name is not found in the contact book")

def edit_name_option(edit_name, edit_option_dialog):
    edit_option_dialog.destroy()
    new_name_dialog = tk.Toplevel(root)
    new_name_dialog.title("New Name")
    new_name_dialog.geometry("400x150")

    label = tk.Label(new_name_dialog, text="Enter the new name:", font=("Helvetica", 14))
    label.pack(pady=10)

    new_name = tk.Entry(new_name_dialog, font=("Helvetica", 12))
    new_name.pack(pady=10)

    ok_button = tk.Button(new_name_dialog, text="OK", command=lambda: new_name_action(edit_name, new_name.get(), new_name_dialog), font=("Helvetica", 14))
    ok_button.pack(side="left", padx=10)

    cancel_button = tk.Button(new_name_dialog, text="Cancel", command=new_name_dialog.destroy, font=("Helvetica", 14))
    cancel_button.pack(side="right", padx=10)

def new_name_action(edit_name, new_name, new_name_dialog):
    new_name_dialog.destroy()
    if new_name:
        contact[new_name] = contact.pop(edit_name)
        display_contact()
        clear_entries()

def edit_contact_option(edit_name, edit_option_dialog):
    edit_option_dialog.destroy()
    new_contact_dialog = tk.Toplevel(root)
    new_contact_dialog.title("New Contact")
    new_contact_dialog.geometry("400x150")

    label = tk.Label(new_contact_dialog, text="Enter the new contact number:", font=("Helvetica", 14))
    label.pack(pady=10)

    new_contact = tk.Entry(new_contact_dialog, font=("Helvetica", 12))
    new_contact.pack(pady=10)

    ok_button = tk.Button(new_contact_dialog, text="OK", command=lambda: new_contact_action(edit_name, new_contact.get(), new_contact_dialog), font=("Helvetica", 14))
    ok_button.pack(side="left", padx=10)

    cancel_button = tk.Button(new_contact_dialog, text="Cancel", command=new_contact_dialog.destroy, font=("Helvetica", 14))
    cancel_button.pack(side="right", padx=10)

def new_contact_action(edit_name, new_contact, new_contact_dialog):
    new_contact_dialog.destroy()
    if new_contact:
        contact[edit_name] = new_contact
        display_contact()
        clear_entries()

def delete_contact():
    if not contact:
        messagebox.showinfo("Empty Contact Book", "There are no contacts to delete.")
        return

    delete_dialog = tk.Toplevel(root)
    delete_dialog.title("Delete Contact")
    delete_dialog.geometry("400x150")

    label = tk.Label(delete_dialog, text="Enter the contact name to delete:", font=("Helvetica", 14))
    label.pack(pady=10)

    del_name = tk.Entry(delete_dialog, font=("Helvetica", 12))
    del_name.pack(pady=10)

    ok_button = tk.Button(delete_dialog, text="OK", command=lambda: delete_contact_action(del_name.get(), delete_dialog), font=("Helvetica", 14))
    ok_button.pack(side="left", padx=10)

    cancel_button = tk.Button(delete_dialog, text="Cancel", command=delete_dialog.destroy, font=("Helvetica", 14))
    cancel_button.pack(side="right", padx=10)

def delete_contact_action(del_name, delete_dialog):
    delete_dialog.destroy()
    if del_name in contact:
        confirm = messagebox.askyesno("Delete Contact", "Do you want to delete {}'s contact?".format(del_name))
        if confirm:
            contact.pop(del_name)
            display_contact()
            clear_entries()
    else:
        messagebox.showinfo("Contact Not Found", "Name is not found in the contact book")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Contact Book")

screen_width = root.winfo_screenwidth()
root.geometry(f"300x430+{screen_width-620}+50")

name_label = tk.Label(root, text="Name:", font=("Helvetica", 12))
name_entry = tk.Entry(root, font=("Helvetica", 12))

phone_label = tk.Label(root, text="Phone:", font=("Helvetica", 12))
phone_entry = tk.Entry(root, font=("Helvetica", 12))

button_font = ("Helvetica", 14)

add_button = tk.Button(root, text="Add Contact", command=add_contact, font=button_font)
search_button = tk.Button(root, text="Search Contact", command=search_contact, font=button_font)
display_button = tk.Button(root, text="Display Contacts", command=display_contact, font=button_font)
edit_button = tk.Button(root, text="Edit Contact", command=edit_contact, font=button_font)
delete_button = tk.Button(root, text="Delete Contact", command=delete_contact, font=button_font)
exit_button = tk.Button(root, text="Exit", command=root.destroy, font=button_font)

display_button.grid(row=4, column=0, columnspan=2, pady=10)
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry.grid(row=0, column=1, padx=10, pady=10)
phone_label.grid(row=1, column=0, padx=10, pady=10)
phone_entry.grid(row=1, column=1, padx=10, pady=10)
add_button.grid(row=2, column=0, columnspan=2, pady=10)
search_button.grid(row=3, column=0, columnspan=2, pady=10)
edit_button.grid(row=5, column=0, columnspan=2, pady=10)
delete_button.grid(row=6, column=0, columnspan=2, pady=10)
exit_button.grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()
