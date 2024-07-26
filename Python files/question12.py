principal = 1000
annual_rate = 7/100
for number_of_years in range(1, 30):

	amount_on_deposit= principal * (1 + 	annual_rate)**number_of_years

print(amount_on_deposit)
