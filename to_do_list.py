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
