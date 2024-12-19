def input_students():
    num_students = int(input("Enter the number of students: "))
    students = []
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student DoB (YYYY-MM-DD): ")
        students.append((student_id, name, dob))
    return students

def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    courses = []
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        credit = int(input("Enter course credit: "))
        courses.append((course_id, course_name, credit))
    return courses

def input_marks(students, courses):
    print("Available courses:")
    for idx, course in enumerate(courses, start=1):
        print(f"{idx}. {course[1]}")
    selected_course = input("Enter the course ID to input marks: ")

    marks = {}
    for student in students:
        mark = float(input(f"Enter mark for {student[1]} (ID: {student[0]}): "))
        marks[student[0]] = mark
    return selected_course, marks