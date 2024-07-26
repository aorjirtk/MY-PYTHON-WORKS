gallons_used=0
miles_per_gallon=0
counter = 0
flag = 0
miles_driven=0
combined_miles_driven_per_gallon = 0

while (flag != -1):

	miles_driven = int(input("Enter the miles driven: "))

	gallons_used = int(input("Enter the amount of gallons used: "))

	miles_per_gallon = miles_driven / gallons_used

	combined_miles_driven_per_gallon = combined_miles_driven_per_gallon + miles_per_gallon

	counter+=1

	flag=int(input("Enter '-1' to stop or '1' to continue: "))

print('miles driven per gallon is ',miles_per_gallon)

print('the combined miles driven per gallon is ',combined_miles_driven_per_gallon)