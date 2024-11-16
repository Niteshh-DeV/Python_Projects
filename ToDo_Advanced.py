import os

def load_tasks(filename="tasks.txt"):
    tasks = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                task, status = line.strip().split(" | ")
                tasks.append({"task": task, "status": status})
    return tasks

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(f"{task['task']} | {task['status']}\n")

def display_menu():
    print("\n--- To-Do List Application ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter the task description: ")
    tasks.append({"task": task, "status": "Pending"})
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\n--- Your Tasks ---")
    for idx, task in enumerate(tasks):
        print(f"{idx + 1}. {task['task']} - {task['status']}")

def mark_task_completed(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter task number to mark as completed: "))
            tasks[task_num - 1]["status"] = "Completed"
            print("Task marked as completed!")
        except (IndexError, ValueError):
            print("Invalid task number!")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter task number to delete: "))
            tasks.pop(task_num - 1)
            print("Task deleted successfully!")
        except (IndexError, ValueError):
            print("Invalid task number!")

def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()