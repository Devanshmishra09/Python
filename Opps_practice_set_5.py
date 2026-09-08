# 9. Create a University Course Management System.
#    Implement Student, Professor, Course, and Department classes.
#    Support course enrollment, dropping courses, and assigning professors.

from pyclbr import Class


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.enrolled_courses = []

    def enroll_course(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            course.add_student(self)
            print(f"{self.name} has enrolled in {course.course_name}.")
        else:
            print(f"{self.name} is already enrolled in {course.course_name}.")

    def drop_course(self, course):
        if course in self.enrolled_courses:
            self.enrolled_courses.remove(course)
            course.remove_student(self)
            print(f"{self.name} has dropped {course.course_name}.")
        else:
            print(f"{self.name} is not enrolled in {course.course_name}.")

class Professor:
    def __init__(self, name, professor_id):
        self.name = name
        self.professor_id = professor_id
        self.courses_taught = []

    def assign_course(self, course):
        if course not in self.courses_taught:
            self.courses_taught.append(course)
            course.assign_professor(self)
            print(f"{self.name} has been assigned to teach {course.course_name}.")
        else:
            print(f"{self.name} is already teaching {course.course_name}.")
class course:
    def