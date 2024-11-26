PROMPT 1:
As an Automation Engineering intern at Dreamfyre University, I was tasked with enhancing a console-based application used to manage students and courses. While reviewing the JSON file that temporarily stores data, I noticed that some students had missing IDs and names. To investigate, I ran the console application and tested its functionality for adding new students. During this test, I discovered that the system allows students to be added with empty IDs and empty names. This issue is the root cause of students with invalid data, creating significant problems when trying to reference or manage these students in other operations.

Similarly, while adding a course, I observed that the application overwrites existing courses when the same course ID is assigned a different course name, and also I can add courses with empty course id and course name. This inconsistency erases previous data, stores invalid data and makes it impossible to maintain accurate records. It could also cause confusion when implementing other features, such as enrolling students or viewing course details.

I want you to debug and fix these issues by ensuring that student IDs and names are valid and meaningful before adding a student. Additionally, prevent the overwriting of course data by disallowing duplicate course IDs with conflicting names.


```python
import sys
import json
import os


class UniversitySystem:
    def __init__(self, data_file="university_data.json"):
        # File to store persistent data
        self.data_file = data_file
        # Initialize dictionaries to store student and course data
        self.students = {}
        self.courses = {}
        # Load data from file if it exists
        self.load_data()

    def load_data(self):
        """Load student and course data from a JSON file."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, "r") as file:
                    data = json.load(file)
                    self.students = data.get("students", {})
                    self.courses = data.get("courses", {})
                    print("Data loaded successfully.")
            else:
                print("Data file not found. Starting with an empty system.")
        except json.JSONDecodeError:
            print("Data file is corrupted or empty. Starting with an empty system.")
        except Exception as e:
            print(f"An unexpected error occurred while loading data: {e}")

    def save_data(self):
        """Save student and course data to a JSON file."""
        try:
            with open(self.data_file, "w") as file:
                data = {
                    "students": self.students,
                    "courses": self.courses
                }
                json.dump(data, file, indent=4)
                print("Data saved successfully.")
        except Exception as e:
            print(f"An error occurred while saving data: {e}")

    def add_student(self, student_id, name):
        if student_id in self.students:
            print("Student ID already exists.")
        else:
            self.students[student_id] = {"name": name, "courses": {}}
            print(f"Student '{name}' added successfully.")
            # Save changes after adding a student
            self.save_data()

    def add_course(self, course_id, course_name):
        self.courses[course_id] = {"name": course_name}
        print(f"Course '{course_name}' added successfully.")
        # Save changes after adding a course
        self.save_data()

    def main_menu(self):
        while True:
            print("\nUniversity Management System")
            print("1. Add Student")
            print("2. Add Course")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                student_id = input("Enter student ID: ")
                name = input("Enter student name: ")
                self.add_student(student_id, name)
            elif choice == "2":
                course_id = input("Enter course ID: ")
                course_name = input("Enter course name: ")
                self.add_course(course_id, course_name)
            elif choice == "3":
                print("Exiting the system. Goodbye!")
                self.save_data()
                sys.exit()
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    system = UniversitySystem()
    system.main_menu()

```
