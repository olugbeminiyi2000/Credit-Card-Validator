import json
import os
from datetime import datetime, timedelta

class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        # Check if file exists and is not empty
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            with open(self.filename, 'r') as file:  # Open in read mode, not write mode
                return json.load(file)
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:  # Open in write mode, not read mode
            json.dump(self.tasks, file, indent=2)

    def add_task(self, title, description=""):
        if not title.strip():  # Check if title is empty
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

    def assign_priority(self, title, description):
        keywords = ["urgent", "important", "high"]
        combined = (title + " " + description).lower()
        if any(keyword in combined for keyword in keywords):
            return "High"
        return "Medium" if len(combined) > 20 else "Low"

    def check_overdue_tasks(self):
        now = datetime.now()
        for task in self.tasks:
            created_time = datetime.fromisoformat(task["created_at"])
            if not task["completed"] and now - created_time > timedelta(minutes=3):
                task["overdue"] = True  # Set overdue to True if task is overdue
                print(f"Notification: Task '{task['title']}' is overdue!")
        self.save_tasks()

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            # Sort tasks by priority before displaying
            sorted_tasks = sorted(self.tasks, key=lambda x: ["Low", "Medium", "High"].index(x["priority"]), reverse=True)
            for task in sorted_tasks:
                status = "Completed" if task["completed"] else "Incomplete"
                overdue = "Overdue" if task.get("overdue") else "On Time"  # Use "overdue" instead of "overdues"
                print(f"ID: {task['id']}, Title: {task['title']}, Status: {status}, Priority: {task['priority']}, {overdue}")

    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):  # Enumerate over self.tasks, not task_id
            if task['id'] == task_id:
                del self.tasks[i]
                self.save_tasks()
                print(f"Task with ID {task_id} deleted.")
                return
        print(f"Task with ID {task_id} not found.")

    def mark_task_completed(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:  # Compare task['id'] with task_id, not task["id"]
                task['completed'] = True
                task['overdue'] = False  # Set overdue to False when task is completed
                self.save_tasks()
                print(f"Task with ID {task_id} marked as completed.")
                return
        print(f"Task with ID {task_id} not found.")

def main():
    manager = TaskManager()
    
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Check Overdue Tasks")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            manager.add_task(title, description)
        elif choice == '2':
            manager.display_tasks()
        elif choice == '3':
            task_id = int(input("Enter the task ID to delete: "))
            manager.delete_task(task_id)
        elif choice == '4':
            task_id = int(input("Enter the task ID to mark as completed: "))
            manager.mark_task_completed(task_id)
        elif choice == '5':
            manager.check_overdue_tasks()
        elif choice == '6':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
