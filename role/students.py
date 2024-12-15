from person.person import Persons
from school.action import Documents


class StudentsActions(Persons):
    def __init__(self):
        super().__init__()
        self.document = Documents()
        self.name = Persons.generate_name()
        print(f'{self} создан с именем: {self.name}')

    def __str__(self):
        return f"Student"

    def learning(self, task_id):
        print(f"I finished {task_id}")

    def get_task(self, task_id):
        print(f'I got {task_id}')


class Student(StudentsActions):
    def start_school_day(self):
        self.go_to_school(self.name, self)
        self.to_greet_everyone()

    def start_learning(self, task_id):
        self.get_task(task_id)
        self.learning(task_id)

    def finish_school_day(self):
        self.go_to_home(self.name, self)
