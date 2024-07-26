
total_withdrawal=0
total_deposit=0
net_amount=0
counter=0
user_input=0

while user_input != -1:
	user_input = int(input("Enter 1 to deposit or 2 to withdraw "))
	counter+=1
	
	if user_input==1:
		deposit = double(input("Enter the amount you want to deposit "))
		if deposit < 0:
			print("invalid number")
		else:
		net_amount+=deposit

	if user_input==2:
		withdraw = double(input("Enter the amount you want to withdraw "))
		net_amount-=withdraw
		if net_amount-withdraw or withdraw < 0:
			print("invalid amount")
			
if net_amount < withdraw:
	print("invalid amount")
else:
	print("account balance is ",net_amount)
