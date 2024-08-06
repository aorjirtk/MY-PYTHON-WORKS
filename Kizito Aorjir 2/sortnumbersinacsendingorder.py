def get_sortedNumbers(num1,num2,num3):
	least_num = num1
	small_num = num2
	large_num = num3
	if num2 < least_num and num2 < num3:
		least_num = num2
	if num3 < least_num and num3 < num2:
		least_num = num3
	if num1 < small_num and num1 > num3:
		small_num = num1
	if num3 < small_num and num3 > num1:
		small_num = num3
	if num2 > large_num and num2 > num1:
		large_num = num2
	if num1 > large_num and num1 > num2:
		large_num = num1
	return least_num,small_num,large_num

print(get_sortedNumbers(9,2,1))