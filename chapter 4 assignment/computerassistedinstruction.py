from random import randint
counter = 0
user_input = 0
number1 = randint(1,10)
number2 = randint(1,10)
access = str(input("Enter 'Yes' to continue or 'No' to stop "))
if access == 'Yes':
	while user_input != 'No':
		counter+=1
		number1 = randint(1,10)
		number2 = randint(1,10)
		result = number1*number2
		print('How much is',number1, '*' ,number2,)
		user_input = int(input("Attempt the above questions or enter 'No' to stop: "))
		if user_input == result:
			print("Very good!, Enter 'Yes' to continue or 'No' to stop ")
			print("you attemoted ",counter, "times")
		if user_input != result:
			print("No. Please try again. ")
				
			
