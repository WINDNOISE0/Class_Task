from role.person import Person


class Student(Person):
    ROLE = "Student"

    def __init__(self, first_name=None, last_name=None):
        super().__init__(first_name, last_name)
        self.class_number = None
        self.grades = {}
        self.experience = 0
        self.print_create_log(self.ROLE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def learning(self, teacher, task_id):
        """
        Имитирует выполнение задачи. Передает номер задачи и дневник учителю. \
        Получает оценку и заполненный дневник. Суммирует все оценки студента.
        """
        print(f"{self} finished {task_id}")
        self.grades, grade = teacher.give_score(self, self.grades, task_id)
        self.experience += grade


