from main import Akant
from decimal import Decimal

class TestAkant(TestCase):

    def test_that_account_can_deposit(self):
        a1 = Akant(name:"John",pin:"0000")
        a1.deposit(10000)
        a1.deposit(5000)
        self.assertEqual(a1.balance, second: 15000)
