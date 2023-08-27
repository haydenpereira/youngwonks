
days = {'Monday' : 6, 'Tuesday' : 7, 'Wednesday' : 9, 'Thursday' : 8, 'Friday' : 6, 'Saturday' : 8, 'Sunday' : 6}
print('There are',len(days),'days in a week')
letters = []
for i in days:
    letters.append(days[i])
letters = letters.sort()
print(letters)