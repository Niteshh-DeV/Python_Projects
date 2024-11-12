# Simple To-Do List Application

# Initialize an empty list to store tasks
tasks = []

def display_tasks():
    """Display all tasks."""
    if not tasks:
        print("Your to-do list is empty!")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(tasks, start=1):
            status = "✅" if task['completed'] else "❌"
            print(f"{index}. {task['description']} [{status}]")

def add_task():
    """Add a new task."""
    task_desc = input("Enter the task description: ")
    tasks.append({'description': task_desc, 'completed': False})
    print(f"Task '{task_desc}' added to the list.")

def remove_task():
    """Remove a task by its position."""
    display_tasks()
    try:
        task_num = int(input("Enter the task number to remove: ")) - 1
        removed_task = tasks.pop(task_num)
        print(f"Task '{removed_task['description']}' removed from the list.")
    except (IndexError, ValueError):
        print("Invalid task number!")

def mark_task_complete():
    """Mark a task as complete."""
    display_tasks()
    try:
        task_num = int(input("Enter the task number to mark as complete: ")) - 1
        tasks[task_num]['completed'] = True
        print(f"Task '{tasks[task_num]['description']}' marked as complete.")
    except (IndexError, ValueError):
        print("Invalid task number!")

def main():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Complete")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            display_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            mark_task_complete()
        elif choice == '5':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a number between 1 and 5.")

# Run the main function
main()