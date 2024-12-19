class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.credits = 0
        self.marks = []

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}"

class Course:
    def __init__(self, course_id, course_name, credit):
        self.course_id = course_id
        self.course_name = course_name
        self.credit = credit

    def __str__(self):
        return f"ID: {self.course_id}, Name: {self.course_name}, Credits: {self.credit}"
    
class Marks:
    def __init__(self):
        self.marks = {}

    def input_marks(self, course, students):
        self.marks[course.course_id] = {}
        for student in students:
            mark = float(input(f"Enter mark for {student.name} (ID: {student.student_id}): "))
            self.marks[course.course_id][student.student_id] = mark

    def show_marks(self, course, students):
        if course.course_id not in self.marks:
            print(f"No marks available for course {course.course_name}.")
            return
        print(f"Marks for course {course.course_name}:")
        for student in students:
            mark = self.marks[course.course_id].get(student.student_id, "N/A")
            print(f"{student.name} (ID: {student.student_id}): {mark}")    