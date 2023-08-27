'''for count in range(1,11,1):
    print (count)'''


'''number = 1
while number <= 10:
    print (number)
    number = number + 1'''



'''number = 20
while number <= 50:
    print (number)
    number += 1
number1 = 49
while number1 >= 10:
    print (number1)
    number1 -= 1'''




'''word = input('choose any word you would like ')
for letters in word:
    print (letters)
print (word)'''


'''sentence = input('choose any sentence you would like ')
for letter in sentence:
    if letter != 'a':
        print (letter)'''
    

'''number = 1
while True:
    print (number)
    number += 1'''




'''number = 10
for count in range(1,11,1):
    print (count)
while True:
    print (number)
    number -= 1'''





'''import time
number = 5
while number >= 1:
     print (number)
     number -= 1
     time.sleep(1)
print ('BLAST OFF!!!!')'''




'''while True:
    number = 1
    while number <= 10:
        print (number)
        number += 1

    number2 = 9
    while number2 >= 1:
        print (number2)
        number2 -= 1 '''   




'''while True:
    for number in range(1,11,1):
        print (number)
    for number2 in range(9,1,-1):
        print (number2)'''



'''import time
import random
while True:
    num1 = random.randint(1,100)
    num2 = random.uniform(1,100)
    print (num1)
    print (num2)
    time.sleep(3)'''



'''while True:
    name = input('what is your name? ')
    if name == 'Hayden':
        break'''
'''import time
import random
money = int(input('how much money do you want to deposit into your account? '))
while True:
    roll_dice = input('would you like to roll the dice? ')
    if roll_dice == 'yes':
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print ('waiting for a few seconds ')
        time.sleep(2)
        if dice1 == dice2:
            print ('you won!')
            print (dice1, dice2)           
            money += 5
            print (money)
        else:
            print ('you lost')
            print (dice1, dice2)
            money -= 1
            print (money)
    elif money == 0 or roll_dice == 'no':
        print ('thank you for playing')
        break'''




'''number = 0
while True:
    if number != 16:
        print (number)
        number += 1
    elif number == 16:
        print ('hello')
        break'''


'''total = 0
number = 1        
while number <= 10:
    print (number)
    number += 1
    total = total + number
print (total)'''


'''import random
while True:
    number = random.randint(1,10)
    if number != 7:
        print (number)
    else:
        print (number)
        break
while True:
    number2 = random.randint(1,10)
    if number2 != 5:
        print (number2)
    else:
        print(number2)
        break'''

'''while True:
    word = input('type in a random word ')
    if len(word) <= 7:
        print (word,'does not have enough letters in it')
    else:
        print (word,'has enough letters in it')
        break'''


'''symbol = input('enter a symbol ')
rows = int(input(' how many rows do you want '))
columns = int(input('how mnay columns '))
for row in range(0,rows,1):
    for column in range(0,columns,1):
        print (symbol, end = ' ')
    print ()'''


'''factorial = 1
number = int(input('enter a number'))
for count in range(0,number,1):
    factorial = number * (number - 1)
print (factorial)'''




'''password = 'hayden'
while True:
    enter_password = input('what is the password ')
    if enter_password == 'hayden':
        print ('access granted')
        break
    else:
        print ('Access Denied')'''


'''while True:
    for count in range(100,999,1):
        print (count)       
        if count % 23 == 0:
            break'''


'''number = int(input('pick a number '))             
for count in range(0,number,1):
    number *= number
print (number)'''   





'''jar = 1
number = int(input('pick a random number '))
while number != 1:
    jar *= number
    number -= 1
print (jar,'is the factorial of your number')'''


'''import random
while True:
    number = random.randint(100,999)
    if number % 23 == 0:
        print (number)
        break
    else:
        print (number)'''


'''guesses = 0
import random
number = random.randint(20,30)
while True:
    guess = int(input('guess the random number between 20 and 30  '))
    if guess != number:
        print ('that is not the right number please try again')
    else:
        print ('you guessed the correct number')
        break
    guesses += 1
print (guesses)'''



'''import time
import random
while True:
    number = random.randint(1,100) 
    number2 = random.uniform(1,100)
    print (number)
    print (number2)
    time.sleep(3)'''



'''import time
timer = int(input('how many seconds to blast off   '))
while timer != 0:
    time.sleep(1)
    print (timer)
    timer -= 1
print ('blast off!!!')'''


'''count = 0
while True:
    count += 1
    if count == 15:
        print ('hello')
        break
    else:
        print (count)'''


'''number = 0
while True:
    print (number)
    number += 2
    if number == 34:
        break'''

'''import random
while True:
    number = random.randint(1,200)
    print (number)
    if number % 11 == 0:
        break'''



