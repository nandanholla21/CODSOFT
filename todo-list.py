import tkinter as tk
from tkinter import messagebox
def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task = listbox_tasks.curselection()
    if selected_task:
        listbox_tasks.delete(selected_task)

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")
root.configure(bg='#EAEAEA')  
entry_task = tk.Entry(root, width=40, font=('Arial', 14), bg='#FFFFFF')
entry_task.pack(pady=10, padx=10)
add_button = tk.Button(root, text="Add Task", command=add_task, font=('Arial', 12), bg='#4CAF50', fg='#FFFFFF')
add_button.pack(pady=5, padx=10)
remove_button = tk.Button(root, text="Remove Task", command=remove_task, font=('Arial', 12), bg='#FF5733', fg='#FFFFFF')
remove_button.pack(pady=5, padx=10)
listbox_tasks = tk.Listbox(root, width=40, font=('Arial', 14), bg='#F0F0F0')
listbox_tasks.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=listbox_tasks.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox_tasks.config(yscrollcommand=scrollbar.set)
root.mainloop()

