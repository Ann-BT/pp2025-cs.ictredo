import os
import pickle
import zlib
from input import input_students, input_courses, input_marks
from output import list_students, list_courses, show_student_marks
from domains import Student, Course

DATA_FILE = "students.dat"

def save_data(students, courses, marks):
    """Serialize and compress data, then save to file."""
    data = {'students': students, 'courses': courses, 'marks': marks}
    with open(DATA_FILE, "wb") as file:
        compressed_data = zlib.compress(pickle.dumps(data))
        file.write(compressed_data)
    print("Data saved successfully!")

def load_data():
    """Load and decompress data if file exists."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "rb") as file:
            compressed_data = file.read()
            data = pickle.loads(zlib.decompress(compressed_data))
        print("Data loaded successfully!")
        return data['students'], data['courses'], data['marks']
    else:
        print("No data file found. Starting fresh.")
        return [], [], {}

def main():
    students, courses, marks = load_data()

    while True:
        print("\nOptions:")
        print("1. Input students")
        print("2. Input courses")
        print("3. List students")
        print("4. List courses")
        print("5. Input marks for a course")
        print("6. Show student marks")
        print("7. Save and exit")
        choice = input("Select an option: ")

        if choice == "1":
            students = input_students()
        elif choice == "2":
            courses = input_courses()
        elif choice == "3":
            list_students(students)
        elif choice == "4":
            list_courses(courses)
        elif choice == "5":
            course_id, course_marks = input_marks(students, courses)
            marks[course_id] = course_marks
        elif choice == "6":
            selected_course = input("Enter course ID to view marks: ")
            if selected_course in marks:
                show_student_marks(marks[selected_course], students, selected_course)
            else:
                print("No marks available for this course!")
        elif choice == "7":
            save_data(students, courses, marks)
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
