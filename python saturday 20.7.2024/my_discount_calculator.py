def my_discount_calculator (price,discount):

	discount_amount = (price/100) * discount

	balance_after_discount = price - discount_amount

	return print(balance_after_discount)

my_discount_calculator(150,15)
my_discount_calculator(1050,25)
my_discount_calculator(150,5)




