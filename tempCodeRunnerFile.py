import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate a random password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to handle password generation and display
def generate_password_and_display():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Length should be a positive integer.")
            return

        password = generate_password(length)
        password_display.config(text="Generated Password:\n" + password)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid integer.")

# Create the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x300")
root.configure(bg="#34495E")

# Create GUI components with updated styling
header_label = tk.Label(root, text="Password Generator", font=("Arial", 18, "bold"), bg="#34495E", fg="white")
header_label.pack(pady=(20, 10))

length_label = tk.Label(root, text="Enter the desired length:", font=("Arial", 12), bg="#34495E", fg="white")
length_label.pack(pady=(0, 5))

length_entry = tk.Entry(root, font=("Arial", 12))
length_entry.pack(pady=(0, 10), padx=20, ipady=5, ipadx=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password_and_display, bg="#2ECC71", fg="white", font=("Arial", 14, "bold"), padx=20, pady=10, bd=0)
generate_button.pack(pady=(0, 20))

password_display = tk.Label(root, text="Generated Password:", font=("Arial", 12), bg="#34495E", fg="white")
password_display.pack(pady=(0, 5))

# Run the main event loop
root.mainloop()
