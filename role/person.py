from faker import Faker


class Person:
    faker = Faker()

    def __init__(self, first_name, last_name, role):
        self.first_name = first_name
        self.last_name = last_name
        self.role = role

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def create_random_person(cls, role):
        return cls(
            first_name=cls.faker.first_name(),
            last_name=cls.faker.last_name(),
            role=role,
        )

    @classmethod
    def create_simple_person(cls, fits_name, last_name, role):
        return cls(first_name=fits_name, last_name=last_name, role=role)

    def update_person_data(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
