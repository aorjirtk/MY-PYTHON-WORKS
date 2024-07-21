smallest_number =0
largest_number =0
average =0
total =0
counter =0
product = 0
number1 = 0
number2 = 0
number3 = 0
number4 = 0

for counter in range(0,4):
	counter+=1
	user_input = int(input("Enter the 4 integers: "))
	if counter == 1:number1 =user_input
	if counter == 2:number2 =user_input
	if counter == 3:number3 =user_input
	if counter == 4:number4 =user_input


	
if number1 > number2 and number1 > number3 and number1 > number4:
	print(number1,' is the largest_number')

elif number2 > number1 and number2 > number3 and number2 > number4:
	print(number2,' is the largest_number')

elif number3 > number2 and number3 > number1 and number3 > number4:
	print(number3,' is the largest_number')

elif number4 > number2 and number4 > number3 and number4 > number1:
	print(number4,' is the largest_number')
if number1 < number2 and number1 < number3 and number1 < number4:
	print(number1,' is the smallest_number')

elif number2 < number1 and number2 < number3 and number2 < number4:
	print(number2,' is the smallest_number')

elif number3 < number2 and number3 < number1 and number3 < number4:
	print(number3,' is the smallest_number')

elif number4 < number2 and number4 < number3 and number4 < number1:
	print(number4,' is the smallest_number')



product= number1*number2*number3*number4
total= number1+number2+number3+number4
average=total/counter
print(product," is the product")
print(total," is the sum")
print('The average is ',average)