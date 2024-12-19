from random import randint

from role.person import Person
from school.document import Document

class Teacher(Person, Document):
    ROLE = "Teacher"

    def __init__(self, first_name=None, last_name=None):
        super().__init__(first_name, last_name)
        self.rank_score = 0
        self.print_create_log(self.ROLE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_random_grade(self):
        """Генерирует рандомную оценку"""
        rand_grade = randint(self.MINIMUM_GRADE, self.MAXIMUM_GRADE)
        return rand_grade

    def give_score(
            self,
            student_data,
            personal_journal,
            task_id
    ):
        """
        Получает школьный журанал и дневник ученика.
        Добавляет туда информацию о задаче, дату и оценку

        :return кортеж с дневником ученика и оценкой
        """

        grade = self.get_random_grade()
        self.input_grade_main_journal(grade, student_data, task_id)
        personal_journal = self.input_grade_personal_journal(grade,task_id, personal_journal)

        self.rank_score += 1

        return personal_journal, grade





