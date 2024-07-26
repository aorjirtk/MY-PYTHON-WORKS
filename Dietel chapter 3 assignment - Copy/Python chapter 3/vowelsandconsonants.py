vowels = 0
consonants = 0

word= str(input("Enter the word: "))

for count in word:
	#if (count == 'a') or (count == 'i') or (count == 'e') or (count == 'o') or (count == 'u'):
		vowels+=1

	if (count == 'a') and (count == 'a') or (count == 'i') and (count == 'i') or (count == 'u') and (count == 'u')or 		(count == 'e') and (count == 'e') or (count == 'o') and (count == 'o'):
		vowels+=1
	else:
	    	consonants+=1
print('The number of vowels in ',word, 'are: ',vowels)
print('The number of consonants in ',word, 'are: ',consonants)


