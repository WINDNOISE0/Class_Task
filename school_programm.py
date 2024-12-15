from person.person import Persons
from role.students import Student
from role.teachers import Teacher
from school.action import SocialAction


first_student_man = Student()
second_student_woman = Student()
third_student_man = Student()

first_teacher_man = Teacher()

c71nfs_class = SocialAction().create_class(
    first_teacher_man,
    first_student_man,
    second_student_woman,
    third_student_man
)

teacher_action = c71nfs_class.teacher
student_action = c71nfs_class.students

number_tusk = c71nfs_class.teacher.document.get_number_task()
student_count = len(c71nfs_class.students)
teacher_action.start_teacher_day()

for student in student_action:
    student_action[student].start_school_day()
    student_action[student].start_learning(number_tusk)
    teacher_action.give_score(student, number_tusk)

