'''print ('hayden')
print ('hayden')
print ('hayden')'''


'''for count in range(1,6,1):
    print (count,'hayden')'''


'''for count in range(21,51,2):
    print (count)'''



'''for count in range(20,51,1):
    if count % 2 == 0:
        print (count)'''


'''for count in range(80,9,-1):
    if count % 2 == 0:
        print (count,'E')
    else:
        print (count,'O')'''
    

'''import time
seconds = int(input('how many seconds do you want till blast off? '))
for sec in range(seconds,0,-1):
    print (sec)
    time.sleep(1)
print ('blast off')'''




'''import random
for count in range(1,26,1):
    numbers = random.randint(50,150)
    if numbers % 2 and numbers % 3 == 0:
        print (numbers,'is divisible by 6')
    else:
        print (numbers,'is not divisible by 6')'''




'''for count in range(1,100,1):
    if count % 3 != 0:
        print (count)


for count in range(1,301,1):
    if count % 6 == 0:
        print (count)'''


'''hobby1 = input('pick any hobby')
hobby2 = input('pick any hobby')
hobby3 = input('pick any hobby')
hobby4 = input('pick any hobby')
hobby5 = input('pick any hobby')
for count in range(1,6,1):'''



'''import random
for count in range(1,26,1):
    numbers = random.randint(50,150)
    if numbers % 2 == 0 and numbers % 3 == 0:
        print (numbers,'is divisible by 6')
    else:
        print (numbers,'is not divisible by 6')'''



'''for count in range(1,6,1):
    hobby = input('what is your hobby ')
    print ('entered hobby is', hobby)'''


'''for count in range(1,101,1):
    print (count,'hayden')'''



'''multiple = int(input('what multiplication table do you want to see '))
number = 0  
number2 = (multiple * 10) + 1 
for count in range(0,number2,multiple):
    print ( multiple,'*',number,'=',count)
    number = number + 1'''



'''print ('hello',end =' ')
print ('hayden')'''


'''for number in range(1,6,1):
    for count in range(1,6,1):
        print ('*',end = ' ')
    print ()'''



'''for rows in range(1,7,1):
    for columns in range(1,4,1):
        print ('*',end = ' ' )
    print ()'''



'''for rows in range(1,4,1):
    for columns in range(2,9,2):
        print (columns, end = ' ' )
    print ()'''




'''row = int(input('how many rows '))
column = int(input('how many columns '))
for rows in range(0,row,1):
    for columns in range(0,column,1):
        print ('*', end = ' ' )
    print ()'''


'''for rows in range(1,6,1):
    for columns in range(3,13,3):
        print (columns, end = ' ')
    print ()'''



'''for rows in range(1,5,1):
    for columns in range(8,1,-2):
        print (columns, end = ' ')
    print ()'''




'''for rows in range(9,-1,-3):
    for columns in range(1,6,1):
        print (rows, end = ' ')
    print ()'''


'''count = 4
for rows in range(1,5,1):
    for columns in range(0,count,1):
        print ('*', end = ' ' )
    print ()
    count = count - 1'''



count = 1
for rows in range(1,5,1):
    for columns in range(0,count,1):
        print ('*', end = ' ')
    print ()
    count = count + 1



'''count = 4
for rows in range(1,5,1):
    for columns in range(0,count,1):
        print (rows, end = ' ')
    print ()
    count = count - 1'''




'''value = 8
count = 1
for rows in range(1,5,1):
    for columns in range(0,count,1):
        print (value, end = ' ')
        value = value - 2
    print ()
    value  = 8
    count = count + 1'''





    
'''value = 3
count = 1
for rows in range(1,5,1):
    for columns in range(0,count,1):
        print (value, end = ' ')
        value = value + 3
    value = 3
    count = count + 1
    print ()'''



'''value = 2
count = 4
for rows in range(1,5,1):
    for columns in range(0,count,1):
        print (value, end = ' ')
        value = value + 2
    print ()
    value = 2
    count = count - 1'''




'''value = 25
count = 5
for rows in range(1,6,1):
    for columns in range(0,count,1):
        print (value , end = ' ')
        value = value - 5
    print ()
    value = 25
    count = count - 1'''



'''for count in range(1,4,1):
    for rows in range(1,4,1):
        for columns in range(0,7,1):
            print ('*', end = ' ')
        print()
    print ()'''




'''total = 0
total2 = 0
count1 = 0
import random
for count in range(1,21,1):
    number = random.randint(-20,20)
    if number >= 0:
        total = number + total
    elif number <= 0:
        count1 = count1 + 1
        total2 = (number + total2) 
print (total) 
count2 = 20 - count1
average2 = total/ count2
print ('average of positive numbers',average2)
print (total2)
print (count1) 
average = total2 / count1
print ('average of negative numbers',average) '''
    
    
    

'''for count in range(1,201,1):
    if count % 3 == 0 and count % 2 != 0:
        print (count)''' 
    
'''total = 0
number1 = input('enter a postive number ')
number2 = input('enter another postive number ')
for count in range(number1,number2,1):
    print (count)'''




'''total = 0
total2 = 0
number = int(input('pick a number between 100 and 200 '))
for count in range(100,201,1):
    if count % 2 == 0:
        print (count)
        total = total + count 
    else:
        print (count)
        total2 = (total2 + count) / (total2 + 1)
if number % 2 == 0:
    print (total)
else:
    print (total2)'''






'''product = 0
num1 = int(input('pick a postive number '))
num2 = int(input('pick another postive number '))
num2 = num2 + 1
for count in range(num1,num2,1):
    print (count)
    product = product + count
print ( 'the sum of all these numbers are',product)'''






'''name =  input('what is your name ')
number = int(input('pick any number '))
for names in range(1,number,1):
    print (name)'''



'''sum = 0
n = int(input('pick a number'))
for count in range(1,n,1):
    if count % 2 != 0:
      sum = sum + count
      print (count)
      print (sum,'is the sum of all the odd numbers') ''' 


'''total = 0
for count in range(1,101,1):
    if count % 2 == 0:
        square = count * count
        total = square + total 
print (total)'''





'''product = 1
num1 = int(input('pick a postive number '))
num2 = int(input('pick another postive number '))
num2 = num2 + 1
for count in range(num1,num2,1):
    print (count)
    product = product * count
print ( 'the sum of all these numbers are',product)'''







'''sum1 = 1
n = int(input('pick a number'))
for count in range(1,n,1):
    if count % 2 != 0:
      sum1 = sum1 * count
      print (count)
      print (sum1,'is the sum of all the odd numbers')'''




'''for count in range(1,11,1):
    print ('hayden')'''




'''word = input('what is your name? ')
for letters in range(0,len(word),1):
    print (word[letters],letters)

for letters in word:
    print (letters)'''

