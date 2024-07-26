#collect the final account value and store
#collect the monthly interest rate and store
#collect the number of months and store
#divide the final account value by 1 + monthly interest rate  raised by number of months



final_account_value = float(input('Enter the final account value: '))
monthly_interest_rate = float(input('Enter the monthly interest rate: '))
number_of_month = float(input('Enter the number of months: '))
initial_deposit_amount = final_account_value/((1+ (monthly_interest_rate)/100)** number_of_month)
print('You need to deposit',initial_deposit_amount,'amount as initial deposit to get #,5000 in 3years')