passed_score = 0
counter = 0
counter2 = 0
failed_score = 0

for score in range(15):
	score = int(input("Enter score of 15 students "))

	if score >= 45:
		counter+=1

	if score <= 44:
		counter2 += 1
		
print('Number of students that failed are ',counter2)
print('Number of students that passed are ',counter)

	