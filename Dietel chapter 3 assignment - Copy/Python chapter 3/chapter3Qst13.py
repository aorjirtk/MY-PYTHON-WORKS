number = int(input("Enter the number: "))
factors=1
counter = 1

for counter in range(1,(number+1)):
	factors=factors*counter

	print(factors)

