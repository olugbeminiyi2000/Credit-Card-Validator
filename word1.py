As I continue building the task manager application, I have just implemented the ability to display all tasks and check overdue tasks. The display tasks functionality is supposed to show the tasks sorted by their priority, and the overdue task check should identify tasks that are overdue based on their creation time. However, I am facing an issue where the overdue task check is not correctly identifying overdue tasks, and the display tasks function sometimes shows the wrong order of tasks based on priority, identify and fix the issues in both the display_tasks and check_overdue_tasks functions.

Here is the code with bugs below.


```python
import json
import os
from datetime import datetime, timedelta

class TaskManager:
    """
    TaskManager class for managing tasks with features such as
    saving/loading tasks, adding task based on priority, marking
    tasks as completed, deleting task from/to a JSON file.
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
        """
        Assigns a priority to the task based on its title and description.

        This method looks for specific keywords related to high priority (such as "urgent", "important", and "high"),
        but also checks if the task description contains any negations (e.g., "not") before these keywords.
        If a negation word precedes a high-priority keyword, the priority is set to "Low" to reflect the negation.
        
        Args:
        title (str): The title of the task.
        description (str): The description of the task.

        Returns:
            str: The assigned priority ("High", "Medium", "Low").
        """
        # List of high-priority keywords
        high_priority_keywords = ["urgent", "important", "high"]
        # Negation words that may affect priority
        negation_keywords = ["not", "no", "never", "none", "without", "lack"]
        
        # Combine title and description into one string and convert to lowercase
        combined = (title + " " + description).lower()

        # Check if any negation keyword appears before any high-priority keyword
        for negation in negation_keywords:
            for keyword in high_priority_keywords:
                if negation in combined and combined.index(negation) < combined.index(keyword):
                    return "Low"
        
        # Assign "High" priority if any high-priority keyword is found and no negation precedes it
        if any(keyword in combined for keyword in high_priority_keywords):
            return "High"

        # If the task description is longer than 20 characters, assign "Medium" priority
        # Otherwise, assign "Low"
        return "Medium" if len(combined) > 20 else "Low"

    def add_task(self, title, description=""):
        """
        Adds a new task with the given title and description.
        
        Args:
        title (str): The title of the task.
        description (str): A brief description of the task.
            
        If the title is empty, the task is not added.
        """
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

    def mark_task_completed(self, task_id):
        """
        Marks a task as completed by its ID and saves the updated list of tasks.
        
        Args:
        task_id (int): The ID of the task to be marked as completed.
            
        This method updates the task's status to completed, resets its overdue status to False, 
        and saves the task list to ensure the changes are persisted. 
        """
        task_found = False
        
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                task['overdue'] = False
                self.save_tasks()
                task_found = True
                print(f"Task with ID {task_id} marked as completed.")
                break
        
        if not task_found:
            print(f"Task with ID {task_id} not found.")


    def delete_task(self, task_id):
        """
        Deletes a task by its ID and saves the updated list of tasks.
        
        Args:
        task_id (int): The ID of the task to be deleted.
            
        This method removes a task from the task list by its ID and saves the task list 
        to ensure that the deletion is persisted. It handles edge cases, such as modifying the 
        list during iteration.
        """
        task_found = False
        
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                del self.tasks[i]
                self.save_tasks()
                task_found = True
                print(f"Task with ID {task_id} deleted.")
                break
        
        if not task_found:
            print(f"Task with ID {task_id} not found.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            sorted_tasks = sorted(self.tasks, key=lambda x: ["Low", "Medium", "High"].index(x["priority"]), reverse=True)
            for task in sorted_tasks:
                status = "Completed" if task["completed"] else "Incomplete"
                overdue = "Overdue" if task.get("overdue") else "On Time"
                print(f"ID: {task['id']}, Title: {task['title']}, Status: {status}, Priority: {task['priority']}, {overdue}")

    def check_overdue_tasks(self):
        now = datetime.now()
        for task in self.tasks:
            created_time = datetime.fromisoformat(task["created_at"])
            if not task["completed"] and now - created_time > timedelta(minutes=3):
                task["overdue"] = True
                print(f"Notification: Task '{task['title']}' is overdue!")
            else:
                task["overdue"] = False
        self.save_tasks()




def main():
    manager = TaskManager()
    print(f"Loaded {len(manager.tasks)} tasks.")

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            manager.add_task(title, description)
        elif choice == '2':
            task_id = int(input("Enter the task ID to delete: "))
            manager.delete_task(task_id)
        elif choice == '3':
            task_id = int(input("Enter the task ID to mark as completed: "))
            manager.mark_task_completed(task_id)
        elif choice == '4':
            manager.display_tasks()
        elif choice == '5':
            manager.check_overdue_tasks()
        elif choice == '6':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()
```
