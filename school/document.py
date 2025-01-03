import json
from datetime import datetime
from faker import Faker


class Document:
    DATA_FORMAT = "%d.%m.%Y"
    faker = Faker()

    def __init__(
            self,
            task_template: str,
            journal_place: str,
            minimum_grade: int = 1,
            maximum_grade: int = 5
    ):
        self.task_template = task_template
        self.minimum_grade = minimum_grade
        self.maximum_grade = maximum_grade
        self.journal_place = journal_place

    def get_journal(self):
        try:
            with open(self.journal_place, "r") as file:
                journal_file = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            journal_file = {"data": []}

        return journal_file

    def get_number_task(self):
        """Генерирует рандомный номер таски формата TASK_TEMPLATE"""
        task_number = self.faker.bothify(text=self.task_template)
        return task_number

    @staticmethod
    def get_now_date():
        """Получить текущую дату"""
        now_date = datetime.now().strftime(Document.DATA_FORMAT)
        return now_date

    def input_grade_main_journal(self, grade, student_data, task_id):
        """Добавляет в общий журнал оценку студента за выполненную задачу"""

        journal_file = self.get_journal()
        now_date = self.get_now_date() # вроде не создается у экземпляра, но по цепочки через экземпляр находит у класса
        # корректно ли вызывать через экземпляр?

        new_dct = {
            "task": task_id,
            "student": str(student_data),
            "create_at": now_date,
            "score": grade,
        }
        journal_file["data"].append(new_dct)

        with open(self.journal_place, "w") as file:
            json.dump(journal_file, file, indent=2)

            print(f"Оценка {grade} поставлена студенту {student_data}")

    def get_student_grades_journal(self, student_data):
        student_grades = {student_data: []}
        journal_file = self.get_journal()

        for data in journal_file["data"]:

            if data["student"] == student_data:
                format_data = {"task": data["task"], "create_at": data["create_at"]}
                student_grades[student_data].append(format_data)

        return student_grades
