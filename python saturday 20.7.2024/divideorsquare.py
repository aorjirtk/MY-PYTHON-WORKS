def divide_or_square(number):
	if number % 5 == 0:
		result = (number)**(1/2)
	else:
		result = number % 5
	return print(result)

divide_or_square(125)
divide_or_square(21)
divide_or_square(0)


		
		