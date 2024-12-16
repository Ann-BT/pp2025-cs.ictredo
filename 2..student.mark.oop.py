class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}"


class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

    def __str__(self):
        return f"ID: {self.course_id}, Name: {self.course_name}"


class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_students(self):
        num_students = int(input("Enter the number of students: "))
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student DoB (YYYY-MM-DD): ")
            self.students.append(Student(student_id, name, dob))

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            self.courses.append(Course(course_id, course_name))

    def input_marks(self):
        print("Available courses:")
        for idx, course in enumerate(self.courses, start=1):
            print(f"{idx}. {course}")
        selected_course = input("Enter the course ID to input marks: ")

        if selected_course not in [course.course_id for course in self.courses]:
            print("Invalid course ID!")
            return

        self.marks[selected_course] = {}
        for student in self.students:
            mark = float(input(f"Enter mark for {student.name} (ID: {student.student_id}): "))
            self.marks[selected_course][student.student_id] = mark

    def list_students(self):
        print("List of students:")
        for student in self.students:
            print(student)

    def list_courses(self):
        print("List of courses:")
        for course in self.courses:
            print(course)

    def show_student_marks(self):
        print("Available courses:")
        for idx, course in enumerate(self.courses, start=1):
            print(f"{idx}. {course}")
        selected_course = input("Enter the course ID to view marks: ")

        if selected_course not in self.marks:
            print("No marks available for this course!")
            return

        print(f"Marks for course ID {selected_course}:")
        for student in self.students:
            mark = self.marks[selected_course].get(student.student_id, "N/A")
            print(f"{student.name} (ID: {student.student_id}): {mark}")

    def run(self):
        while True:
            print("\nOptions:")
            print("1. Input students")
            print("2. Input courses")
            print("3. List students")
            print("4. List courses")
            print("5. Input marks for a course")
            print("6. Show student marks for a course")
            print("7. Exit")
            choice = input("Select an option: ")

            if choice == "1":
                self.input_students()
            elif choice == "2":
                self.input_courses()
            elif choice == "3":
                self.list_students()
            elif choice == "4":
                self.list_courses()
            elif choice == "5":
                self.input_marks()
            elif choice == "6":
                self.show_student_marks()
            elif choice == "7":
                print("Exiting the program.")
                break
            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    school = School()
    school.run()
