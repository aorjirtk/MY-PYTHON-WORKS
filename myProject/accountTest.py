
import unittest

from account import Account


class TestAccount(unittest.TestCase):
    def test_that_account_exists(self):
        self.account = Account("John", "Smith", pin="1111")

    def test_that_account_can_be_created(self):
        self.account = Account(first_name='John', last_name='Smith',pin= "1111")
        self.assertEqual(self.account.first_name,"John",)
        self.assertEqual(self.account.last_name,"Smith")

    def test_that_account1_deposit_1k_balance_is_1k(self, amount):
        self.account = Account(first_name='John', last_name='Smith', pin="1111")
        self.account.deposit(1000)
        self.assertEqual(self.account.balance,1000)

    def test_that_when_deposit_5k_and_negative_1k_balance_is_5k(self):
        self.account = Account(first_name='John', last_name='Smith', pin="1111")
        self.account.deposit(5000)
        self.account.deposit(-1000)
        self.assertEqual(self.account.balance,5000)


if __name__ == '__main__':
     unittest.main()





