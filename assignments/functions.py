'''def greeting():
    name = input('what is your name  ')
    print ('hello',name)
greeting()'''

'''import random
def random_numbers():
    for i in range(1,6,1):
        numbers = random.randint(1,10)
        print(numbers)
random_numbers()'''

'''def greeting(xname):
    print ('hello',xname)
name = input('what is your name ')
greeting(name)'''

'''def sum(n1,n2):
    print (n1 + n2)
number1 = int(input('pick a number '))
number2 = int(input('pick another number '))
sum(number1,number2)'''


'''def number1(n):
    if n == 0:
        print (n,'is 0')
    elif n > 0:
        print (n,'is a postive number')
    else:
        print (n,'is a negative number')
number = int(input('pick a number  '))
number1(number)'''


'''def palindrome(w):
    reverse = w[::-1]
    if w == reverse:
        print ('the word is a palindrome')
word = input('pick any word ')
palindrome(word)'''

'''import random
def random_numbers(y):
    odd_numbers = []
    even_numbers = []
    for x in y:
        if x % 2 == 0:
            even_numbers.append(x)
        else:
            odd_numbers.append(x)
    print ('these are the odd numbers',odd_numbers)
    print ('these are the even numbers',even_numbers)
numbers = []
for i in range(1,6,1):
    number = random.randint(1,100)
    numbers.append(number)
random_numbers(numbers)'''



'''import random
def x():
    numbers = []
    number = int(input('pick any number  '))
    while len(numbers) < 5:
        for i in range(1,6,1):
            number2 = random.randint(number - 10,number + 10)
            if number2 not in numbers:
                numbers.append(number2)
    print (numbers)
x()'''


'''def x(y):
    value = list(y.keys())
    for i in value:
        if y[i] % 2 != 0:
            del y[i]
    print (y)
sports = {'basketball': 5,'soccer': 9, 'football': 14,'lacrosse': 10,'cricket': 20}
x(sports)'''



'''def school_fee():
    name = input('what is your name?  ')
    grade = int(input('what is your grade?  '))
    if grade >= 6:
        print(name,'has to pay $10,000 for the admission fee')
    else:
        print(name,'has to pay $14,000 for the admission fee')
school_fee()'''


'''def factor(n):
    factors = []
    for i in range(0,n,1):
        if i % n == 0:
            factors.append(i)
    print(factors)
number = int(input('pick a number  '))
factor(number)'''



'''def animals():
    domestic = ('dog','cat','hamster','guinea pig','parrot')
    wild = ('tiger','lion','elephant','monkey','zebra')
    for i in domestic:
        if i in domestic:
            print (domestic[i],'is a domestic animal ')
    for x in wild:
        if x in wild:
            print(wild[x],'is a wild animal')
animals()''' 



'''import random
def f(c):
    numbers = []
    positive = []
    negative = []
    for i in range(1,21,1):
        number = random.randint(-255,255)
        numbers.append(number)
    for x in numbers:
        if c == 'negative':
            if x < 0:
                negative.append(x)
        else:
            if x >= 0:
                positive.append(x)
    if c == 'negative':
        print (negative)
    else:
        print (positive)
choice = input('negative or positive  ')
f(choice)'''


'''word = input('pick any word  ')
def l(w):
    w = list(w)
    w.sort()
    w = ''.join(w)
    print (w)
l(word)'''



'''def quarters(q):
    pennies1 = 25 * q
    return pennies1
quarter = int(input('how many quarters  '))
def dimes(d):
    pennies2 = 10 * d
    return pennies2
dime = int(input('how many dimes  '))
def nickels(n):
    pennies3 = 5 * n
    return pennies3
nickel = int(input('how many nickels  '))
p1 = quarters(quarter)
p2 = dimes(dime)
p3 = nickels(nickel)
total_pennies = p1 + p2 + p3
print ('you have a total of',total_pennies,'pennies')'''


'''strings = int(input('how many strings are you going to input  '))
def palindrome(s):
    for count in range(0,s,1):
        string = input('enter a string  ')
        if string == string[::-1]:
            print ('your string is a palindrome')
        else:
            print ('your string is not a palindrome')
palindrome(strings)'''


'''import random
upper_bound = int(input('pick a number  '))
lower_bound = int(input('pick another number lower than your first number  '))
def number(l,u):
    n = random.randint(u,l)
    print (n,'is between',upper_bound,'and',lower_bound)
number(upper_bound,lower_bound)'''



'''numbers = []
for count in range(1,6,1):
    number = int(input('pick a number  '))
    numbers.append(number)
def average(n):
    sum = 0
    for count in n:
        sum += count
    average1 = sum // len(n)
    print (average1,'is the average of all your numbers')
def total(n):
    sum = 0
    for count in numbers:
        sum += count
    print (sum,'is the sum of all your numbers ')
choice = input('do you want to find the total of all your numbers or the average  ')
if choice == 'average':
    average(numbers)
else:
    total(numbers)'''




'''def vowel():
    vowels = 0
    sentence = input('enter a sentence  ')
    sentence1 = list(sentence)
    for count in sentence1:
        print (count)
        if count == 'a' or count == 'e' or count ==  'i' or count == 'o' or count == 'u':
            vowels += 1
    return vowels
v = vowel()
print ('there are',v,'vowels in your sentence')'''



'''def number(n):
    factors = []
    for i in range(1,n,1):
        if n % i == 0:
            factors.append(i)
    return factors
num = int(input('pick any number  '))
n = number(num)
print (n)'''


'''def square_number(n):
    square = n * n
    return(square)
number = int(input('pick a number  '))
s = square_number(number)
print (s)'''



'''import area_functions
choice = input('what shape do you want to find the area of you can pick a rectangle,square,circle,and triangle  ')
if choice == 'rectangle':
    length = int(input('what is the length of your rectangle  '))
    width = int(input('what is the width of your rectangle  '))
    a = area_functions.area_rectangle(length,width)
    print (a,'is the area of your rectangle')
elif choice == 'square':
    width = int(input('what is the width of your square  '))
    a = area_functions.area_square(width)
    print (a,'is the area of your square ')
elif choice == 'circle':
    radius = int(input('what is the radius of your circle  '))
    a = area_functions.area_circle(radius)
else:
    base = int(input('what is the base of your triangle'))
    height = int(input('what is the height of your triangle'))
    a = area_functions.area_triangle(base,height)'''


'''a = 10
def check(a):
    a += 10
    print(a,'in function')
print(a,'outside function,before function call')
check(a)
print (a,'outside function,after function call')'''


'''a = 10
def check():
    global a
    a += 10
    print(a,'in function')
print(a,'outside function,before function call')
check()
print (a,'outside function,after function call')'''


'''str1 = input('enter a string  ')
str2 = input('enter another string  ')
def x(s1,s2):
    if len(s1) == len(s2):
        print (1)
    else:
        print (0)
x(str1,str2)'''


'''numbers = {}
for i in range(0,100,1):
    numbers[i] = i * i
number = int(input('pick a number between 1 through 100  '))
def x(n):
    numbers2 = {}
    global numbers
    for i in numbers:
        if i % n != 0:
            numbers2[i] = i * i
    print (numbers2)
x(number)'''




'''for count in range(1,3,1):
    print ('*',end = ' ')
print ()
print ()
print ('*')
print ()
for count in range(1,3,1):
    print ('*',end = ' ')'''


'''number = int(input('pick a number  '))
def square_number():
    global number
    number = number * number
    print (number)
def sum_number():
    global number
    number = number + number
    print (number)
print (number)
square_number()
print (number)
sum_number()'''


'''g = 'Welcome to Youngwonks'
print (g[0],g[1],g[2])
print (g[-1])
print (g[0:3])
print (g[4:7])
print (g[:4])
print (g[4:])
print (g[0:15:2])
print (g[::3])
print (g[::-1])'''



'''number = int(input('pick a number  '))
def square_number(n):
    n = n * n
    print (n)
def sum_number(n):
    n = n + n
    print (n)
print (number)
square_number(number)
print (number)
sum_number(number)'''


'''def greet(n = 'stranger'):
    print ('hello',n)
greet('hayden')'''


'''def patterns(n1 = 10,n2 = 10):
    for rows in range(0,n1,1):
        for columns in range(0,n2,1):
            print ('*',end = '')
        print ()
patterns(n2 = 1)'''


'''def x(start = 1,stop = 100,step = 1):
    for count in range(start,stop,step):
        print (count)
x()'''



'''import random
def x(n1 = 1,n2 = 10):
    random_number = random.randint(n1,n2)
    print (random_number)
x(n1 = 1,n2 = 100)'''

