class Student:
    def __init__(self, JPA_id, JPA_name, JPA_course):
        self.JPA_id = JPA_id
        self.JPA_name = JPA_name
        self.JPA_course = JPA_course

    def display_info(self):
        print(self.JPA_id, self.JPA_name, self.JPA_course)

    #JohnPaulArcilla