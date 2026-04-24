class Employee_jpa:
    def __init__(self_jpa, name_jpa, salary_jpa):
        self_jpa.name_jpa = name_jpa
        self_jpa.salary_jpa = salary_jpa

class Manager_jpa(Employee_jpa):
    def __init__(self_jpa, name_jpa, salary_jpa, department_jpa):
        super().__init__(name_jpa, salary_jpa)
        self_jpa.department_jpa = department_jpa

    def display_manager_jpa(self_jpa):
        print("Name:", self_jpa.name_jpa)
        print("Salary:", self_jpa.salary_jpa)
        print("Department:", self_jpa.department_jpa)

manager1_jpa = Manager_jpa("John", 50000, "IT")
manager1_jpa.display_manager_jpa()
