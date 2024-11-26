Here’s the updated and fixed code where we directly take a student ID as input and validate it to ensure it is non-empty, unique, and meaningful. Directly addresses the issues of empty or duplicate student IDs, course IDs and course overwrites. 

### **Fixed Code**

```python
import sys
import json
import os

class UniversitySystem:
    """
    A class to manage a university system for students and courses, 
    with persistent data storage in a JSON file.
    """

    def __init__(self, data_file="university_data.json"):
        """
        Initialize the UniversitySystem.

        Parameters:
        - data_file (str): The path to the JSON file used for persistent data storage.
        """
        self.data_file = data_file  # File to store persistent data
        self.students = {}         # Dictionary to store student data
        self.courses = {}          # Dictionary to store course data
        self.load_data()           # Load data from file upon initialization

    def load_data(self):
        """
        Load student and course data from a JSON file.
        Handles scenarios where the file is missing, empty, or corrupted.
        """
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
        """
        Save student and course data to a JSON file.
        Handles unexpected errors during the save process.
        """
        try:
            with open(self.data_file, "w") as file:
                data = {
                    "students": self.students,
                    "courses": self.courses,
                }
                json.dump(data, file, indent=4)
                print("Data saved successfully.")
        except Exception as e:
            print(f"An error occurred while saving data: {e}")

    def validate_student_id(self, student_id):
        """
        Validate the student ID to ensure it is non-empty and unique.

        Parameters:
        - student_id (str): The student ID to validate.

        Returns:
        - bool: True if the student ID is valid, False otherwise.
        """
        if not student_id.strip():
            print("Error: Student ID cannot be empty or whitespace.")
            return False
        if student_id in self.students:
            print("Error: Student ID already exists. Please use a unique ID.")
            return False
        return True

    def add_student(self, student_id, name):
        """
        Add a student to the system after validating the input.

        Parameters:
        - student_id (str): The unique ID of the student.
        - name (str): The name of the student.

        Validates:
        - Student ID is non-empty and unique.
        - Student name is non-empty.
        """
        if not self.validate_student_id(student_id):
            return
        if not name.strip():
            print("Error: Student name cannot be empty or whitespace.")
            return

        # Add the student to the system
        self.students[student_id] = {"name": name.strip(), "courses": {}}
        print(f"Student '{name}' added successfully with ID: {student_id}")
        self.save_data()  # Save changes to the data file

    def validate_course_id(self, course_id):
        """
        Validate the course ID to ensure it is non-empty and unique.

        Parameters:
        - course_id (str): The course ID to validate.

        Returns:
        - bool: True if the course ID is valid, False otherwise.
        """
        if not course_id.strip():
            print("Error: Course ID cannot be empty or whitespace.")
            return False
        if course_id in self.courses:
            print(f"Error: Course ID '{course_id}' already exists.")
            return False
        return True

    def add_course(self, course_id, course_name):
        """
        Add a course to the system after validating the input.

        Parameters:
        - course_id (str): The unique ID of the course.
        - course_name (str): The name of the course.

        Validates:
        - Course ID is non-empty and unique.
        - Course name is non-empty.
        """
        if not self.validate_course_id(course_id):
            return
        if not course_name.strip():
            print("Error: Course name cannot be empty or whitespace.")
            return

        # Add the course to the system
        self.courses[course_id] = {"name": course_name.strip()}
        print(f"Course '{course_name}' added successfully with ID: {course_id}")
        self.save_data()  # Save changes to the data file

    def main_menu(self):
        """
        Display the main menu of the University Management System and 
        process user input to perform different operations.
        """
        while True:
            # Display the main menu options
            print("\nUniversity Management System")
            print("1. Add Student")
            print("2. Add Course")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                # Add a student
                student_id = input("Enter student ID: ")
                name = input("Enter student name: ")
                self.add_student(student_id, name)
            elif choice == "2":
                # Add a course
                course_id = input("Enter course ID: ")
                course_name = input("Enter course name: ")
                self.add_course(course_id, course_name)
            elif choice == "3":
                # Exit the system
                print("Exiting the system. Goodbye!")
                self.save_data()
                sys.exit()
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Create an instance of UniversitySystem and start the main menu
    system = UniversitySystem()
    system.main_menu()
```


### **Explanation of Fixes**

1. **Validation for Student ID**:
   - Added a `validate_student_id` method to check:
     - The student ID is non-empty (`not student_id.strip()`).
     - The student ID is unique (`student_id not in self.students`).
   - The method returns `False` if validation fails and provides appropriate error messages.

2. **Validation for Student Name**:
   - Checked that the student name is not empty (`not name.strip()`) before adding the student.
   - Displays an error message if validation fails.

3. **Validation for Course ID**:
   - Added a `validate_course_id` method to check:
     - The course ID is non-empty (`not course_id.strip()`).
     - The course ID is unique (`course_id not in self.courses`).

4. **Prevention of Overwriting Course Data**:
   - `validate_course_id` ensures that duplicate course IDs are not allowed.
   - Displays an error message if a duplicate course ID is entered.

5. **Save Data after Every Modification**:
   - The `save_data` method is called after adding a student or course to persist changes to the JSON file.

6. **Improved User Experience**:
   - Clear error messages inform users why their input is invalid.
   - Streamlined validation logic makes the code cleaner and more maintainable.


### **How It Works**
- **Adding a Student**:
  1. User enters a student ID and name.
  2. The `validate_student_id` method checks the ID's validity.
  3. If valid, the student is added, and changes are saved to the JSON file.

- **Adding a Course**:
  1. User enters a course ID and name.
  2. The `validate_course_id` method checks the ID's validity.
  3. If valid, the course is added, and changes are saved to the JSON file.
