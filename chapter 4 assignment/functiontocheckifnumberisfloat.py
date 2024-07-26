def function_to_find_float_numbers(number1,number2):
	
	if type(number1) == float and type(number2) == float: 
		result = 2

	if type(number1) == float and type(number2) != float:
		result = 1

	if type(number1) != float and type(number2) == float:
		result = 1

	if type(number1) != float and type(number2) != float:
		result = 0
	return result
	
print(function_to_find_float_numbers(2,1))
print(function_to_find_float_numbers(1.2,1))
print(function_to_find_float_numbers(1.2,2))

	