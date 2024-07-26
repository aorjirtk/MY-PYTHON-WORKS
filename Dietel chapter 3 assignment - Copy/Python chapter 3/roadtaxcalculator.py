tax = 0 

cost_of_car = int(input("Enter the cost of car: "))

if cost_of_car < 1000000:

	tax = (cost_of_car * 10) / 100

elif cost_of_car > 1000000 and cost_of_car < 3000000:

	tax = (cost_of_car * 15) / 100
	
elif cost_of_car > 3000000 and cost_of_car < 5000000:

	tax = (cost_of_car * 20) / 100

else:
	tax = (cost_of_car * 25) / 100
	
	

print('Your tax is ', tax)