import unittest
import loan
from loan.loan_contract import LoanContract

class TestLoanContract(unittest.TestCase):
    def setUp(self):
        self.borrower = LoanContract("John Doe", 15, 200000.00, 2)

    def test_that_we_can_get_details_of_borrower_name(self):
        self.assertEqual(self.borrower.get_borrower_name(), "John Doe")

    def test_that_we_can_get_details_of_borrower_loan_amount(self):
        self.assertEqual(self.borrower.get_borrower_loan_amount(), 200000.00)

    def test_that_we_can_calculate_borrower_monthly_pay(self):
        self.assertEqual(self.borrower.get_monthly_pay(), 800)

    def test_that_we_can_calculate_borrower_total_pay(self):
        self.assertEqual(self.borrower.get_total_pay(), 2000)




