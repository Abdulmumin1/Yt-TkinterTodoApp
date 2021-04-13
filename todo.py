import tkinter as tk
import tkinter.messagebox as msg
from tkinter.font import Font
import pickle

#initiating the window
win = tk.Tk()
win.title('ToDo')
win.geometry("350x600")
win.resizable(False, False)
win.configure(background="black")

def add_task():
    """
    Fuction for addding item to the listbox
    this is done by getting the item in the 
    entry box and inserting it at the end of
    our list box
    """
    if task_input.get() != "":
        lst_tasks.insert(tk.END, task_input.get().capitalize())
        en_task.delete(0, tk.END)
    else:
        msg.showwarning('Waring', 'you must enter a task!')


def del_task():
    """
    Function delete the selected item in
    the list box and show warning if anykind
    of exception is catched
    """
    try:
        task_index = lst_tasks.curselection()[0]
        lst_tasks.delete(task_index)
    except:
        msg.showwarning('Warning',  'You must select a task to delete!')
def load_tasks():
    """
    used to load tasks from the the tasks.dat
    file and also return and error message if 
    any exception is catched
    """
    try:

        tasks = pickle.load(open("tasks.dat", "rb"))
        lst_tasks.delete(0,  tk.END)
        if tasks:
            for task in tasks:
                lst_tasks.insert(tk.END, task)
        else:
            msg.showwarning("alert", "no task to be loaded!")
    except:
        msg.showwarning("warning", "No tasks to load")

def save_tasks():
    """
    uses the pickle module to dump
    the items collected from the listbox
    and write it into a file 
    """
    
    tasks = lst_tasks.get(0, lst_tasks.size())
    if tasks:
        pickle.dump(tasks, open("tasks.dat", "wb"))
    else:
        msg.showwarning('alert', 'nothing to save')
#defining a Font
my_font = Font(
    family="monospace",
    size="10",
    weight="bold"
)
#storing our entry input
task_input = tk.StringVar()
Todo_label = tk.Label(win, text="Todo list", height=3, width=50, bg="green", fg="white", font=my_font, bd=0)
Todo_label.pack()

#creating a frame to pack the list and the scrollbar into
frame = tk.Frame(win)
frame.pack()

lst_tasks = tk.Listbox(frame, height=20, width=50, font=my_font, highlightthickness=0, selectbackground="cyan")
lst_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

sc_bar = tk.Scrollbar(frame)
sc_bar.pack(side=tk.RIGHT, fill=tk.BOTH)

lst_tasks.config(yscrollcommand=sc_bar.set)
sc_bar.config(command=lst_tasks.yview)

#defining a frame to pack our entry box and add_item button into
iframe = tk.Frame(win)
iframe.pack()

en_task = tk.Entry(iframe, textvariable=task_input,  width=40)
en_task.pack(sid=tk.LEFT, fill=tk.BOTH)
en_task.focus()
btn_add = tk.Button(iframe, text="Add task",height=0, width=8, command=add_task, bg="cyan", )
btn_add.pack(side=tk.RIGHT, fill=tk.BOTH)
   
btn_del = tk.Button(win, text="Delete task",height=3, width=48, command=del_task,bg="red")
btn_del.pack() 

btn_load = tk.Button(win,text="Load tasks", height=3, width=48, command=load_tasks, bg="brown")
btn_load.pack() 

btn_save = tk.Button(win, text='Save tasks', height=3, width=48, command=save_tasks, bg="pink")
btn_save.pack() 

if __name__ == "__main__":
    win.mainloop()


