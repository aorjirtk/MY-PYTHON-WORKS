word = str(input("Enter your word "))

print(len(word))

for count in range(0,len(word)):
	 

	#if len(word) >2:
		#result = word[0] + word[1] + word[-2] + word[-1]
	
	#if len(word) ==2:
		#result = word[0] + word[1] + word[0] + word[1]
	#if len(word) == 1:
		#result = '""'

	if len(word) > 3:
		if word[-1] != 'g' and word[-2] != 'n' and word[-3] != 'i':
			result = word + 'ing'
	
		if word[-1] == 'g' and word[-2] == 'n' and word[-3]=='i':
			result = word + 'ly'
	if len(word) <= 3:
		result = word
print(result)
		

	