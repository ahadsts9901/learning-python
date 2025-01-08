class Student:
    language = "python"
    
    def __init__(self, language):
        self.language = language

    def get_lang(self):
        print(f"language is {self.language}")



class Tutor(Student):
    student = 0

    def __init__(self, students):
        self.students = students

    def get_students(self):
        print(f"students are {self.students}")


class Admin(Tutor):
    students = 0
    tutors = 0

    def __init__(self, tutors):
        self.tutors = tutors

    def get_tutors(self):
        print(f"tutors are {self.tutors}")


student = Student("javascript")
student.get_lang()

tutor = Tutor(34)
tutor.get_lang()
tutor.get_students()

admin = Admin(4)
admin.get_lang()
admin.get_tutors()
admin.get_students()
