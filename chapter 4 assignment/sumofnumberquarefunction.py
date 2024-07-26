def sum_of_number_square_function(*numbers):
	total = 0
	for value in numbers:
		total+=value**2
	return (total)
print(sum_of_number_square_function(1,2,3,4,5))