import math
import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}"



class Course:
    def __init__(self, course_id, course_name, credits):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits 

    def __str__(self):
        return f"ID: {self.course_id}, Name: {self.course_name}, Credits: {self.credits}"


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
            credits = int(input("Enter course credits: ")) 
            self.courses.append(Course(course_id, course_name, credits))

    def input_marks(self):
        print("Available courses:")
        for course in self.courses:
            print(course)
        selected_course = input("Enter the course ID to input marks: ")

        # Validate course
        if selected_course not in [course.course_id for course in self.courses]:
            print("Invalid course ID!")
            return

        # Input marks
        self.marks[selected_course] = {}
        for student in self.students:
            mark = float(input(f"Enter mark for {student.name} (ID: {student.student_id}): "))
            rounded_mark = math.floor(mark)  # Round down using math
            self.marks[selected_course][student.student_id] = rounded_mark

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
        for course in self.courses:
            print(course)
        selected_course = input("Enter the course ID to view marks: ")

        if selected_course not in self.marks:
            print("No marks available for this course!")
            return

        print(f"Marks for course ID {selected_course}:")
        for student in self.students:
            mark = self.marks[selected_course].get(student.student_id, "N/A")
            print(f"{student.name} (ID: {student.student_id}): {mark}")

    def calculate_gpa(self):
        student_gpas = {}  

        for student in self.students:
            total_weighted_score = 0
            total_credits = 0
            for course in self.courses:
                course_id = course.course_id
                credits = course.credits
                if course_id in self.marks and student.student_id in self.marks[course_id]:
                    score = self.marks[course_id][student.student_id]
                    total_weighted_score += score * credits
                    total_credits += credits
            # Calculate GPA
            gpa = total_weighted_score / total_credits if total_credits > 0 else 0
            student_gpas[student.student_id] = round(gpa, 2)

        return student_gpas

    def sort_students_by_gpa(self):
        gpas = self.calculate_gpa()
        sorted_students = sorted(self.students, key=lambda student: gpas.get(student.student_id, 0), reverse=True)
        print("\nStudents sorted by GPA:")
        for student in sorted_students:
            print(f"{student.name} (ID: {student.student_id}): GPA = {gpas.get(student.student_id, 0)}")

    def run(self):
        while True:
            print("\nOptions:")
            print("1. Input students")
            print("2. Input courses")
            print("3. List students")
            print("4. List courses")
            print("5. Input marks for a course")
            print("6. Show student marks for a course")
            print("7. Calculate and display GPA")
            print("8. Sort students by GPA")
            print("9. Exit")
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
                gpas = self.calculate_gpa()
                print("\nGPA for each student:")
                for student in self.students:
                    print(f"{student.name} (ID: {student.student_id}): GPA = {gpas.get(student.student_id, 0)}")
            elif choice == "8":
                self.sort_students_by_gpa()
            elif choice == "9":
                print("Exiting the program.")
                break
            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    school = School()
    school.run()
