import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

def generate_password(length, complexity):
    if complexity == "Easy":
        character_sets = [string.ascii_letters, string.digits]
    elif complexity == "Medium":
        character_sets = [string.ascii_letters, string.digits, string.punctuation]
    elif complexity == "Hard":
        character_sets = [string.ascii_letters, string.digits, string.punctuation, string.ascii_letters.upper()]

    all_characters = ''.join(character_sets)
    length = max(length, 8)

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def generate_password_and_display():
    try:
        password_length = int(length_entry.get())
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid number.")
        return

    selected_complexity = complexity_combobox.get()

    password = generate_password(password_length, selected_complexity)
    result_label.config(text=f"Your Generated Password: {password}")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.wm_iconbitmap("key-skeleton-left-right.ico")
# Labels
length_label = ttk.Label(root, text="Enter the length of your password:")
length_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

complexity_label = ttk.Label(root, text="Select Complexity:")
complexity_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

# Entry widget for password length
length_entry = ttk.Entry(root, width=5)
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Combobox for selecting complexity level
complexity_levels = ["Easy", "Medium", "Hard"]
complexity_combobox = ttk.Combobox(root, values=complexity_levels, state="readonly")
complexity_combobox.set("Medium")  # Default complexity level
complexity_combobox.grid(row=1, column=1, padx=10, pady=10)

# Button to generate and display password
generate_button = ttk.Button(root, text="Generate Password", command=generate_password_and_display)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Label to display the generated password
result_label = ttk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
