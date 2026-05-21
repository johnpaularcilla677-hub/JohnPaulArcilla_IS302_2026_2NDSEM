class JPA_Animal:
    def speak(self):
        print("Animal makes a sound")


class JPA_Dog(JPA_Animal):
    def speak(self):
        print("Dog barks")


class JPA_Cat(JPA_Animal):
    def speak(self):
        print("Cat meows")


JPA_animals = [JPA_Dog(), JPA_Cat()]

for JPA_animal in JPA_animals:
    JPA_animal.speak()

    #JohnPaulArcilla