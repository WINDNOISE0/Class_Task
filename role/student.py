from role.person import Person


class Student(Person):
    ROLE = "Student"

    def __init__(self, first_name, last_name, role):
        super().__init__(first_name, last_name, role)
        self.experience = 0

    def learning(self, teacher, task_id):
        """
        Имитирует выполнение задачи. Передает номер задачи и дневник учителю.
        Получает оценку и заполненный дневник. Суммирует все оценки студента.
        """
        print(f"{self} finished {task_id}")
        grade = teacher.add_score(self, task_id)
        self.experience += grade
