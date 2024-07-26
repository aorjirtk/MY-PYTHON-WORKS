#collect the number of minutes and store as total minutes
#divide total minutes by number of minutes in a year which is 525600
#print result as number of years
#get the minutes left 
#divide the minutes left by number of minutes in a day which is 1440
#print result as number days left


total_minutes = int(input('Enter the minutes: '))

year = total_minutes//525600
minutes_in_years = year * 525600
minutes_left = total_minutes - minutes_in_years
day = minutes_left//1440
print(year,'years and ', day,'days')
