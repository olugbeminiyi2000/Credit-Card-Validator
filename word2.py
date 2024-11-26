While testing the student-course management functionality of the application, I identified a few critical issues that need attention. In the `view_student_courses_and_grades` method, although the system correctly checks if the student ID exists, it does not handle the case where a student is found but has not yet enrolled in any courses. In such instances, the method currently displays an empty list without context, which may confuse users. The method should be updated to provide a clear message indicating that the student is not enrolled in any courses.

Additionally, I found a significant issue in the `enroll_student` method. The system allows students to be enrolled in the same course multiple times, but instead of preventing duplicate enrollments, it overwrites the previous entry. This behavior can lead to the loss of important data, such as grades, if grades were previously assigned for that course. It is crucial that the system checks whether the student is already enrolled in the course before proceeding with the enrollment, preventing overwrites and ensuring that grades are preserved.

Furthermore, when a non-existent student ID is passed to the `enroll_student` method, the system attempts to access the `courses` attribute of a `NoneType` object, which results in a `TypeError: 'NoneType' object is not subscriptable`. This error occurs because the system does not properly validate whether the student ID exists before attempting to enroll them in a course. To fix this, the method should handle the case of a missing student ID more gracefully, providing a user-friendly error message rather than crashing.

These issues need to be resolved to ensure that the student-course management system works efficiently, prevents data loss, and provides a better user experience.

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

    def view_student_courses_and_grades(self, student_id):
        """View a student's enrolled courses and grades."""
        student = self.students.get(student_id)
        if student:
            print(f"Courses for Student '{student_id}':")
            for course_id, course_info in student['courses'].items():
                print(f"{course_info['name']} - Grade: {course_info.get('grade', 'N/A')}")
        else:
            print("Student not found.")

    def enroll_student(self, student_id, course_id):
        """Enroll a student in a course."""
        student = self.students.get(student_id)
        if student:
            course = self.courses.get(course_id)
            student['courses'][course_id] = {"name": course['name'], "grade": None}
            print(f"Student '{student_id}' has been enrolled in course '{course_id}'.")
            self.save_data()
        else:
            print(f"Error: Student with ID '{student_id}' not found.")

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
            print("3. Enroll Student in Course")
            print("4. View Student's Courses and Grades")
            print("5. Exit")
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
		# enroll student
                student_id = input("Enter student ID: ")
                course_id = input("Enter course ID: ")
                self.enroll_student(student_id, course_id)
            elif choice == "4":
		# view students courses and grades
                student_id = input("Enter student ID: ")
                self.view_student_courses_and_grades(student_id)
            elif choice == "5":
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
