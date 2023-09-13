'''def Tshirt(price):
    tax = price * 0.10
    price += tax
    print ('the cost of your T shirt is',int(price),'dollars')
def discount(price):
    discount_percentage = price * 0.5
    price -= discount_percentage
    print('the cost of your item with a 50 percent discount is',int(price),'dollars')
Tshirt(int(input('what is the price of your item? ')))
discount(int(input('what is the price of your item? ')))'''

'''def x(word):
    word = word[::-1]
    print (word)
    print ('the length of your word is',len(word))
    length = 0
    for x in word:
        x = ord(x)
        if x in range(65,91):
            length += 1
    print ('there are',length,'capital letter(s) in your word')
x(input('enter a word '))'''

'''import random
def random_num(n,start,end):
    if start == '':
        start = 1
    if end == '':
        end = 100
    start = int(start)
    end = int(end)
    for i in range(0,n,1):
        print (random.randint(start,end))
random_num(int(input('enter the number of random numbers you want ')),input('enter a starting number '),input('now enter a ending number '))'''

'''def x(hours,kilometers):
    seconds = (hours * 60) * 60
    miles = kilometers / 1.609
    m_per_sec = miles/seconds
    print(m_per_sec,' miles per second')
x(int(input('how many hours ')),int(input('how many kilometers ')))'''

'''calendar = []
weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday']
for i in weekdays:
    calendar.append(i)
    for x in range(1,6,1):
        activity = input('what activity do you do on ' + i + ' ')
        calendar.append(activity)
print (calendar)'''

'''count = 0
numbers = [(5,6),(1,4),(7,2),(8,3),(5,9)]
for i in numbers:
    x = (i[1],i[0])
    numbers[count] = 
print(numbers)'''

'''def x(word):
    word = word[::-1]
    print (word)
    print ('the length of your word is',len(word))
    length = 0
    for x in word:
        x = ord(x)
        if x in range(65,91):
            length += 1
    print ('there are',length,'capital letter(s) in your word')
x(input('enter a word '))'''

'''import random
def random_num(n,start = 1,end = 100):
    for i in range(0,n,1):
        print (random.randint(start,end))
#random_num(int(input('enter the number of random numbers you want ')),input('enter a starting number '),input('now enter a ending number '))
random_num(5,end = 200)'''

'''calendar = []
weekdays = ['Monday','Tuesday','Wednesday']
for i in weekdays:
    day = [i]
    for x in range(1,3,1):
        activity = input('what activity do you do on ' + i + ' ')
        day.append(activity)
    calendar.append(day)
print (calendar)'''

'''count = 0
numbers = [(2,1),(4,3),(6,5),(8,7),(10,9)]
for i in numbers:
    numbers.remove(i)
    numbers.insert(count,(i[1],i[0]))
    count += 1
print (numbers)'''

'''names = ['Hayden','Chelsea','Leon','Grinal','Meera','Alex']
names2 = []
for i in names:
    name = [i,i[::-1]]
    names2.append(name)
print(names2)'''

'''import random
numbers = []
numbers_list = []
for x in range(0,10,1):
    numbers = []
    for i in range(0,10,1):
        num = random.randint(0,100)
        numbers.append(num)
    numbers_list.append(numbers)
print (numbers_list)'''

# '''import random
# factorial = 1
# for i in range(0,10,1):
#     number = random.randint(1,20)
#     for x in range(1,number + 1,1):
#         factorial *= x 
#     print ('the factorial of {} is {}'.format(number,factorial))
#     factorial = 1'''

'''letters_word = {}
word = input('enter a string ')
for letter in word:
    if letter not in letters_word:
        letters_word[letter] = 1
    elif letter in letters_word:
        letters_word[letter] += 1
print (letters_word)'''

'''columns = int(input('how many columns '))
rows = int(input('how many rows '))
listvar = []
temp_list = []
for i in range(0,rows,1):
    temp_list.append(0)
for x in range(0,columns,1):
    listvar.append(temp_list)
for i in listvar:
    print(i)'''

'''temperatures = [[23, 29, 26], [32, 37, 34.5], [33, 37, 35], [30, 39, 34.5], [28, 37, 32.5]]
max_temp = []
min_temp = []
average_temp = []
num = 0
average = None
for i in temperatures:
    max_temp.append(i[0])
    min_temp.append(i[1])
    average_temp.append(i[2])
for i in max_temp:
    num += i
average = num / 5
print(average)
num = 0
average = 0
for i in min_temp:
    num += i
average = num / 5
print(average)
average = num = 0
for i in average_temp:
    num += i
average = num / 5
print(average)'''

'''import random
listvar = [['Avengers', 'Harry Potter', 'Lord of the Rings', 'Star Wars'], ['Game of Thrones', 'The Simpsons', 'Friends', 'The Office', 'The Family Guy'], ['The Da Vinci Code', 'The Little Prince', 'Harry Potter', 'To Kill a Mockingbird']]
category = input('pick any category, Movies, TV shows, or Novels ')
if category == 'Movies':
    word = random.choice(listvar[0])
elif category == 'TV shows':
    word = random.choice(listvar[1])
elif category == 'Novels':
    word = random.choice(listvar[2])
underscore_word = []
for i in word:
    if i == ' ':
        underscore_word.append(' ')
    else:
        underscore_word.append('_')
while True:
    print(list(word))
    letter = input('guess a letter from the word ')
    if letter not in word:
        print('the letter you guessed is not in the word')
    elif letter in word:'''
        
'''import random
numbers = []
for i in range(1,51,1):
    num = random.randint(1,150)
    numbers.append(num)
for i in numbers:
    if i % 2 != 0:
        print(i)'''

'''value = 1
rows = 5
columns = 1
for i in range(0,rows,1):
    for x in range(0,columns,1):
        print(value,end = ' ')
        value += 2
    print()
    columns += 1
    value = 1'''

'''for hr in range(0,24,1):
    for min in range(0,60,1):
        print(hr,':',min) '''

'''import modules
choice = input('do you want area or circumference ')
rad = int(input('what is the radius '))
if choice == 'area':
    a = modules.area(rad)
    print(a)
elif choice == 'circumference':
    c = modules.circumference(rad)
    print (c)'''

'''numbers = [[13,15,17,19],[21,16,23],[73,79,51,35]]
print (numbers)
for i in numbers:
    for x in range(0,len(i),1):
        if x % 2 == 0:
            i[x] = i[x] ** 3
        else:
            i[x] = i[x] ** 2
print (numbers)'''

'''numbers = [56,4,23,78,5]
for i in range(0,5,1):
    numbers[i] += 100
print (numbers)'''

'''names = ['Hayden','Bob','Chelsea','Ashley','Anthony']
for i in range(0,5,1):
    names[i] = list(names[i])
    names[i].reverse()
    names[i] = ''.join(names[i])
print (names)'''

'''total_amount = 0
banana_price = 0
pear_price = 0
fruits = ['apple','banana','mango','orange','pear']
price = [3,5,1,2,3]
quantity = [2,3,7,8,10]
basket = [price,quantity]
print (basket[0][3],'dollars')
print (basket[1][2],'mangoes')
print (basket[0][0] * basket[1][0],'dollars')
for i in basket[1]:
    total_amount += i
print ('there are',total_amount,'fruits in your basket')
banana_price = basket[0][1] * basket[1][1]
pear_price = basket[0][-1] * basket[1][-1]
print (banana_price + pear_price,'dollars')'''

'''words = []
for i in range(0,5,1):
    word = input('enter a word ')
    words.append([word,word[::-1]])
print (words)'''

'''names = ['Aiden','Hayden','Chelsea','Anthony','Bob']
for i in range(0,5,1):
    names[i] = names[i][0] + names[i][-1]
print (names)'''

'''number = 0
last_num = 1
add = 1
for i in range(1,12,1):
    print(number)
    number += last_num
    last_num = number'''

'''increase = -1
column = 5
for rows in range(0,9,1):
    for columns in range(0,column,1):
        print ('*',end = '')
    print ()
    if column == 1:
        increase = -increase
    column += increase
'''

'''names_ages = {}
names = ['Arun','John','Varun','Mike','Tony']
ages = [15,9,12,10,14] 
print(names)
print(ages)
for i in range(0,5,1):
    names_ages[names[i]] = ages[i]
print(names_ages)'''

'''days = {'Monday' : 6, 'Tuesday' : 7, 'Wednesday' : 9, 'Thursday' : 8, 'Friday' : 6, 'Saturday' : 8, 'Sunday' : 6}
print('There are',len(days),'days in a week')
letters = []
for i in days:
    letters.append(days[i])'''

'''amount = 0
special_names = {}
name = input('enter your name ')
for i in name:
    if i == 'a' or i == 'e' or i == 'o':
        amount += 1
special_names[name] = amount
print(special_names)'''

'''import random
vote_bank = {'Lisa': 25, 'Ammy': 36, 'Joe': 34, 'Brooke': 51, 'Melanie':24}
print(max(vote_bank))
print(min(vote_bank))
name = random.choice(vote_bank.keys())
vote_bank[name] += 1
print(vote_bank)'''

'''numbers = {}
for i in range(1,101,1):
    numbers[i] = i * i
num = int(input('pick a number from 1 to 100 '))
for i in numbers:
    if i % num == 0 or numbers[i] % num == 0:
        del(numbers[i])'''

'''days = {'Monday' : 6, 'Tuesday' : 7, 'Wednesday' : 9, 'Thursday' : 8, 'Friday' : 6, 'Saturday' : 8, 'Sunday' : 6}
print('There are',len(days),'days in a week')
letters = []
for i in days:
    letters.append(i)
letters.sort(reverse = 1)
print(letters)
for i in letters:
    print(i,'has',days[i],'letters')'''

'''amount = 0
special_names = {}
for i in range(0,5,1):
    name = input('what is your name ')
    for i in name:
        if i == 'a' or i == 'e' or i == 'o':
            amount += 1
    special_names[name] = amount
    amount = 0
print(special_names)'''

'''import random
vote_bank = {'Lisa': 25, 'Ammy': 36, 'Joe': 34, 'Brooke': 51, 'Melanie': 24}
print(max(vote_bank.values()))
print(min(vote_bank.values()))
names = []
for i in vote_bank:
    names.append(i)
name = random.choice(names)
vote_bank[name] += 1
print(vote_bank)'''

'''numbers = {}
for i in range(1,101,1):
    numbers[i] = i * i
num = int(input('enter a number from 1 to 100 '))
for i in numbers:
    if i % num != 0 or numbers[i] % num != 0:
        del(numbers[i])
print(numbers)'''


'''numbers = {}
for i in range(1,101,1):
    numbers[i] = i * i
num = int(input('enter a number from 1 to 100 '))
for i in list(numbers.keys()):
    if i % num == 0:
        del(numbers[i])
print(numbers)'''

'''d = {'Arun':80, 'John':59, 'Mike':70, 'Jack':92, 'Tom': 85}
for i in d:
    print(i,':',d[i])
    choice = input('is this the right score? ')
    if choice == 'yes':
        print('Thank you for confirming')
    else:
        score = input('what is the right score ')
        d[i] = score
print(d)'''

'''sum = 0
d = {'Arun':9252777474, 'John':1527483848, 'Mike':1039402394, 'Jack':9278928349, 'Tom': 8524567890}
print(d)
for i in d:
    for x in str(d[i]):
        sum += int(x)
    d[i] = sum
    sum = 0
print(d)'''

'''age = []
name = []
new_info = {}
info = {'Arun':15, 'John':9, 'Varun':12, 'Mike':10, 'Tony':14}
for i in info:
    age.append(info[i])
    name.append(i)
for i in range(0,len(name),1):
    new_info[name[i]] = age[i]
print(new_info)'''

'''count = 0
name = input('what is your name? ')
friend_name = input('what is your friends name? ')
while count != len(name):
    if name[count] in friend_name:
        print(name[count])
    count += 1'''

'''import random   
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
colors = [red,white,blue,green,black]
background = black
rectangle = white
while True:
    screen.fill(background)
    pygame.draw.rect(screen,rectangle,(225,300,150,50))
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.pos[0] in range(225,375) and event.pos[1] in range(300,350):
                rectangle = random.choice(colors)
            else:
                background = random.choice(colors)
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()'''

'''number = 1
rows = 0 
columns = 6
num = 0
while rows < 5:
    while columns > 1:
        print(number, end = ' ')
        number += 1
        columns -= 1
    print()
    rows += 1
    columns -= 1'''

'''import random
numbers = []
while True:
    num = random.randint(10,20)
    if num in numbers:
        pass
    else:
        numbers.append(num)
    if len(numbers) == 10:
        break
print(numbers)'''

numbers = [[13, 15, 17, 19],
           [21, 16, 23],
           [73, 79, 51, 35]]
for i in numbers:
    for x in i:
        if x % 2 != 0:
            numbers[numbers.index(i)][i.index(x)] = x * x
print(numbers)


























    







































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































