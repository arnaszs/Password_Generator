import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())

    if length <= 0:
        messagebox.showerror("Error", "Password length must be greater than 0")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    password = password_entry.get()
    if password:
        window.clipboard_clear()
        window.clipboard_append(password)
        window.update()
        messagebox.showinfo("Copied", "Password copied to clipboard")
    else:
        messagebox.showwarning("Empty Password", "Generate a password first before copying")

# Create the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("275x250")  # Set initial window size

# Style configuration
background_colour = "#3498db"  # Blue colour
fg_colour = "#ffffff"  # White colour
button_colour = "#2ecc71"  # Green colour for buttons
button_text_colour = "#ffffff"  # White colour for button text
colour_entry_fields = "#ecf0f1"  # Light gray background for entry fields

# Set background color for the entire window
window.configure(bg=background_colour)

# Length Label and Entry
length_label = tk.Label(window, text="Password Length:", bg=background_colour, fg=fg_colour)
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = tk.Entry(window, bg=colour_entry_fields)
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Generate Button
generate_button = tk.Button(window, text="Generate Password", command=generate_password,
                            bg=button_colour, fg=button_text_colour, relief=tk.GROOVE)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Password Entry
password_entry = tk.Entry(window, bg=colour_entry_fields)
password_entry.grid(row=2, column=0, columnspan=2, pady=10)

# Copy Password Button
copy_button = tk.Button(window, text="Copy Password", command=copy_password,
                        bg=button_colour, fg=button_text_colour, relief=tk.GROOVE)
copy_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
window.mainloop()
