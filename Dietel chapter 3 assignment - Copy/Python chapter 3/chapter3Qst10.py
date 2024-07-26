principal = 1000
annual_rate = 7/100
for number_of_years in range(1, 31):

	amount_on_deposit= principal * (1 + annual_rate)**number_of_years

	print('At the end of ',number_of_years, 'years, the amount on deposit is ',amount_on_deposit)
