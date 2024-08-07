class Student:
    def __init__ (self, student_name, age, grade):
        self.student_name = student_name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f'Name: {self.student_name} Age: {self.age} Grade: {self.grade}'


class Course:
    def __init__(self, course_name, instructor, students:list=[]):
        self.course_name = course_name
        self.instructor = instructor
        self._students = students

    def add_student(self, student_name, age, grade):
        student = Student(student_name, age, grade)
        self._students.append(student)

    def update_student(self, name, age = 0, grade = 0):
        for student in self._students:
            if name.lower() == student.student_name.lower():
                if age:
                    student.age = age
                if grade:
                    student.grade = grade
        else:
            print('Student is not in this course')
    
    def remove_student(self, name):
        for student in self._students:
            if name.lower() == student.student_name.lower():
                self._students.remove(student)
                return
        else:
            print('Student is not in this course')

    @property
    def students(self):
        if self._students:
            for student in self._students:
                print(student)
        else:
            print('There are no students in the course')
    
                    