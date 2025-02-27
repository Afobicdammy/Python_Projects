# Person


# Student
    # Attributes:
        # Student's name
        # Student's ID
        # Courses

# Instructor
    # Attributes:
        # Instructor's name
        # Instructor's ID
        # Courses

# Course
    # Atrributes: Instructor, students

# Student management system (Blackboard):
     #Manage Students
    # Manage Courses
    # Manage Enrollments

# Setting up the classes

class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def __str__(self):
         return f"Students: {self.name}, ID:{self.id_number}"
       

class Student(Person):
    def __init__(self, name, id_number, major):
        super().__init__(id_number, name)
        self.name = name
        self.id_number = id_number
        self.major = major
        self.course_list = []

    def __str__(self):
         return f" Student: {self.name}, ID:{self.id_number}, Major:{self.major}"
    
    def __repr__(self):
        return self.__str__()


class Instructor(Person):
    def __init__(self, id_number, name, department):
        super().__init__(id_number,name)
        self.department = department
        self.name = name
        self.id_number = id_number
        self.course_list = []
    
    def __str__(self) -> str:
         return f"Instructor: {self.name}, ID:{self.id_number}, Department:{self.department}"


class Course:
    def __init__(self, course_name, course_id):
        self.course_name = course_name
        self.course_id = course_id
        self.enrolled_students = []

    def add_student(self, student):
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
        else:
            print("Student already entrolled")

    def remove_student(self, student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
        else:
            print("student not found")


    def __str__(self) -> str:
         return f"Students: {self.course_name}, ID:{self.course_id}"
    
    def __repr__(self):
        return self.__str__()
      
class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.grade = None
        pass

    def assign_grades(self, grade):
        self.grade = grade
        pass

    def __str__(self):
         return f"Students: {self.student.name}, ID:{self.course.course_id}, Grade: {self.grade}"
    
   
class Blackboard:
    def __init__(self):
        self.students = []
        self.instructors = []
        self.course = []
        self.enrollments = []

    def add_student(self, student):
        self.students.append(student)
        pass

    def remove_student(self, student):
        self.students.remove(student)
        pass

    def update_student(self, student, change_name =None, Change_major = None):
        if change_name:
            student.name = change_name
        if Change_major:
            student.major = Change_major
        pass

    def add_instructor(self, instructor):
        self.instructors.append(instructor)
        pass

    def remove_instructor(self, instructor):
        self.instrctor.remove(instructor)


    def update_instructor(self, instructor, change_name = None, Change_department = None):
         if change_name:
            instructor.name = change_name
         if Change_department:
            instructor.department = Change_department

    def add_courses(self, course):
        self.courses.append(course)
        pass

    def remove_courses(self, course):
        self.courses.remove(course)
        pass

    def enroll_student(self,student,course):
        if student not in course.enrolled_students:
            course.add_student(student)
            enrollment = Enrollment(student, course)
            self.enrollments.append(enrollment)

    def assign_grade(self, student, course, grade):
        for enrollment in self.enrollments:
            if enrollment.student == student and enrollment.course == course:
                enrollment.assign_grade(grade)

    def get_course_student(self,course): # get list of students in a course
        return course.enrolled_students
    
    def get_student_course(self,student): # get the courses a student is taking
        return [enrollment.course for enrollment in self.enrollments if enrollment.student == student]

