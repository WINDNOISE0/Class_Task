from faker import Faker

class Person:
    faker = Faker()

    def __init__(self, first_name, last_name):
        if first_name is None:
            first_name = self.faker.first_name()
        if last_name is None:
            last_name = self.faker.last_name()

        self.first_name = first_name
        self.last_name = last_name


    def print_create_log(self, role):
        """Выводит лог при создании персоны"""
        print(f"Персона {self.first_name} {self.last_name} создана успешно. Роль персоны: {role} ")

    def get_person_data(self, role):
        """Возвращает данные о персоне"""
        return f'First name: {self.first_name} | Last name: {self.last_name} | Role: {role}'


