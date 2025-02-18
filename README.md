# To-Do List 

### Project Overview
This is a **To-Do List** written in Python that allows users to manage their tasks. The system provides functionality to:
- Add new tasks with a priority and deadline.
- View all tasks sorted by priority and deadline.
- Mark tasks as completed.
- Delete tasks.
- Show task completion statistics.

The project is organized into two files:
1. `ToDoList.py` - Implementation for `To Do List` Functions.
2. `main.py` - The main program where the user interacts with the system.

---
### Files

#### 1. `ToDoList.py`
This file contains the implementation of the functions that manage the to-do list tasks. It handles the task management operations, such as adding tasks, viewing tasks, marking tasks as completed, deleting tasks, and showing statistics.

#### Functions in `ToDoList.py`
- `clearScreen()`: Clears the screen for better user experience.
- `addTask()`: Adds a new task with a priority and optional deadline.
- `getDeadline()`: Returns the deadline of a task or a maximum date if no deadline is set.
- `viewTasks()`: Displays all tasks sorted by priority and deadline.
- `markComplete()`: Marks a task as completed.
- `deleteTask()`: Deletes a task based on priority and task number.
- `showStatistics()`: Displays statistics about the tasks, including completion rate.

#### 2. `main.py`
This is the entry point of the program where the user interacts with the system.

#### How `main.py` Works:
1. The program imports the functions from `ToDoList.py`.
2. It displays a menu with options to perform various operations.
3. The user selects an option, and the corresponding function from `ToDoList.py` is called.
4. The program continues to run in a loop until the user chooses to exit.

#### Menu Options in `main.py`
```
1.Add Task
2.View Tasks
3.Mark Task as Completed
4.Delete Task
5.Show Task Statistics
6.Exit

```
- Each option calls the respective function from `ToDoList.py`.
---
### Libraries Used
- **numpy**: Used to calculate task completion statistics.
- **os**: Used to clear the terminal screen at the beginning of each function for better user experience.
- **datetime**: Used for handling task deadlines.

### Notes
- Tasks are stored in a dictionary categorized by priority (`High`, `Medium`, `Low`).
- Each task contains information like the task name, completion status, and an optional deadline.
- The user can choose to mark tasks as completed, delete them, or view statistics regarding task completion.
- The program validates user inputs to ensure proper functionality.

---










