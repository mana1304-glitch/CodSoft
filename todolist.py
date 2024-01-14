import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except IndexError:
        pass

root = tk.Tk()
root.title("TODOLIST")

frame = tk.Frame(root)

frame.pack(pady=10)

listbox = tk.Listbox(frame, width=50, height=10, bd=0, font=("Arial", 12))
listbox.configure(bg='beige')
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(root, font=("Arial", 12), width=40)
entry.configure(bg='beige')
entry.pack(pady=20)

add_button = tk.Button(root, text="Add Task", width=10, command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=10, command=delete_task)
delete_button.pack(pady=5)

root.mainloop()