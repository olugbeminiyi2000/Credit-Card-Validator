As a software engineer at Dailyshift, I am working on improving a task management application in Python. I've encountered a bug in my task priority logic when testing. The system is assigning "High" priority to tasks even when a word like "not" precedes high-priority keywords such as "urgent", "important", or "high". For example, if a task description contains the phrase "not urgent", the system should assign a "Low" priority instead of "High", but it continues marking the task as "High". I need help fixing this bug so that the presence of negating words like "not" properly negates the priority, assigning "Low" priority when a negation precedes high-priority keywords like "urgent" or "important". This fix will ensure the system behaves as expected and doesn't mislabel tasks.

import json
import os
from datetime import datetime

class TaskManager:
    """
    TaskManager class for managing tasks with features such as
    saving/loading tasks from a JSON file.
    """

    def __init__(self, filename='tasks.json'):
        """
        Initializes the TaskManager with the given filename for storing tasks.
        
        Args:
        filename (str): The name of the JSON file where tasks are saved.
        """
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """
        Loads the list of tasks from the JSON file.
        
        Handles JSON decoding errors and provides feedback if
        the file is corrupted.
        
        Returns:
        list: List of tasks loaded from the file, or an empty list if 
        the file doesn't exist or is corrupted.
        """
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Error: The task file is corrupted or contains invalid JSON.")
                return []  # Return empty list if JSON is invalid
            except Exception as e:
                print(f"Error loading tasks: {e}")
                return []  # Handle other unexpected errors
        else:
            print("No task file found. Starting with an empty task list.")
        return []

    def save_tasks(self):
        """
        Saves the current tasks list to the JSON file.
        
        Handles file write errors and informs the user if saving fails.
        """
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.tasks, file, indent=2)
        except PermissionError:
            print("Error: Insufficient permissions to write to the task file.")
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def assign_priority(self, title, description):
        keywords = ["urgent", "important", "high"]
        combined = (title + " " + description).lower()
        if any(keyword in combined for keyword in keywords):
            return "High"
        return "Medium" if len(combined) > 20 else "Low"


    def add_task(self, title, description=""):
        if not title.strip():
            print("Task title cannot be empty.")
            return
        
        new_task = {
            "id": self.tasks[-1]["id"] + 1 if self.tasks else 1,
            "title": title,
            "description": description,
            "completed": False,
            "created_at": datetime.now().isoformat(),
            "priority": self.assign_priority(title, description),
            "overdue": False
        }
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task '{title}' added successfully with priority: {new_task['priority']}!")


def main():
    manager = TaskManager()
    print(f"Loaded {len(manager.tasks)} tasks.")

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            manager.add_task(title, description)
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()
