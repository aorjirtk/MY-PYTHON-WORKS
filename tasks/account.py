from random import random


class Account:
    number_of_eyes = 2

    def __init__(self, name,number,phone, pin):
        self.name = name
        self.number = number
        self.balance = 0.00
        self.phone = self.set_phone(phone)
        self.account_number = self.__get_account_number()

    def deposit(self, amount):
        self.balance = self.balance + amount

    def get_balance(self):
        return self.balance



    def generate_account_number(self):
        return "2222" + str(random.randrange(start:10000, stop:99999))


    @property
    def phone(self):
        return self.phone

    @phone.setter
    def phone(self, number):
        if len(number) != 11:
            raise ValueError"phone number is invalid"

    @depossit.setter
    def deposit(self, amount):
        if amount <= 0.00:
             raise ValueError"deposit amount is invalid"



h1 = Account( "Samuel","4344434344", pin="3331")
h2 = Account("Kizito", "4354455454", "4332")
h3 = Account("Mark","322134553454", pin="2122")