class Student_jpa:
    def __init__(self_jpa, name_jpa, student_id_jpa, gpa_jpa):
        self_jpa.__name = name_jpa
        self_jpa.__student_id = student_id_jpa
        self_jpa.__gpa = gpa_jpa

    def get_student_info_jpa(self_jpa):
        print("Name:", self_jpa.__name)
        print("Student ID:", self_jpa.__student_id)
        print("GPA:", self_jpa.__gpa)

student1_jpa = Student_jpa("Juan", "2023-001", 1.75)
student1_jpa.get_student_info_jpa()
