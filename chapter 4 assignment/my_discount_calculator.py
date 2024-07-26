def my_discount_calculator (price,discount):

	discount_amount = (price/100) * discount

	balance_after_discount = price - discount_amount

	return balance_after_discount

print(my_discount_calculator(150,15))
print(my_discount_calculator(1050,25))
print(my_discount_calculator(150,5))




