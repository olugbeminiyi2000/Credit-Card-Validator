I have been enhancing the University Management System, but when I tried to assign grades to students using the assign_grade method, I encountered a problem. The system allows the entry of grades that aren't valid—such as non-numeric grades or values that don’t make sense in a grading context (like negative numbers or values above 100). This is causing some inconsistent data to be saved, and it’s making it difficult for the faculty to trust the grading system


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
        """
        View a student's enrolled courses and their corresponding grades.
        If the student is not enrolled in any courses, display a meaningful message.

        Parameters:
        - student_id (str): The ID of the student to retrieve course data for.
        """
        student = self.students.get(student_id)
        if student:
            if not student['courses']:
                print(f"Student '{student_id}' is not enrolled in any courses.")
            else:
                print(f"Courses for Student '{student_id}':")
                for course_id, course_info in student['courses'].items():
                    print(f"{course_info['name']} - Grade: {course_info.get('grade', 'N/A')}")
        else:
            print(f"Student with ID '{student_id}' not found.")

    def enroll_student(self, student_id, course_id):
        """
        Enroll a student in a course if they are not already enrolled.
        Prevents the duplication of course enrollments and ensures grades are preserved.

        Parameters:
        - student_id (str): The ID of the student to enroll.
        - course_id (str): The ID of the course to enroll the student in.
        """
        student = self.students.get(student_id)
        if student:
            course = self.courses.get(course_id)
            if not course:
                print(f"Error: Course with ID '{course_id}' not found.")
                return
            if course_id in student['courses']:
                print(f"Student '{student_id}' is already enrolled in the course '{course_id}'.")
            else:
                student['courses'][course_id] = {"name": course['name'], "grade": None}
                print(f"Student '{student_id}' has been enrolled in course '{course_id}'.")
                self.save_data()
        else:
            print(f"Error: Student with ID '{student_id}' not found.")

    def assign_grade(self, student_id, course_id, grade):
        student = self.students.get(student_id)
        if student and course_id in student['courses']:
            student['courses'][course_id]['grade'] = grade
            print(f"Grade '{grade}' assigned to student '{student_id}' for course '{course_id}'.")
            self.save_data()
        else:
            print(f"Error: Could not assign grade. Student '{student_id}' or course '{course_id}' not found.")


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
            print("5. Assign Grade to Student")
            print("6. Exit")
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
                # Enroll a student in a course
                student_id = input("Enter student ID: ")
                course_id = input("Enter course ID: ")
                self.enroll_student(student_id, course_id)
            elif choice == "4":
                # View a student's courses and grades
                student_id = input("Enter student ID: ")
                self.view_student_courses_and_grades(student_id)
            elif choice == "5":
                # Assign a grade to a student course
                student_id = input("Enter student ID: ")
                course_id = input("Enter course ID: ")
                grade = input("Enter grade: ")
                self.assign_grade(student_id, course_id, grade)
            elif choice == "6":
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
