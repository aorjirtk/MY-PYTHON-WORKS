def multiplication_function(*numbers):
	total = 1
	for number in numbers:
		total *= number
	return total
print(multiplication_function(1,2,3,4,5))