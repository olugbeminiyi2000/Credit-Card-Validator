A small development team is building a terminal-based Task Management System to help manage their daily workflow. The system stores tasks in a local JSON file, allowing users to add tasks, mark them as complete, and display task lists. Recently, during internal testing, they noticed that some functionalities aren't working correctly. Your task is to debug and fix the code to ensure it performs as expected.

Task: 
Analyze the provided Python code, identify the logical and runtime bugs, and correct them. The features involved are adding tasks and displaying tasks. The code must meet the following requirements:
1. Tasks should be added to the JSON file correctly.
2. Tasks should display with all their details.
3. Ensure proper error handling for user inputs and file operations.
4. The program should not crash unexpectedly.

Code:
```python
import json
import os

class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self, title, description=""):
        new_task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "description": description
            "completed": False
        }
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task '{title}' added successfully.")

    def display_tasks(self):
        for task in self.tasks:
            status = "Completed" if task["completed"] else "Incomplete"
            print(f"ID: {task['id']}, Title: {task['title']}, Description: {task['description']}, Status: {status}")

def main():
    manager = TaskManager()
    
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            manager.add_task(title, description)
        elif choice == '2':
            manager.display_tasks()
        elif choice == '3':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice, please enter a valid option.")

if __name__ == "__main__":
    main()
```
### Constraints:
- Do not add new features.
- Use only built-in Python libraries.
- Maintain the functionality described in the task requirements.
