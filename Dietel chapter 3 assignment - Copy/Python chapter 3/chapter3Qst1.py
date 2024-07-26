
counter=0
user_input=0

while user_input != 1 and user_input != 2:
	user_input = int(input("Enter 1 or 2 to stop "))
	if user_input != 1 and user_input != 2:
		counter+=1
print(counter)