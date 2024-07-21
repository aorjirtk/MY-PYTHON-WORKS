from random import randint

counter = 0
guess_number = randint(1,1000)

userInput = 0
access = str(input("Enter 'Yes' to play or 'No' to stop: "))
if access == 'Yes':
	while userInput != 'No':
		counter+=1
		userInput=int(input("Guess my number between 1 and 1000 with the fewest guesses: "))

		if userInput < guess_number:
			print("Too low, Try again")

		if userInput > guess_number:
			print("Too high, try again")

		if userInput == guess_number:
			print("Congratulations. You guessed the number")
			print('Thank you for your time')
			print("The number of attempts is ",counter)
			access = str(input("Enter 'Yes' to play or 'No' to stop: "))
			if userInput == 'Yes':
				userInput=int(input("Guess my number between 1 and 1000 with the fewest guesses: "))
				guess_number = randint(1,10)
			else:
				break

	

