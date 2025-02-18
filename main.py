from ToDoList import *

def showMenu():
    """ Display the menu options """
    print("\n" + "="*50)
    print(" " * 10 + " To-Do List  ")
    print("="*50)
    print(" " * 10 + " 1. Add Task")
    print(" " * 10 + " 2. View Tasks")
    print(" " * 10 + " 3. Mark Task as Completed")
    print(" " * 10 + " 4. Delete Task")
    print(" " * 10 + " 5. Show Task Statistics")
    print(" " * 10 + " 6. Exit") 
    print("="*50)

def main():
    while True:
        
        showMenu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            addTask()
        elif choice == "2":
            viewTasks()
        elif choice == "3":
           markComplete()
        elif choice == "4":
            deleteTask()
        elif choice == "5":
            showStatistics()
        elif choice == "6":
            print("Exiting To-Do List System.")
            
            break
        else:
            print("Invalid choice! Enter a number between 1-6.")
              

if __name__ == "__main__":
    main()