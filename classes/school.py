from classes.staff import Staff
from classes.students import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.all_members()
        self.students = Student.all_members() #[Student, Student, Student]

    def list_students(self):
        for idx, stud in enumerate(self.students):
            print(f"{idx +1}. {stud.name} {stud.school_id}")

    def find_student_by_id(self, student_id):
        for stud in self.students:
            if student_id == stud.school_id:
                return stud
        print("""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This ID doesn't match any students!!!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
        
    def add_student(self, student_data):
        new_student = Student(**student_data)
        self.students.append(new_student)