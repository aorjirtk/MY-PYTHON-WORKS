class LoanContract:


    def __init__(self,borrower_name: str, interest_rate: float,loan_amount: float,loan_period: int):
        self.duration_in_months = None
        self.monthly_interest_rate = None
        self.total_payment = None
        self.monthly_payment = None
        self.borrower_name = borrower_name
        self.interest_rate = interest_rate
        self.loan_amount = loan_amount
        self.loan_period = loan_period

    def get_borrower_name(self):
        return self.borrower_name

    def get_borrower_loan_amount(self):
        return self.loan_amount

    def get_monthly_interest_rate(self):
        self.monthly_interest_rate = (self.interest_rate * 100)/ 12
        return self.monthly_interest_rate

    def get_duration_in_months(self):
        self.duration_in_months = self.loan_period * 12 * 100
        return self.duration_in_months

    def get_monthly_pay(self):
        self.monthly_payment = (self.loan_amount * (self.monthly_interest_rate)) / (1 - (1 - (1 + self.monthly_interest_rate)** self.duration_in_months))
        return self.monthly_payment

    def get_total_pay(self):
        self.total_payment = ((self.loan_amount * (self.interest_rate / 12)) / (1 - (1 - (1 + (self.interest_rate/12))**(self.loan_period * 12))))* (self.loan_period * 12)
        return self.total_payment
        




