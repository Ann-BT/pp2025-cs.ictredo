from input import input_students, input_courses, input_marks
from output import list_students, list_courses, show_student_marks
from domains import Student, Course

def main():
    students = []
    courses = []
    marks = {}

    while True:
        print("\nOptions:")
        print("1. Input students")
        print("2. Input courses")
        print("3. List students")
        print("4. List courses")
        print("5. Input marks for a course")
        print("6. Show student marks")
        print("7. Exit")
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
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
