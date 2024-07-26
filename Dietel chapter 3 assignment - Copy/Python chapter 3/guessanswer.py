from random import randint


for counter in range(1,11):
	counter+=1
	number=randint(1,5)
	number2 = randint(1,5)
	result = number + number2
	print('solve for ', number, '+', number2)

	attempt = int(input('Enter the correct answer in 10 attempts: '))

	if attempt != result:
		print('Almost there, Try again')

	if attempt == result:
		print('You are Genius, keep up the good work')
		print('You have attempted: ',counter,'times')


		

	
	