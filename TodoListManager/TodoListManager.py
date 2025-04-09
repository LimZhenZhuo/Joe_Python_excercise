import tkinter as tk  # Import Tkinter for GUI
from tkinter import messagebox, simpledialog  # Import dialog boxes
import os  # Import OS for file operations


class TodoApp:
    def __init__(self, root):
        self.root = root  # Main window instance
        self.root.title("Todo List Manager")  # Set window title
        self.tasks = []  # List to store tasks
        self.file_path = "tasks.txt"  # File to save tasks

        # Load tasks from file if it exists
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:  # Open in read mode
                self.tasks = f.read().splitlines()  # Read lines into list

        # Create a Listbox widget to display tasks
        self.listbox = tk.Listbox(root, width=50)
        self.listbox.pack(pady=10)  # Add padding

        # Create a frame to hold buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        # Add "Add Task" button with a callback to add_task()
        tk.Button(btn_frame, text="Add Task", command=self.add_task).pack(side=tk.LEFT, padx=5)
        # Add "Delete Task" button with a callback to delete_task()
        tk.Button(btn_frame, text="Delete Task", command=self.delete_task).pack(side=tk.LEFT, padx=5)

        # Populate the Listbox with existing tasks
        self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)  # Clear current items
        for task in self.tasks:
            self.listbox.insert(tk.END, task)  # Insert each task

    def add_task(self):
        # Show input dialog to get task content
        task = simpledialog.askstring("Add Task", "Enter task content:")
        if task:  # Only proceed if input is not empty
            self.tasks.append(task)  # Add to task list
            self.update_listbox()  # Refresh the Listbox
            self.save_tasks()  # Save to file

    def delete_task(self):
        # Get selected task index (returns a tuple, e.g., (2,))
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]  # Extract the first (only) index
            del self.tasks[index]  # Remove task from list
            self.update_listbox()  # Refresh the Listbox
            self.save_tasks()  # Save to file
        else:
            # Show warning if no task is selected
            messagebox.showwarning("Warning", "Please select a task first!")

    def save_tasks(self):
        # Write tasks to file, each on a new line
        with open(self.file_path, "w") as f:
            f.write("\n".join(self.tasks))


if __name__ == "__main__":
    root = tk.Tk()  # Create main Tkinter window
    app = TodoApp(root)  # Instantiate the app
    root.mainloop()  # Start the GUI event loop