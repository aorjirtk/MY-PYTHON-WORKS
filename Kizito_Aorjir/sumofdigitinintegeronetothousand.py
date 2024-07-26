#Collect the number from the user and store
#to the first digit, modulo the number by 10000 and also use the // operator by 1000 to remove the other 3 digits
#to get the second digit, modulo the number by 1000 to remove the first digit and also use the // operator by 100 to remove the other 3 digits 
#to get the third digit, modulo the number by 10 remove the first 2 digits and also use the // to extract the last digit
#to get the fourth digit, modulo the number by 10, to extract all firt 3 digits and u are left with the fourth digit.
#add the first, second, third amd fourth digits together to get the sum of the digits.
#print




number = int(input('Enter the number from 0-1000: '))

first_digit = (number % 10000) //1000 
second_digit = (number % 1000) // 100
third_digit = (number % 100) //10
fourth_digit = number % 10

total = first_digit + second_digit + third_digit + fourth_digit
print('The sum of digits in integers from 0 - 1000 is: ',total)



