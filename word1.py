Here’s an updated and documented version of the `Facade design pattern` implementation, addressing the issues described in the prompt.


### Explanation of the Changes:
1. **Separation of Concerns**: 
   - The `UniversitySystem` class is only responsible for core business logic like adding students, enrolling in courses, and assigning grades. It doesn't deal with the user interface or menu handling.
   - The `UniversitySystemFacade` class handles all the user interaction, displaying the menu, and calling the appropriate methods on `UniversitySystem`. This class serves as a **Facade** that simplifies the user interface to interact with the system.

2. **Extensibility**:
   - If you wanted to add additional functionality, like updating a student's information or viewing course details, you could do so in the `UniversitySystemFacade` without modifying the `UniversitySystem` class itself.
   - The `main_menu` is now much cleaner, and you can add more menu options without interfering with the core logic of the system.

3. **Clean Design**:
   - This design follows the **Facade Pattern** as it provides a simplified interface (`UniversitySystemFacade`) that hides the complexities of interacting with the core system (`UniversitySystem`).
   - If you need to change the underlying system, like switching from file-based storage to a database, you can do so in the `UniversitySystem` class without affecting the user-facing menu logic in `UniversitySystemFacade`.


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
        """
        Assign a grade to a student in a particular course.
        Ensures that the grade is a valid numeric value between 0 and 100.

        Parameters:
        - student_id (str): The ID of the student.
        - course_id (str): The ID of the course.
        - grade (int): The grade to assign to the student.
        """
        student = self.students.get(student_id)
        if student and course_id in student['courses']:
            try:
                # Attempt to convert the grade to a float
                grade = float(grade)
                if 0 <= grade <= 100:
                    student['courses'][course_id]['grade'] = grade
                    print(f"Grade '{grade}' assigned to student '{student_id}' for course '{course_id}'.")
                    self.save_data()
                else:
                    print("Error: Grade must be between 0 and 100.")
            except ValueError:
                print("Error: Invalid grade. Please enter a numeric value.")
        else:
            print(f"Error: Could not assign grade. Student '{student_id}' or course '{course_id}' not found.")

            
class UniversitySystemFacade:
    """
    A facade class to simplify interactions with the underlying `UniversitySystem` class.
    It abstracts the core logic of student and course management and provides a simple 
    interface for users to interact with the university system through a menu.
    
    This class encapsulates the complexity of the system's operations, presenting a 
    simplified API to the user, and allows the system to be extended or modified 
    more easily without affecting the user interface logic.
    """
    
    def __init__(self):
        """
        Initializes the facade by creating an instance of the `UniversitySystem` class.
        
        This serves as a wrapper around the core system to handle user input and delegate
        tasks like adding students, adding courses, enrolling students, and assigning grades.
        """
        # Instantiate the underlying system class
        self.system = UniversitySystem()

    def display_menu(self):
        """
        Displays the main menu for the University Management System and handles 
        user interaction through input. Based on user choices, the appropriate methods 
        are called from the `UniversitySystem` class to perform system operations.
        
        This method runs in a loop until the user decides to exit.
        """
        while True:
            # Display menu options to the user
            print("\nUniversity Management System")
            print("1. Add Student")
            print("2. Add Course")
            print("3. Enroll Student in Course")
            print("4. View Student's Courses and Grades")
            print("5. Assign Grade to Student")
            print("6. Exit")
            
            # Get the user's choice from the menu
            choice = input("Enter your choice: ")

            if choice == "1":
                # Add a student to the system
                self.add_student()
            elif choice == "2":
                # Add a student to the system
                self.add_course()
            elif choice == "3":
                # Enroll a student in a course
                self.enroll_student()
            elif choice == "4":
                # View student's courses and grades
                self.view_student_courses_and_grades()  
            elif choice == "5":
                # Assign a grade to a student
                self.assign_grade()
            elif choice == "6":
                # Exit message
                print("Exiting the system. Goodbye!")
                # Save data before exit
                self.system.save_data()
                break  # Exit the loop and terminate the program
            else:
                print("Invalid choice. Please try again.")

    def add_student(self):
        """
        Handles the logic for adding a student to the system. Prompts the user 
        to input student ID and name, and then calls the `add_student` method 
        from the `UniversitySystem` class to actually add the student.
        """
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        self.system.add_student(student_id, name)  

    def add_course(self):
        """
        Handles the logic for adding a course to the system. Prompts the user 
        to input course ID and course name, and then calls the `add_course` method 
        from the `UniversitySystem` class to actually add the course.
        """
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        self.system.add_course(course_id, course_name)

    def enroll_student(self):
        """
        Handles the logic for enrolling a student in a course. Prompts the user 
        to input student ID and course ID, then delegates the task of enrolling 
        the student to the `enroll_student` method of the `UniversitySystem` class.
        """
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")
        self.system.enroll_student(student_id, course_id)

    def assign_grade(self):
        """
        Handles the logic for assigning a grade to a student in a particular course. 
        Prompts the user to input student ID, course ID, and grade, and then calls 
        the `assign_grade` method of the `UniversitySystem` class to actually assign 
        the grade to the student.
        """
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")
        grade = input("Enter grade: ")
        self.system.assign_grade(student_id, course_id, grade)

    def view_student_courses_and_grades(self):
        """
        Handles the logic for viewing a student's enrolled courses and their grades. 
        Prompts the user to input a student ID, then retrieves and displays the 
        list of courses along with the respective grades from the `UniversitySystem` class.
        """
        student_id = input("Enter student ID: ")
        self.system.view_student_courses_and_grades(student_id)  

if __name__ == "__main__":
    # Start the facade which will handle user interactions
    facade = UniversitySystemFacade()
    facade.display_menu()
```
