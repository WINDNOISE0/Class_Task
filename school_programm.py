from role.students import Student
from role.teachers import Teacher

first_student = Student()
first_teacher = Teacher()

task = first_teacher.get_number_task()
first_student.learning(first_teacher, task)
