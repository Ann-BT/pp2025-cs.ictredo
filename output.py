def list_students(students):
    print("List of students:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")

def list_courses(courses):
    print("List of courses:")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}, Credits: {course[2]}")

def show_student_marks(marks, students, selected_course):
    print(f"Marks for Course ID {selected_course}:")
    for student in students:
        mark = marks.get(student[0], "N/A")
        print(f"{student[1]} (ID: {student[0]}): {mark}")