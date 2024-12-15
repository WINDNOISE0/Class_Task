from faker import Faker

class Documents:
    def get_number_task(self):
        faker = Faker()
        task_number = faker.bothify(text="Task-###")
        return task_number


class SocialAction:
    def __init__(self):
        self.teacher = None
        self.students = []
        self.class_name = None

    def create_class(self, teacher:object,  *students_args):
        self.teacher = teacher
        self.students = {student.name: student for student in students_args}

        print(f"Класс создан")
        return self
