from role.parent import Parent
from role.student import Student
from role.teacher import Teacher
from school.document import Document

school_journal = Document("Task-###", 1, 5, "./journal.json", "%d.%m.%Y")
first_student = Student.create_random_person("Student")
second_student = Student.create_simple_person("Christina", "Nelson", "Student")

first_teacher = Teacher.create_random_person("Teacher")

first_parent = Parent.create_random_person("Parent")

first_teacher.add_journal(school_journal)
task = first_teacher.journal.get_number_task()

first_parent.add_child(str(second_student))

first_parent.get_grades(str(second_student), first_teacher)
first_parent.get_student_experience(second_student)

first_student.learning(first_teacher, task)
second_student.learning(first_teacher, task)
