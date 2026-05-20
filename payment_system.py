class JPA_Payment:
    def pay(self):
        print("Processing payment")


class JPA_CashPayment(JPA_Payment):
    def pay(self):
        print("Payment made using cash")


class JPA_CardPayment(JPA_Payment):
    def pay(self):
        print("Payment made using credit card")


JPA_payments = [JPA_CashPayment(), JPA_CardPayment()]

for JPA_p in JPA_payments:
    JPA_p.pay()

    #JohnPaulArcilla