even_number = 0
for number in range (1000, 3001):
	if ((number % 10000) //1000) % 2 == 0 and ((number % 1000) // 100) % 2 == 0 and ((number % 100) //10) % 2 == 0 and (number % 10) %2 == 0:
		even_number = number
		print(even_number)