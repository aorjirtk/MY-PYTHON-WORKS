number = int(input("Enter the five digit number "))


last_digit = int(number % 10)

first_digit = int(number // 10000)

fourth_digit = int((number // 10) % 10)

second_digit = int((number // 1000) % 10)

third_digit = int((number // 100) % 10)

for counter in range(1,2):
	print(first_digit)
	print(second_digit)
	print(third_digit)
	print(fourth_digit)
	print(last_digit)

