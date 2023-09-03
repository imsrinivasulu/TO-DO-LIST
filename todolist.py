import tkinter as tk
from tkinter import messagebox
class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []
        self.taskentry = tk.Entry(root, width=40)
        self.taskentry.pack(padx=20, pady=10)
        self.addbutton = tk.Button(root, text="Add Task", command=self.addtask)
        self.addbutton.pack()
        self.tasklistbox = tk.Listbox(root, width=40)
        self.tasklistbox.pack(padx=20, pady=10)
        self.removebutton = tk.Button(root, text="Remove Task", command=self.removetask)
        self.removebutton.pack()
    def addtask(self):
        tasktext = self.taskentry.get()
        if tasktext:
            self.tasks.append(tasktext)
            self.tasklistbox.insert(tk.END, tasktext)
            self.taskentry.delete(0, tk.END)
    def removetask(self):
        selectedtaskindex = self.tasklistbox.curselection()
        if selectedtaskindex:
            index = int(selectedtaskindex[0])
            self.tasklistbox.delete(index)
            del self.tasks[index]
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
