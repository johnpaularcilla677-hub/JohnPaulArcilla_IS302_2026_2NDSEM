class Person_jpa:
    def __init__(self_jpa, name_jpa, age_jpa):
        self_jpa.name_jpa = name_jpa
        self_jpa.age_jpa = age_jpa

class Student_jpa(Person_jpa):
    def __init__(self_jpa, name_jpa, age_jpa, course_jpa):
        super().__init__(name_jpa, age_jpa)
        self_nbs.course_jpa = course_jpa

    def display_student_jpa(self_jpa):
        print("Name:", self_jpa.name_jpa)
        print("Age:", self_jpa.age_jpa)
        print("Course:", self_jpa.course_jpa)

student1_jpa = Student_jpa("Maria", 20, "BSIS")
student1_jpa.display_student_nbs()
