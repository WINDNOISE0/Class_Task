from faker import Faker


class Person:
    faker = Faker()

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def __str__(self):
        return f"{self._first_name} {self._last_name}"

    @classmethod
    def create_random_person(cls):
        return cls(
            first_name=cls.faker.first_name(),
            last_name=cls.faker.last_name()
        )

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, new_first_name):
        self._first_name=new_first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, new_last_name):
        self._last_name=new_last_name
