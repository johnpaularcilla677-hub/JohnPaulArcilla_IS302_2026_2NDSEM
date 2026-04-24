class Employee_jpa:
    def __init__(self_jpa, name_jpa):
        self_jpa.__name = name_jpa
        self_jpa.__salary = 0

    def set_salary_jpa(self_jpa, salary_jpa):
        if salary_jpa > 0:
            self_jpa.__salary = salary_jpa

    def get_salary_jpa(self_jpa):
        return self_jpa.__salary

emp_jpa = Employee_jpa("Ana")
emp_jpa.set_salary_jpa(30000)
print("Salary:", emp_jpa.get_salary_jpa())
