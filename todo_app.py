import tkinter as tk
from tkinter.font import Font
import tkinter.messagebox as msg
import pickle

def add_task():
	task_to_add = add_task_variable.get()
	if task_to_add:
		listbox.insert(tk.END, task_to_add)
		add_task_input.delete(0, tk.END)
	else:
		msg.showwarning("Warning", "Please enter a task!")

def delete_task():
	try:
		task_to_delete = listbox.curselection()[0]
		listbox.delete(task_to_delete)
	except IndexError:
		msg.showwarning("Warning", "Please select a task to delete")


def save_tasks():
	tasks = listbox.get(0, listbox.size())
	if tasks:
		pickle.dump(tasks, open("task.dat", 'wb'))
	else:
		msg.showwarning("Warning", "no tasks to save!")


def load_task():
	try:
		tasks = pickle.load(open("task.dat", 'rb'))
		if tasks:
			for task in tasks:
				listbox.insert(tk.END, task)
		else:	
			msg.showwarning("Warning", "no task to load!")
	except:
		msg.showwarning("Warning", "task.dat does not exist")




window = tk.Tk()
window.title("Todo app")

my_font = Font(
    weight="bold",
    family="monospace",
    size=15
)

listbox = tk.Listbox(window, height=20, width=50, selectbackground="orange", font=my_font)
listbox.pack(fill=tk.BOTH, expand=True)

entry_frame = tk.Frame(window)
entry_frame.pack(expand=True, fill=tk.BOTH)

add_task_variable = tk.StringVar()

add_task_input = tk.Entry(entry_frame, width=39, textvariable=add_task_variable, font=my_font)
add_task_input.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
add_task_input.focus()

add_task_btn = tk.Button(entry_frame, text="add task", bg="orange", command=add_task)
add_task_btn.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

del_task_btn = tk.Button(window, width=48, text="delete task", bg="orange", command=delete_task)
del_task_btn.pack(expand=True, fill=tk.BOTH)

save_tasks_btn = tk.Button(window, width=48, text="save tasks", bg="orange", command=save_tasks)
save_tasks_btn.pack(expand=True, fill=tk.BOTH)

load_tasks_btn = tk.Button(window, width=48, text="load tasks", bg="orange", command=load_task)
load_tasks_btn.pack(expand=True, fill=tk.BOTH)


window.mainloop()

