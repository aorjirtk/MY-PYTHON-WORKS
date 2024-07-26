def get_average_function (*numbers):
	total = 0
	average = 0
	for number in numbers:
		total+=number
		average = total/len(numbers)
	return average
print(get_average_function(1,2,3,4,5,6,7,8))