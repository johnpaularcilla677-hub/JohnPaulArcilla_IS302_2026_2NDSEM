class Person_jpa:
    def __init__(self_jpa, name_jpa, age_jpa):
        self_nbs.name_jpa = name_jpa
        self_nbs.age_jpa = age_jpa

    def display_info_jpa(self_jpa):
        print("Name:", self_jpa.name_jpa)
        print("Age:", self_jpa.age_jpa)

class Student_jpa(Person_jpa):
    def __init__(self_jpa, name_jpa, age_jpa, course_jpa):
        super().__init__(name_jpa, age_jpa)
        self_jpa.course_jpa = course_jpa

    def display_info_jpa(self_jpa):
        super().display_info_jpa()
        print("Course:", self_jpa.course_jpa)

class Teacher_nbs(Person_jpa):
    def __init__(self_jpa, name_jpa, age_jpa, subject_jpa):
        super().__init__(name_jpa, age_jpa)
        self_nbs.subject_jpa = subject_jpa

    def display_info_jpa(self_jpa):
        super().display_info_jpa()
        print("Subject:", self_jpa.subject_jpa)

# Example usage
student_jpa = Student_jpa("Maria", 20, "BSIS")
teacher_jpa = Teacher_jpa("Mr. Smith", 45, "Mathematics")

print("Student Info:")
student_nbs.display_info_nbs()
print("\nTeacher Info:")
teacher_nbs.display_info_nbs()
