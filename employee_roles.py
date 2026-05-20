class JPA_Employee:
    def work(self):
        print("Employee performs tasks")


class JPA_Programmer(JPA_Employee):
    def work(self):
        print("Programmer writes code")


class JPA_Designer(JPA_Employee):
    def work(self):
        print("Designer creates UI designs")


JPA_employees = [JPA_Programmer(), JPA_Designer()]

for JPA_emp in JPA_employees:
    JPA_emp.work()

    #JohnPaulArcilla