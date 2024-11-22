import json
import os

class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    return json.load(file)
            else:
                # Create the file if it doesn't exist
                with open(self.filename, 'w') as file:
                    json.dump([], file)
                return []
        except json.JSONDecodeError:
            print("Error: Unable to load tasks from file. Please check the file format.")
            return []

    def save_tasks(self):
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.tasks, file)
        except Exception as e:
            print(f"Error: Unable to save tasks to file. {str(e)}")

    def add_task(self, title, description=""):
        if not title:
            print("Error: Task title cannot be empty.")
            return
        
        new_task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "description": description,
            "completed": False  # Added a comma after description
        }
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task '{title}' added successfully.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        
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
            description = input("Enter task description (optional): ")
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
