from decimal import Decimal
class Akant:
    def __init__(self, name: str, pin: str , balance: Decimal = 0.00):
        self.name = name.upper()
        self.pin = pin
        self.balance = balance

        def deposit(self, amount):
            self.balance += amount


account1 = Akant("Chi", "1111")
account2 = Akant("Kizito", "2222")
print(account1.name)
