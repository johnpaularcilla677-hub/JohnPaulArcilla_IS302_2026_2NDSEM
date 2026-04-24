class Vehicle_jpa:
    def __init__(self_jpa, brand_jpa, model_jpa):
        self_jpa.brand_jpa = brand_jpa
        self_jpa.model_jpa = model_jpa

class Car_jpa(Vehicle_jpa):
    def __init__(self_jpa, brand_jpa, model_jpa, year_jpa):
        super().__init__(brand_jpa, model_jpa)
        self_nbs.year_jpa = year_jpa

    def display_car_jpa(self_jpa):
        print(self_jpa.brand_jpa, self_jpa.model_jpa, self_jpa.year_jpa)

car1_jpa = Car_jpa("Honda", "Civic", 2022)
car1_jpa.display_car_jpa()
