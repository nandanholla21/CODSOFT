import tkinter as tk
from tkinter import messagebox
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
        else:
            messagebox.showerror("Error", "Invalid operation")
            return

        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x300")
root.configure(bg="#f5f5f5")
entry_num1 = tk.Entry(root, width=10, font=('Arial', 16), bg="#ffffff")
entry_num1.grid(row=0, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(root, width=10, font=('Arial', 16), bg="#ffffff")
entry_num2.grid(row=0, column=2, padx=10, pady=10)
operations = ["Addition", "Subtraction", "Multiplication", "Division"]
operation_var = tk.StringVar(root)
operation_var.set(operations[0])
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.config(font=('Arial', 12), bg="#3498db", fg="white")
operation_menu.grid(row=0, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate", command=calculate, font=('Arial', 16), bg="#2ecc71", fg="white")
calculate_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=tk.EW)

result_label = tk.Label(root, text="Result:", font=('Arial', 16), bg="#f5f5f5", fg="#333333")
result_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky=tk.W)
root.mainloop()

