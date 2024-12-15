import datetime
import json
from random import randint

from person.person import Persons
from school.action import Documents


class TeacherAction(Persons):
    def __init__(self):
        super().__init__()
        self.document = Documents()
        self.name = Persons.generate_name()
        print(f'{self} создан с именем: {self.name}')

    def __str__(self):
        return f"Teacher"

    def random_grade(self):
        rand_grade = randint(1,5)
        return rand_grade

    def check_student_task(self):
        print("Задание проверено ")


class Teacher(TeacherAction):
    def start_teacher_day(self):
        self.go_to_school(self.name, self)
        self.to_greet_everyone()

    def give_score(self, student_name, task):
        with open("./journal.json", "r") as file:
            journal_file = json.load(file)
            print(f"{task} review started by {student_name}")
            grade = self.random_grade()
            now_date = datetime.datetime.now().strftime("%d %m %Y")
            print(f"{task} review finished by {student_name}")
            journal_file[f"Name: {student_name}, Date: {now_date}"] = f"Score: {grade}"

            with open("./journal.json", "w") as file:
                json.dump(journal_file, file, indent=2)

            print(f"Оценка {grade} поставлена студенту {student_name}")







