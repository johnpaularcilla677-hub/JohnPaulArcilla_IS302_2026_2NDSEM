class Animal_jpa:
    def __init__(self_jpa, name_jpa):
        self_jpa.name_jpa = name_jpa

    def speak(self_jpa):
        print(self_jpa.name_jpa, "makes a sound")

class Dog_jpa(Animal_jpa):
    def bark(self_jpa):
        print(self_jpa.name_jpa, "barks")

dog1_jpa = Dog_jpa("Buddy")
dog1_jpa.speak()
dog1_jpa.bark()
