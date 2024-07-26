#collect gratuity rate from user and store
#collect subtotal for user and store
#since gratuity rate is in percentage, divide it by 100 and multiply by subtotal to get the gratuity
#print value as gratuity
#add gratuity to subtotal to get total
#print value as total



gratuity_rate = float(input('Enter gratuity rate: '))
subtotal = float(input('Enter subtotal amount: '))

gratuity = (gratuity_rate/100) * subtotal
total = subtotal + gratuity
print('Your gratuity is: ', gratuity)
print('Your total is: ', total)

