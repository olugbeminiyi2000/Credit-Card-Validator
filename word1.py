Here is the summary of the changes made to the code block and the explanation of it's time complexity.


### Explanation of Bugs Fixed:
1. **`mark_task_completed` Method:**  
   The initial bug was that after marking a task as completed, the task list was not being saved. This caused the changes to be lost when the program continued. The fix added a call to `self.save_tasks()` to ensure that the updated task list is saved after the completion status is updated.  
   
2. **`delete_task` Method:**  
   In the original code, deleting a task within the loop modified the list, causing subsequent tasks to be skipped. This was because when a task was deleted, the list shrank, and the loop index continued to the next item, skipping the one right after the deleted task. The fix was to exit the loop after deleting a task using a `break` statement to avoid modifying the list during iteration and causing unintended behavior.


```python
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
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()
```


### Time Complexity:

1. **`mark_task_completed` Method:**  
   - **Time Complexity:** `O(n)`, where `n` is the number of tasks in the list. The method iterates through the list of tasks to find the task with the given `task_id`. Once the task is found, the status is updated, and the task list is saved, which is an `O(1)` operation. Hence, the overall time complexity is linear relative to the number of tasks.

2. **`delete_task` Method:**  
   - **Time Complexity:** `O(n)`, where `n` is the number of tasks. The method iterates through the task list to find the task to delete, and deletion itself takes constant time (`O(1)`). After deleting the task, the updated list is saved, which is also an `O(1)` operation. Thus, the overall time complexity is linear in terms of the number of tasks.


This structure ensures both methods work correctly and efficiently, fixing the previous bugs and ensuring the task list is updated and saved correctly after each operation. The time complexity of both methods is linear, making them suitable for handling reasonably sized task lists.
