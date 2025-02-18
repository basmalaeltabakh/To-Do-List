import os
import sys
import time
import numpy as np
from collections import defaultdict
from datetime import datetime

# Tasks dictionary with priorities
tasks = defaultdict(list)
priorities = {"High": 1, "Medium": 2, "Low": 3} 

def clearScreen():
    """Clear the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def addTask():
    clearScreen() 
    """Add Task with priority and deadline"""
    task = input("Enter the new task name: ").strip()

    if not task:
        print("Task cannot be empty!")
        return
    
    print("\nChoose a priority: ")
    for index, priority in enumerate(priorities.keys(), start=1):
        print(f"{index}. {priority}")
    
    choice = input("Enter the number (1-3): ")
    try:
        priority = list(priorities.keys())[int(choice)-1]
        deadline_input = input("Enter deadline (YYYY-MM-DD) or leave blank: ").strip()
        deadline = datetime.strptime(deadline_input, "%Y-%m-%d") if deadline_input else None
        tasks[priority].append({"Task": task, "Completed": False, "Deadline": deadline})
        print("Task added successfully!")
    except Exception as e:
        print(f"Invalid choice! Error: {e}")

def getDeadline(task):
    """Return the task deadline, or a maximum date if no deadline is set."""
    return task["Deadline"] if task.get("Deadline") else datetime.max

def viewTasks():
    clearScreen() 
    """Display all tasks sorted by priority and deadline"""
    if not any(tasks.values()): 
        print("No tasks available!")
        return

    print("Tasks available, proceeding to display...") 
    
    for priority in sorted(priorities, key=priorities.get):
        if tasks[priority]:  
            print(f"\n{priority}:")
            sortedTasks = sorted(tasks[priority], key=getDeadline)
            for idx, task in enumerate(sortedTasks, 1):
                status = "✓" if task["Completed"] else "✗"
                deadline = task["Deadline"].strftime("%Y-%m-%d") if task["Deadline"] else "No deadline"
                print(f"  {idx}. [{status}] {task['Task']} (Deadline: {deadline})")

def markComplete():
    clearScreen() 
    """Mark a Task as Completed"""
    viewTasks()
    try:
        
        priorityChoice = input("Choose priority (High, Medium, Low): ").strip().title()

       
        if priorityChoice not in priorities:
            print("Invalid priority! Please choose from High, Medium, or Low.")
            return
        
        taskNum = int(input("Enter Task number: ")) - 1
        if 0 <= taskNum < len(tasks[priorityChoice]):
            tasks[priorityChoice][taskNum]["Completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid number! Please enter a valid task number.")
    except Exception as e:
        print(f"Input error! Error: {e}")

def deleteTask():
    clearScreen() 
    """Delete a Task based on priority and task number"""
    viewTasks()
    try:
      
        priorityChoice = input("Choose priority (High, Medium, Low): ").strip().title()

       
        if priorityChoice not in priorities:
            print("Invalid priority! Please choose from High, Medium, or Low.")
            return
        
        taskNum = int(input("Enter Task number: ")) - 1
        if 0 <= taskNum < len(tasks[priorityChoice]):
            del tasks[priorityChoice][taskNum]
            print("Task deleted successfully!")
        else:
            print("Invalid number! Please enter a valid task number.")
    except Exception as e:
        print(f"Input error! Error: {e}")

def showStatistics():
    clearScreen() 
    """Show statistics of completed vs pending tasks"""
    totalTasks = 0
    for priority in priorities:
        totalTasks += len(tasks[priority])

    completedTasks = 0
    for priority in priorities:
        for task in tasks[priority]:
            if task["Completed"]:
                completedTasks += 1

    if totalTasks == 0:
        print("No Tasks to show statistics!")
    else:
        completionRate = np.round((completedTasks / totalTasks) * 100, 2)
        print(f"\nTask Completion Statistics:")
        print(f"Completed: {completedTasks}/{totalTasks} ({completionRate}%)")
        print(f"Pending: {totalTasks - completedTasks}/{totalTasks}")