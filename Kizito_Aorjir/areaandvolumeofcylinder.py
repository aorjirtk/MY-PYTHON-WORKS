#collect the radius of the cylinder and store
#collect the length of the cylinder and store
#get the value of pi which is 3.14159265
#multiply the pi by the value of radius square which gives you the area
#print result as area
#multiply the area by the length which gives you the volume
#print result as volume

radius = float(input('Enter the radius of cylinder: '))
length = float(input('Enter the length of cylinder: '))
PI = 3.14159265
area = PI * (radius**2)
volume = area * length
print('The area of the cylinder is ', area)
print('The volume of the cylinder is ', volume)