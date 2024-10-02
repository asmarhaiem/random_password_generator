import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip  # Clipboard integration

# Function to generate password
def generate_password():

    length = int(password_length_entry.get())
    #It gets the value of the BooleanVar the box is checked or not then we will use in the root main
    #The value stored in include_symbols is then used later in the program (specifically in the generate_password function) to determine whether to add symbols to the character set used for generating the password
    #BoxChecked = True

    include_uppercase = uppercase_var.get()
    include_numbers = numbers_var.get()
    include_symbols = symbols_var.get()
    exclude_chars = exclude_entry.get()

#For security reasons we include mandaatory characters
    characters = string.ascii_lowercase
    mandatory_characters = []

    if include_uppercase:
        characters += string.ascii_uppercase
        mandatory_characters.append(random.choice(string.ascii_uppercase))  # Ensure at least one uppercase letter
    if include_numbers:
        characters += string.digits
        mandatory_characters.append(random.choice(string.digits))  # Ensure at least one number
    if include_symbols:
        characters += string.punctuation
        mandatory_characters.append(random.choice(string.punctuation))  # Ensure at least one symbol

    # Exclude specific characters
    if exclude_chars:
        characters = ''.join([char for char in characters if char not in exclude_chars])

    # Generate password
    #we make sure we have the place to mandatory characters so substract the length of it
    password = ''.join(random.choice(characters) for _ in range(length - len(mandatory_characters)))
    password += ''.join(mandatory_characters)  # Ensure mandatory characters are included
    password = ''.join(random.sample(password, len(password)))  # Shuffle to avoid pattern
    password_label.config(text=f"Generated Password: {password}")

# Function to copy password to clipboard
def copy_to_clipboard():
    pyperclip.copy(password_label.cget("text").split(": ")[1])
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Create main window
root = tk.Tk()
root.title("Advanced Password Generator")

# Add elements to the window
tk.Label(root, text="Password Length:").grid(row=0, column=0, pady=5)
password_length_entry = tk.Entry(root)
password_length_entry.grid(row=0, column=1)

uppercase_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var).grid(row=1, column=0, columnspan=2)

numbers_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).grid(row=2, column=0, columnspan=2)

symbols_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).grid(row=3, column=0, columnspan=2)

tk.Label(root, text="Exclude Characters:").grid(row=4, column=0, pady=5)
exclude_entry = tk.Entry(root)
exclude_entry.grid(row=4, column=1)

tk.Button(root, text="Generate Password", command=generate_password).grid(row=5, column=0, columnspan=2, pady=10)

password_label = tk.Label(root, text="Generated Password: ")
password_label.grid(row=6, column=0, columnspan=2, pady=5)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).grid(row=7, column=0, columnspan=2, pady=5)

# Run the Tkinter event loop
root.mainloop()
