import json
import os

class TaskManager:
    """
    A class to manage tasks stored in a JSON file.

    Attributes:
    filename (str): The name of the JSON file to store tasks.
    tasks (list): A list of tasks loaded from the JSON file.
    """

    def __init__(self, filename='tasks.json'):
        """
        Initializes the TaskManager with a filename and loads tasks from the file.

        Args:
        filename (str): The name of the JSON file to store tasks. Defaults to 'tasks.json'.
        """
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """
        Loads tasks from the JSON file.

        Returns:
        list: A list of tasks loaded from the JSON file. If the file does not exist, an empty list is returned.

        Time Complexity: O(n), where n is the number of tasks in the JSON file.
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        """
        Saves tasks to the JSON file.

        Time Complexity: O(n), where n is the number of tasks in the tasks list.
        """
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=2)

    def add_task(self, title, description=""):
        """
        Adds a new task to the tasks list and saves it to the JSON file.

        Args:
        title (str): The title of the task.
        description (str): The description of the task. Defaults to an empty string.

        Time Complexity: O(n), where n is the number of tasks in the tasks list.
        """
        if not title.strip():
            print("Task title cannot be empty.")
            return

        # Fixed ID assignment logic to handle the case when the tasks list is empty
        new_task_id = max([task['id'] for task in self.tasks], default=0) + 1

        new_task = {
            "id": new_task_id,
            "title": title,
            "description": description,
            "completed": False
        }
        self.tasks.append(new_task)
        self.save_tasks()

    def display_tasks(self):
        """
        Displays all tasks in the tasks list.

        Time Complexity: O(n), where n is the number of tasks in the tasks list.
        """
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                status = "Completed" if task["completed"] else "Incomplete"
                print(f"ID: {task['id']}, Title: {task['title']}, Description: {task['description']}, Status: {status}")

    def delete_task(self, task_id):
        """
        Deletes a task with the specified ID from the tasks list and saves the updated list to the JSON file.

        Args:
        task_id (int): The ID of the task to delete.

        Time Complexity: O(n), where n is the number of tasks in the tasks list.
        """
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                del self.tasks[i]
                self.save_tasks()
                print(f"Task with ID {task_id} deleted.")
                return
        print(f"Task with ID {task_id} not found.")

def main():
    manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            manager.add_task(title, description)
        elif choice == '2':
            manager.display_tasks()
        elif choice == '3':
            # Added validation for numeric input
            while True:
                try:
                    task_id = int(input("Enter the task ID to delete: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric ID.")
            manager.delete_task(task_id)
        elif choice == '4':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
