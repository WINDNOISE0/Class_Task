from role.person import Person
from role.teacher import Teacher


class Parent(Person):
    def __init__(self, first_name, last_name, role):
        super().__init__(first_name, last_name, role)
        self.child = []

    def add_child(self, data_child):
        self.child.append(data_child)

    def get_grades(self, student_data, teacher: Teacher):
        student_grade = {}
        if student_data in self.child:
            student_grade = teacher.get_student_grades(student_data)

        return student_grade

    def get_student_experience(self, student_data):
        """Получение опыта (для примера), при единичном запуске опыт всегда будет == 0, так как объект пересоздается
        в новой программе с нулевым значением, что нельзя сказать про journal.json
        """
        if str(student_data) in self.child:
            student_experience = student_data.experience
            print(student_experience)
            return student_data.experience
