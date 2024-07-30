def reverse(number):
	reversed_num = 0
	while number != 0:
		digit = number % 10
		reversed_num = reversed_num * 10 + digit
		number // = 10
	return reversed_num

print(reverse(123))
		