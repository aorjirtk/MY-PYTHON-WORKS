number = int(input("Enter the five digit number ")) 


if (number % 10) == (number // 10000) and ((number // 1000) % 10) == ((number // 10) % 10):
	print( number, " is a palindrome")
else:
	print(number, " is Not a palindrom")
