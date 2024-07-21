principal=float(input("Enter the principal amount: "))

annual_interest_rate=float(input("Enter the annual interest rate: "))

duration_of_loan=float(input("Enter the duration of the loan: "))

rate= annual_interest_rate/12

monthly_payment_amount=0

monthly_payment_amount= principal*((annual_interest_rate*(1+annual_interest_rate)**duration_of_loan)/((1+annual_interest_rate)**duration_of_loan)-1)
print(monthly_payment_amount)