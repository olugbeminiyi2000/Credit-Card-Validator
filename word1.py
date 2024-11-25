I am a software engineer at Dailyshift, tasked with building an efficient task management system in Python. My first task is to load previous tasks from a tasks.json file using the load_tasks() function. However, this function crashes with a JSONDecodeError when it attempts to read a corrupted or partially written JSON file. To address this, I tried saving tasks using the save_tasks() function, but it silently fails to write data if the file system has restricted permissions, leading to unsaved tasks without any warning or error message. Update both functions to handle these scenarios gracefully, ensuring the program remains robust and provides clear error feedback to the user.

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
            json.dump(self.tasks, file, indent=2)

```
