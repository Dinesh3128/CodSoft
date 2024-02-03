import json
from datetime import datetime

# Function to load tasks from the 'tasks.json' file
def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

# Function to save tasks to the 'tasks.json' file
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=2)

# Function to display the list of tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("To-Do List:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['title']} - {task['deadline']}")

# Function to add a new task
def add_task():
    title = input("Enter task title: ")
    deadline_str = input("Enter task deadline (YYYY-MM-DD HH:MM): ")

    try:
        deadline = datetime.strptime(deadline_str, "%Y-%m-%d %H:%M")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD HH:MM.")
        return

    tasks = load_tasks()
    tasks.append({'title': title, 'deadline': deadline_str})
    save_tasks(tasks)
    print("Task added successfully.")

# Function to update an existing task
def update_task():
    tasks = load_tasks()
    display_tasks(tasks)

    # Get the index of the task to update
    task_index = int(input("Enter the index of the task you want to update: ")) - 1

    # Check if the entered index is valid
    if 0 <= task_index < len(tasks):
        # Get new title and deadline from the user
        new_title = input("Enter new task title (leave empty to keep the same): ")
        new_deadline_str = input("Enter new task deadline (YYYY-MM-DD HH:MM, leave empty to keep the same): ")

        # Update task information if new values are provided
        if new_title:
            tasks[task_index]['title'] = new_title
        if new_deadline_str:
            try:
                new_deadline = datetime.strptime(new_deadline_str, "%Y-%m-%d %H:%M")
                tasks[task_index]['deadline'] = new_deadline_str
            except ValueError:
                print("Invalid date format. Deadline not updated.")

        # Save the updated tasks to the file
        save_tasks(tasks)
        print("Task updated successfully.")
    else:
        print("Invalid task index.")

# Main function that runs the program
def main():
    while True:
        print("\n1. Display Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Exit")

        # Get user's choice
        choice = input("Enter your choice (1/2/3/4): ")

        # Perform actions based on user's choice
        if choice == '1':
            tasks = load_tasks()
            display_tasks(tasks)
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
