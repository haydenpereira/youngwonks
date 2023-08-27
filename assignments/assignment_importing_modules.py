'''import time
time.sleep(5)
refresh = input('do you want to refresh your page ')
if refresh == 'yes':
    print (' Please wait your page is loading')
    time.sleep(2)
    print ('there is high traffic try again later')
else:
    print ('thank you for visting our website ')'''


'''import random
rand = random.randint(1,30)
if rand % 2 == 0 and rand % 3 == 0:
    print (rand)
else:
    print (' the number is not divisible by 2 and 3')'''


'''import random
num1 = int(input('enter a number of digits from 1 to 6'))
if num1 == 1:'''


'''import random
rand1 = random.randint(1,50)
rand2 = random.randint(1,50)
rand3 = random.randint(1,50)
if rand1 + rand2 + rand3 > 60:
    print ('AAABBB')
elif rand1 + rand2 + rand3 > 50:
    print ('ABBBB')
elif rand1 + rand2 + rand3 > 35:
    print ('BBBBA')
else:
    print ('CCCCC')'''


import random 
rand = random.randint(1,200)
print (rand)
if rand % 2 == 0:
    print (rand,'is even')
else:
    print (rand,'is odd')

