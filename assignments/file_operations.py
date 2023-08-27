'''import time
x = open("myself.txt",'r')
data = x.read()
print (data)
for i in data:
    time.sleep(1)
    print (i)'''

'''x = open('colors.txt','w')
x.write('black')
x.close()'''

'''x = open('myself.txt','r')
data = x.readlines()
print (data)
for i in range(0,len(data),1):
    data[i] = data[i].strip()
    print (data[i])
print (len(data))'''

'''vowels = 0
x = open('myself.txt','r')
data = x.read()
for i in data:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vowels += 1
print (vowels)'''

'''x = open('myself.txt','r')
data = x.readline()
data = data.strip()
print (data)'''

'''total = 0
x = open('colors.txt','r')
data = x.readlines()
for i in data:
    i = i.split(' ')
    print (i)
    total += len(i)
#data = data.strip()
#data = data.split(' ')
print (total)'''


'''capital_letters = 0
x = open('colors.txt','r')
data = x.read()
for i in data:
    if i.isupper():
        capital_letters += 1
print(capital_letters)'''

'''for i in data:
    if ord(i) >= 65 and ord(i) <= 90:
        capital_letters += 1
print ('there are {0} capital letters in the file'.format(capital_letters))'''

'''words = 0
x = open('colors.txt','r')
data = x.readlines()
print (data)
for i in data:
    i = i.strip()
    i = i.split(' ')
    for x in i:
        if len(x) > 5:
            words += 1
print (words,'is the number of words in the sentences that have 5 words or more')'''


'''x = open('colors.txt','r')
data = x.readlines()
print (data)
for i in data:
    i = i.strip()
    i = i.split(' ')
    for x in i:
        if x.endswith('s'):
            print (x)'''

'''data = data.split(' ')
print (data)
for i in data:
    if i[-1] == 's':
        print (i)'''

'''x = open('animals.txt','r')
data = x.readlines()
print (data)
for i in data:
    i = i.strip()
    if i[-1] == 'r':
        print (i)'''

'''import time
line_number = 0
x = open('test_file.txt','r')
data = x.readlines()
for i in data:
    line_number += 1
    print (line_number)
    i = i.strip()
    print (i)
    time.sleep(1)'''

'''import random
total = 0
x = open('1000 numbers.txt','w')
for i in range(1,1001,1):
    number = random.randint(1,2000)
    x.write(str(number) + '\n')
x.close()
x = open('1000 numbers.txt','r')
data = x.readlines()
print (data)
for i in data:
    i = i.strip()
    i = int(i)
    total += i
print (total)'''

'''names = []
x = open('names.txt','r')
data = x.read()'''

'''x = open('integers.txt','r')
data = x.read()
data = data.split(' ')

print (data)'''

'''import random
total = 0
x = open('numbers.txt','w')
for i in range(1,21,1):
    number = random.randint(1,100)
    number = str(number)
    x.write(number + '\n')
x.close()
x = open('numbers.txt','r')
data = x.readlines()
print (data)
for i in data:
    i = i.strip()
    i = int(i)
    total += i
print (total)'''

'''y = open('names3.txt','w')
x = open('names2.txt','r')
data = x.readlines()
for i in data:
    i = i.strip()
    i = list(i)
    i.reverse()
    i = ''.join(i)
    y.write(i + '\n')
y.close()
x.close()'''
    

'''import time
line_number = 0
x = open('places.txt','r')
data = x.readlines()
for i in data:
    line_number += 1
    i = i.strip()
    count = 0
    for x in i:
        count += 1
    print (line_number,i,count)'''

    


'''import random
x = open('Dialogue.txt','r')
data = x.readlines()
print (data)
choice = random.choice(data)
print (choice)'''

'''x = open('names1.txt','r')
data = x.readlines()
data.sort()
for i in range(0,len(data),1):
    data[i] = data[i].strip()
print (data)'''

'''total = 0
x = open('integers.txt','r')
data = x.readlines()
for i in data:
    i = i.split(' ')
    for x in i:
        x = x.strip()
        x = int(x)
        total += x
average = total // 6
print (average)'''

'''source_file = input('enter the source file name  ')
x = open(source_file,'r')
data = x.readlines()

username = data[1]'''

'''friends_contact = {}
for i in range(1,4,1):
    friends_name = input('what is one of your friends names  ')
    contact_number = input('what is your friends contact number  ')
    friends_contact[friends_name] = contact_number
for i in friends_contact:
    x = open(i,'w')
    x.write(friends_contact[i])
x.close()'''

'''y = 0
import random
x = open('numbers','w')
while True:
    number = random.randint(1,100)
    if number % 3 == 0:
        number = str(number)
        x.write(number + '\n')
        y += 1
        if y == 10:
            break
x.close() '''

'''x = open('words.txt','r')
data = x.readlines()
print (data)
for word in data:
    word = word.strip()
    reversed = word[::-1]
    if word == reversed:
        print (reversed)'''

'''word = input('pick a word  ')
word2 = input('pick another word  ')
x = open('first_letters.txt','w')
first_letter = word[0] + '\n' + word2[0]
x.write(first_letter)'''


'''def y():
    x = open('dictionary.txt','r')
    data = x.readlines()
    return len(data)
length = y()
print (length)'''

'''letters = {}
total = 0
number = 97
x = open('dictionary.txt','r')
data = x.readlines()
while True:
    count = 0
    for i in data:
        if i[0] == chr(number):
            count += 1
            letters[chr(number)] = count
    number += 1
    if number == 123:
        print (letters)
        break
for i in letters:
    total += letters[i]
print (total)
value = list(letters.values())
maximum = max(value)
minimum = min(value)
for i in letters:
    if letters[i] == maximum:
        print (i)
    elif letters[i] == minimum:
        print (i)'''

'''for i in data:
    i = i.strip()
    if i[0] == chr(number):
        letters[chr(number)] += 1
print (letters)''' 

'''letter1 = input('pick a letter  ')
letter2 = input('pick another letter  ')
letter3 = input('pick one final letter  ')
x = open('dictionary.txt','r')
data = x.readlines()
for i in data:
    if letter1 in i and letter2 in i and letter3 in i:
        print (i)'''

'''x = open('dictionary.txt','r')
data = x.readlines()
for i in data:
    i = i.strip()
    if i[-1] == 'y':
        print (i)'''

'''import os
file = input('enter a file name  ')
if os.path.isfile(file):
    print ('file found')
else:
    print ('file not found')'''


'''x = open('numbers.txt','w')
for i in range(10000,20000,1):
    i = str(i)
    if i == i[::-1]:
        x.write(i + '\n')
x.close()'''

'''x = open('sentence1.txt','r')
data = x.read()
y = open('sentence2.txt','r')
data2 = y.read()
print (data + data2)'''

'''x = open('animals.txt','r')
data = x.read()
data = data.replace(' ','_')
print (data)'''

'''x = open('dictionary.txt','r')
data = x.readlines()
for i in data:
    i = i.strip()
    if i == i[::-1]:
        print (i)'''

'''number = {}
for i in range(0,21,1):
    number[i] = i * i
keys = list(number.keys())
for i in keys:
    if i % 2 == 0:
        del number[i]
print (number)'''

