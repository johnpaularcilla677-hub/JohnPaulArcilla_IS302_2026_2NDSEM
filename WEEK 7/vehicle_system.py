class Vehicle_jpa:
    def __init__(self_jpa, brand_jpa, model_jpa):
        self_jpa.brand_jpa = brand_jpa
        self_jpa.model_jpa = model_jpa

class Car_nbs(Vehicle_nbs):
    def __init__(self_nbs, brand_nbs, model_nbs, year_nbs):
        super().__init__(brand_nbs, model_nbs)
        self_nbs.year_nbs = year_nbs

    def display_car_nbs(self_nbs):
        print(self_nbs.brand_nbs, self_nbs.model_nbs, self_nbs.year_nbs)

car1_nbs = Car_nbs("Toyota", "Corolla", 2022)
car1_nbs.display_car_nbs()
