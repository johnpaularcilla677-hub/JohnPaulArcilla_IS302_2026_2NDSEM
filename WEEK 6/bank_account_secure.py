class BankAccount_jpa:
    def __init__(self_jpa, balance_jpa):
        self_jpa.__balance = balance_jpa

    def deposit_jpa(self_jpa, amount_jpa):
        self_jpa.__balance += amount_jpa

    def withdraw_jpa(self_jpa, amount_jpa):
        if amount_jpa <= self_jpa.__balance:
            self_jpa.__balance -= amount_jpa
        else:
            print("Insufficient funds")

    def get_balance_jpa(self_jpa):
        return self_jpa.__balance

account_jpa = BankAccount_jpa(5000)
account_jpa.deposit_jpa(1000)
account_nbs.withdraw_nbs(2000)
print("Balance_jpa:", account_jpa.get_balance_jpa())
