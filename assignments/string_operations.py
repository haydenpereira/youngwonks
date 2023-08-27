'''sentence = 'hello world'
print (sentence[::-1])'''


'''sentence = 'the ocean is deep'
print (sentence[2::3])'''

'''word = 'the ocean is deep'
word = word.capitalize()
print (word)'''


'''strings = input('enter any number of strings with a comma to seperate them  ')
strings = strings.split(',')
for count in strings:
    print (count)'''


'''string = 'The fox waS Hungry so he wEnt ON a HUNt'
string = string.title()
string = string.split(' ')
print (string)'''


'''string = '  hayden   '
string = string.strip()
print (string)'''


'''string = 'JanFebMarAprMayJunJulAugSepNovDec'
number = int(input('pick a number between 1 and 12  '))
start = (number - 1) * 3
end = start + 3
print (string[start:end])'''

'''numbers = input('enter any amount of random numbers each seperated by spaces  ')
numbers = numbers.split(' ')
for count in numbers:
    count = int(count)
    if count % 2 == 0:
        print (count)'''


'''name = input('what is your name  ')
age = int(input('what is your age  '))
location = input('where do you live  ')
print ('Hello my name is',name,'and I am',age,'years old and I live in',location)
print ('Hello my name is {0} and I am {1} years old and I live in {2}'.format(name,age,location))'''


# a - 97 z -122 A - 65 Z - 90
'''print(chr(98))
print(chr(66))
print(ord('Z'))'''


'''string = input('enter a string  ')
for count in string:
    print (ord(count),count)'''

'''sports = ['basketball','football','volleyball','tennis','badminton']
sports = '**'.join(sports)
print (sports)
print (sports[-3])
print (sports[4:18])
print (ord(sports[14]))
if ord(sports[19]) >= 97 and ord(sports[19]) <=122 or ord(sports[19]) >= 65 or ord(sports[19]) <= 90:
    print ('{0} is part of the alphabet '.format(sports[19]))
else:
    print ('{0} is not part of the alphabet'.format(sports[19]))'''



'''strings = ' Young+ Wonks'
strings = strings.split('+')
string = strings[0] * 3
print (string)'''


'''first_name = input('what is your first name  ')
last_name = input('what is your last name  ')
username = first_name[0]+last_name
username = username.lower()
print ('{0} is your usename'.format(username))'''


'''import time
tries = 0
choice = input('would you like to sign up or login  ')
if choice == 'sign up':
    name = input('what is your name?  ')
    birth = input('what is the date of your birth seperate each number by a slash  ')
    city = input('what city do you live in  ')
    birth = birth.split('/')
    password = name[0:4]+birth[0]+birth[1]+city[0:3]
    print ('{0} is your password please rememeber it ')
else:
    name = input('what is your name?  ')
    birth = input('what is the date of your birth seperate each number by a slash  ')
    city = input('what city do you live in  ')
    birth = birth.split('/')
    password = name[0:4]+birth[0]+birth[1]+city[0:3]
    while True:
        login = input('what is your password?  ')
        if login == password:
            print ('Login successful')
            break
        else:
            print ('Access Denied')
            tries += 1
            if tries == 5:
                print ('you have been locked out for one minute')
                for i in range(60,0,-1):
                    print (i)
                    time.sleep(1)'''



'''music_notes = input('enter music notes all seperated by commas  ')
notes = music_notes.split(',')
for i in notes:
    i = i.lower()
    print (i)'''



