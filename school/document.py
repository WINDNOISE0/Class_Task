import json
from datetime import datetime

from faker import Faker

class Document:
    TASK_TEMPLATE = "Task-###"
    MAXIMUM_GRADE = 5
    MINIMUM_GRADE = 1
    JOURNAL_PLACE = "./journal.json"
    DATA_FORMAT = "%d.%m.%Y"
    faker = Faker()

    def __init__(self):
        pass

    def get_number_task(self):
        """Генерирует рандомный номер таски формата TASK_TEMPLATE"""

        task_number = self.faker.bothify(text=self.TASK_TEMPLATE)
        return task_number

    def get_now_date(self):
        """Получить текущую дату"""

        now_date = datetime.now().strftime(self.DATA_FORMAT)
        return now_date


    def input_grade_main_journal(self, grade, student_data, task_id):
        """Добавляет в общий журнал оценку студента за выполненную задачу"""

        try:

            with open(self.JOURNAL_PLACE, "r") as file:
                journal_file = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            journal_file = {"data":[]}

        now_date = self.get_now_date()


        new_dct = {
            "task":task_id,
            "student": str(student_data),
            "create_at": now_date,
            "score": grade
        }
        journal_file["data"].append(new_dct)

        with open(self.JOURNAL_PLACE, "w") as file:
            json.dump(journal_file, file, indent=2)

            print(f"Оценка {grade} поставлена студенту {student_data}")

    def input_grade_personal_journal(self, grade, task_id, personal_journal):
        """Добавляет в дневник студента оценку за выполненную задачу"""

        now_date = self.get_now_date()
        grade_str_personal = f"{task_id}  Date: {now_date}"

        personal_journal[grade_str_personal] = grade
        return personal_journal


