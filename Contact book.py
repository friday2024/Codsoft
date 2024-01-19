import tkinter as tk
from tkinter import messagebox

def add_contact():
    name = name_entry.get()
    if name:
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()

        contact_info = f"Phone: {phone}\nEmail: {email}\nAddress: {address}"
        contacts[name] = contact_info

        messagebox.showinfo("Success", "Contact added successfully!")

        clear_entries()
    else:
        messagebox.showwarning("Warning", "Please enter a name.")

def view_contacts():
    if contacts:
        contacts_list_window = tk.Toplevel(root)
        contacts_list_window.title("Contacts List")

        contacts_list = tk.Text(contacts_list_window, wrap="word", height=15, width=40)
        contacts_list.pack(padx=10, pady=10)

        for name, info in contacts.items():
            contacts_list.insert(tk.END, f"{name}\n{info}\n\n")

        contacts_list.config(state=tk.DISABLED)
    else:
        messagebox.showinfo("No Contacts", "No contacts to display.")

def search_contact():
    search_window = tk.Toplevel(root)
    search_window.title("Search Contact")

    search_label = tk.Label(search_window, text="Enter name to search:")
    search_label.pack(pady=10)

    search_entry = tk.Entry(search_window, width=30)
    search_entry.pack(pady=10)

    def perform_search():
        name_to_search = search_entry.get()
        search_window.destroy()

        if name_to_search in contacts:
            contact_info = contacts[name_to_search]
            messagebox.showinfo("Contact Found", f"{name_to_search}\n{contact_info}")
        else:
            messagebox.showinfo("Contact Not Found", f"No contact found for {name_to_search}.")

    search_button = tk.Button(search_window, text="Search", command=perform_search)
    search_button.pack(pady=10)

def update_contact():
    name_to_update = name_entry.get()
    if name_to_update in contacts:
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()

        contact_info = f"Phone: {phone}\nEmail: {email}\nAddress: {address}"
        contacts[name_to_update] = contact_info

        messagebox.showinfo("Success", "Contact updated successfully!")
        clear_entries()
    else:
        messagebox.showinfo("Contact Not Found", f"No contact found for {name_to_update}.")

def delete_contact():
    name_to_delete = name_entry.get()
    if name_to_delete in contacts:
        del contacts[name_to_delete]
        messagebox.showinfo("Success", "Contact deleted successfully!")
        clear_entries()
    else:
        messagebox.showinfo("Contact Not Found", f"This contact does not contain for {name_to_delete}.")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Contact Management System")

# Set the window icon
root.iconbitmap("diary-bookmarks.ico")

# Contacts dictionary to store contact information
contacts = {}

# Labels
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
phone_label = tk.Label(root, text="Phone:")
phone_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
email_label = tk.Label(root, text="Email:")
email_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
address_label = tk.Label(root, text="Address:")
address_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

# Entry widgets
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)
phone_entry = tk.Entry(root, width=30)
phone_entry.grid(row=1, column=1, padx=10, pady=5)
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=2, column=1, padx=10, pady=5)
address_entry = tk.Entry(root, width=30)
address_entry.grid(row=3, column=1, padx=10, pady=5)

# Buttons
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=4, column=0, columnspan=2, pady=10)

view_button = tk.Button(root, text="View Contacts", command=view_contacts)
view_button.grid(row=5, column=0, columnspan=2, pady=10)

search_button = tk.Button(root, text="Search Contact", command=search_contact)
search_button.grid(row=6, column=0, columnspan=2, pady=10)

update_button = tk.Button(root, text="Update Contact", command=update_contact)
update_button.grid(row=7, column=0, columnspan=2, pady=10)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=8, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
