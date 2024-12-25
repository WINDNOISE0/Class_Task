from random import randint
from role.person import Person
from school.document import Document


class Teacher(Person):

    def __init__(self, first_name, last_name, role):
        super().__init__(first_name, last_name, role)
        self.rank_score = 0
        self.journal = (
            Document  # не уверен, что это лучшее решение, но None вероятно хуже
        )

    def get_random_grade(self):
        """Генерирует рандомную оценку"""
        rand_grade = randint(self.journal.minimum_grade, self.journal.maximum_grade)
        return rand_grade

    def get_student_grades(self, student_data):
        return self.journal.get_student_grades_journal(student_data)

    def add_journal(self, journal: Document):
        """Альтернативная инициализация породила проблему с добавлением super атрибутов
        дочернего класса при создании экземпляра. Было рассмотрено два решения:
        1. Переопределять метод create_person в дочернем классе - более громоздкий
        2. Создать метод добавления журнала к уже созданному учителю - более простой и читаемый
        """
        self.journal = journal

    def add_score(self, student_data, task_id):
        """
        Получает школьный журнал и дневник ученика.
        Добавляет туда информацию о задаче, дату и оценку

        :return кортеж с дневником ученика и оценкой
        """

        grade = self.get_random_grade()

        self.journal.input_grade_main_journal(grade, student_data, task_id)

        self.rank_score += 1
        return grade
