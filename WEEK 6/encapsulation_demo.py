class Person_jpa:
    def __init__(self_nbs, name_jpa, age_jpa):
        self_jpa.__name = name_jpa
        self_jpa.__age = age_jpa

    def get_name_jpa(self_jpa):
        return self_jpa.__name

    def get_age_jpa(self_jpa):
        return self_jpa.__age

p1_nbs = Person_jpa("Maria", 20)
print("Name:", p1_jpa.get_name_nbs())
print("Age:", p1_jpa.get_age_nbs())
