from faker import Faker

class Persons:
    @staticmethod
    def generate_name():
        faker = Faker()
        return faker.first_name()

    def to_greet_everyone(self, *args):
        if args:
            for arg in args:
                print(f"Hello {arg}")
        else:
            print("Привет всем")

    def go_to_home(self, role, name):
        print(f"I am {name} {role}  and I left home")

    def go_to_school(self, role, name):
        print(f"I am {name} {role} and I arrive to school")

