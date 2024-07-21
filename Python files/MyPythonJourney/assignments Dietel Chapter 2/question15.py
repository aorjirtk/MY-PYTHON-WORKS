first_number = float(input("Enter first number"))

second_number = float(input("Enter second number"))

third_number = float(input("Enter third number"))

if first_number > second_number and first_number > third_number:
	print(first_number, 'is the highest number') 
elif second_number > first_number and second_number > third_number:
	print(second_number, 'is the highest number') 
elif third_number > first_number and third_number > second_number:
	print(third_number, 'is the highest number')

if first_number > second_number and first_number < third_number:
	print(first_number, 'is the second number') 
elif second_number > first_number and second_number < third_number:
	print(second_number, 'is the second number') 
elif third_number > first_number and third_number < second_number:
	print(third_number, 'is the second number')

if third_number < second_number and third_number < first_number:
	print(third_number, 'is the least number') 
elif second_number < first_number and second_number < third_number:
	print(second_number, 'is the least number') 
elif third_number < first_number and third_number < second_number:
	print(third_number, 'is the least number')