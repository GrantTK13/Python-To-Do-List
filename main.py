import time  # Imports the time module.

tasks = []  # Create an empty list that will contain tasks later on.

print("GrantTK13's To-Do List Program")  # Title
time.sleep(1)
print("Commands:")  # List of commands
time.sleep(1)
print("add - Creates a new task.")
print("remove - Deletes a task.")
print("change - Changes a task.")
print("complete - Marks a task as completed.")
print("clear - Deletes all tasks.")
print("list - Lists all tasks.")
print("quit - Exits the program.")
time.sleep(1)

def add_task():
    task_to_add = input("Enter the name of the task you would like to add: ")
    if not task_to_add in tasks:
        tasks.append(task_to_add)
        print("\'" + task_to_add + "\' has been added.")
        time.sleep(1)
    else:
        print("\'" + task_to_add + "\' is already in this to-do list!")  # Warns the user if the task already exists.
        time.sleep(1)

def remove_task():
    task_to_remove = input("Enter the name of the task you would like to remove: ")
    if task_to_remove in tasks:
        tasks.remove(task_to_remove)  
        print("\'" + task_to_remove + "\' has been removed.")
        time.sleep(1)
    else:
        print("\'" + task_to_remove + "\' isn't a task!")  # Warns the user if the task to remove doesn't exist.
        time.sleep(1)

def change_task():
    task_to_change = input("Enter the name of the task you would like to change: ")
    if task_to_change in tasks:
        task_to_change_index = tasks.index(task_to_change)
        new_task_name = input("Enter the new task: ")
        tasks[task_to_change_index] = new_task_name
        print("\'" + task_to_change + "\' has been changed to \'" + new_task_name + "\'.")
        time.sleep(1)
    else:
        print("\'" + task_to_change + "\' isn't a task!")  # Warns the user if the task to change doesn't exist.
        time.sleep(1)

def complete_task():
    completed_task = input("Enter the name of the task you would like to mark as complete: ")
    if completed_task in tasks:
        completed_task_index = tasks.index(completed_task)
        tasks[completed_task_index] = completed_task + " (completed)"
        print("\'" + completed_task + "\' has been marked as completed.")
        time.sleep(1)
    else:
        print("\'" + completed_task + "\' isn't a task!")  # Warns the user if the task to mark as complete doesn't exist.
        time.sleep(1)

def clear_tasks():
    tasks.clear()
    print("Removed all tasks.")
    time.sleep(1)

def list_tasks():
    if not len(tasks) == 0:
        print("The tasks in this to-do list are: " + ", ".join(tasks) + ".")
        time.sleep(1)
    else:
        print("This to-do list has no tasks!")  # Warns the user if the to-do list is empty.
        time.sleep(1)

def quit():
    print("Exiting the program...")
    time.sleep(1)

def not_command():
    print("That isn't a command!")
    time.sleep(1)

while True:  # Repeat forever

    command = input("Enter a command: ")  # Opens the command prompt.

    if command == "add":  # Executes the code below if the command is 'add'.
        add_task()
    elif command == "remove":  # Executes the code below if the command is 'remove'.
        remove_task()
    elif command == "change":  # Executes the code below if the command is 'change'.
        change_task()
    elif command == "complete":  # Executes the code below if the command is 'complete'.
        complete_task()
    elif command == "clear":  # Executes the code below if the command is 'clear'.
        clear_tasks()
    elif command == "list":  # Executes the code below if the command is 'list'.
        list_tasks()
    elif command == "quit":  # Executes the code below if the command is 'quit'.
        quit()
        break
    else:  # Executes the code below if the command doesn't exist.
        not_command()

# aight bye
