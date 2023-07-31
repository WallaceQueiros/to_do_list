# This library allows you to interact with the operating system
import os


# Function responsible for displaying the menu
def display_menu():
    print("Menu")
    print("1. Add task")
    print("2. Mark task as completed")
    print("3. Display task list")
    print("4. Exit")


# Function responsible for adding tasks
def add_task():
    description = input("Enter the task description: ")
# Opens the file "tasks.txt" in writing mode "a"-(append) using the management context "with
# "a" mode allows adding new lines at the end of the file without overwriting existing content
    with open("tasks.txt", "a") as file:
        file.write(description + "\n")
    print("Task added successfully!")


def mark_task_completed():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readline()

        if not tasks:
            print("No tasks to mark as completed.")
            return

        print("Task List: ")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.strip()}")

        task_number = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1] = "[Completed] " + tasks[task_number - 1]
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except FileNotFoundError:
        print("No tasks registered yet.")


def display_task_list():
    try:
        with open("task.txt", "r") as file:
            tasks = file.readline()

        if not tasks:
            print("No tasks registered.")
        else:
            print("Task List: ")
            for task in tasks:
                print(f'- {task.strip()}')
    except FileNotFoundError:
        print("No tasks registered yet.")