'''l = ['apple','banana','pear','orange','grape']
l[2] = 'kiwi'#replacing an element
#l.append('watermelon')
l.insert(2,'peach')
if 'orange' in l:
    print ('present')
else:
    print ('not here')
l.remove('grape')
l.pop(1)
print (l)'''


'''days = ['Monday','Tuesday','Wednesday','Friday']
favorite_day = input('what is your favorite day?')
if favorite_day in days:
    print ('it is present')
else:
    question = input('your favorite day is not in the list do you want to add it?')
    if question == 'yes':
        position = int(input('where would you like to add the in the list?'))
        position -= 1
        days.insert(position,favorite_day )
print (days)'''

'''position = int(input('what position do you want to replace '))
day = input('what day do you want to replace it with ')
position -= 1
days[position] = day
print (days)'''




'''flowers = ['sunflower','orchid','columbine','tulip','periwinkle']
flowers.pop(1)
print (flowers)'''



'''stationary = []
for count in range (1,6,1):
    item = input('enter a stationary item  ')
    stationary.append(item)
print (stationary)'''


'''flowers = ['sunflower','orchid','columbine','tulip','periwinkle']
length = len(flowers)
print (length)'''

'''numbers = [5,6,2,12,8]
numbers[2] += 5
print (numbers)'''


'''numbers = [5,6,2,12,8]
for number in range(0,len(numbers),1):
    numbers[number] += 5
print (numbers)'''


'''numbers = [5,6,2,12,8]
for number in numbers:
    number += 5
    print (number)'''


'''numbers = [4,12,67,43,82]
numbers.sort()
numbers.reverse()
print (numbers[0])
print (numbers[len(numbers) - 1])
print (numbers)'''


'''numbers = [4,12,67,43,82]
high = max(numbers)
low = min(numbers)
print (high)
print (low)'''

#numbers.sort(reverse = 1)

'''import random
numbers = []
while True: 
    number = random.randint(1,200)
    if number not in numbers:
        numbers.append(number)
    if len(numbers) == 50:
        break
    
print (numbers)'''


'''passwords_attempted = 0
password = 'hayden' 
passwords_wrong = []
while True:
    passwords_tried = input('enter password    ')
    if passwords_tried == password:
        print ('correct password')
        break
    else:
        print ('wrong please try again')
        passwords_attempted += 1
        passwords_wrong.append(passwords_tried)
        if passwords_attempted == 3:
            print ('you got too many failed atttempts')
            break        
print ('these are the passwords you got wrong',passwords_wrong)'''



        
'''import random
numbers = []
for count in range(1,21,1):
    number = random.randint(1,200)
    print (number)
    numbers.append(number)
greatest = max(numbers)
least = min(numbers)
print (numbers)
print (greatest,'is the greatest number')
print (least,'is the lowest number')'''



'''import random
numbers = []
for count in range(1,21,1):
    number = random.randint (1,100)
    numbers.append(number)
numbers.sort()
numbers.reverse()
print (numbers)
print (numbers[1])'''


'''fruits = ['apple','pear','orange']
sentence = '-'.join(fruits)
print (sentence)'''


'''letters = ['h','a','y','d','e','n']
name = ''.join(letters)
print (name)'''


'''word = 'apple'
letters = list(word)
print (letters)'''


'''sentence = 'hello how-are you'
words = sentence.split('e')
print (words)'''

#birthdate = input('when were you born  ')
##birthday = birthdate.split('/')
'''birthday.pop(2)
birthday.append('2022')
birthday.pop(0)
birthday.insert(0,'12')'''
#birthday[0] = '11'
#birthday[2] = '2022'
#print (birthday)

'''import random
fruits = ['apple','pear','orange']
random.shuffle(fruits)
print (fruits)'''


'''import random
characters = ['mickey mouse','goofy','tom','jerry','minnie mouse','popeye','woody wood pecker']
for count in range(1,11,1):
    random.shuffle(characters)
print (characters[0])'''


'''numbers = []
for count in range(1,1001,1):
    if count % 5 == 0 and count % 15 != 0:
        numbers.append(count)
print (numbers)'''


'''length = []
words = ['hello','word','apple','orange','laptop','couch','pencil','eraser','rubber','phone']
for count in range(0,10,1):
    length.append(len(words[count]))
print (length)'''



'''import random
numbers = []
for count in range(1,11,1):
    number = random.randint(1,20)
    if number < 5:
        numbers.append('bing')
    else:
        numbers.append(number)
print (numbers)'''


'''numbers = [5,10,15,20,25]
for count in range(0,5,1):
    numbers[count] += 10
print (numbers)'''


'''import random
place = input('enter any place name    ')
word = list(place)
random.shuffle(word)
string = ''.join(word)
print (string)'''



'''sentence = input('enter any sentence  ')
words = sentence.split(' ')
words2 = []
for value in words:
    if len(value) >= 3:
        words2.append(value)'''
'''for count in range(0,len(words),1):
    if len(words[count]) >= 3:
        words2.append(words[count])'''
#print (words2)




'''words = ['house','computer','pencil','book','window']
letter = input('enter any letter  ')
for value in words:
    if letter in value:
        print (value,value.index(letter))'''


'''import random
words = ['house','computer','pencil','book','window'] 
random_word = random.choice(words) 
print (random_word) '''

'''import random
words = ['house','computer','pencil','book','window']
random_word = random.sample(words,2)
print (random_word)'''

'''import random
numbers = []
num = []
for count2 in range(1,21,1):
     number = random.randint(1,100)
     num.append(number)   
for value in range(1,count2 + 1,1):
    numbers.append(value)
print (numbers)
num2 = count2 // 2
for count in range(0,num2,1):
    print (numbers[count],end = ' ')
print ()
for count2 in range(num2,len(numbers),1):
    print (numbers[count2],end = ' ')'''


'''length = []
words = ['house','plant','laptop','python','hay','den','hat','couch','bag','code']
for value in range(0,10,1):
    length1 = len(words[value])
    length.append(length1)
print (words)
print (length)'''


'''import random
words = ['house','computer','pencil','book','window']
random_word = random.choice(words)
print (random_word)
change = list(random_word)
random.shuffle(change) 
string = ''.join(change)
print (string)'''



'''symbol = []
word = input('choose any word  ')
word2 = list(word)
length = len(word2)
for count in range(0,length,1):
    symbol.append('*')
print (word2)
print (symbol)'''



'''symbol = ['*']
word = input('enter any word  ')
length = len(word)
symbols = symbol * length
print (word)
print (symbols)'''





'''words = ['house','plant','laptop','python','hay','den','hat','couch','bag','code']
words_new = []
for count in range(len(words)):
    if count % 2 != 0:
        words_new.append(words[count])
print (words)
print (words_new)'''


'''name = ['hayden','chelsea','james','bob','rick']
letters = []
for count in range(0,len(name),1):
    name1 = list(name[count][1])
    letters.append(name1)
print (name)
print (letters)'''
    

'''letters = []
name = ['hayden','chelsea','james','bob','rick']
for value in name:
    print (value[1])
    letters.append(value[1])
print (letters)'''



'''import random
num = []
for count2 in range(1,21,1):
     number = random.randint(1,100)
     num.append(number)   
half = len(num) // 2
for count in range(0,half,1):
    print (num[count],end = ' ')
print()
for count3 in range (half,len(num),1):
    print (num[count3],end = ' ')'''
'''num2 = count2 // 2
for count in range(0,num2,1):
    print (num[count],end = ' ')
print ()
for count2 in range(num2,len(num),1):
    print (num[count2],end = ' ')'''



'''tries = 0
import random
blank = ['_']
words = ['table','house','window','balloon','cactus']
for count1 in range(0,len(words),1):
    word = random.choice(words)
    length = len(word)
    underscore = blank * length
    print (underscore)
    while True:
        letter = input('guess a letter   ')
        if letter in word:
            for count in range(0,len(word),1):
                if letter == word[count]:
                    underscore[count] = letter               
        else:
            print ('please try again')
            tries += 1
            if tries == 3:
                break             
        print (underscore)
        if '_' not in underscore:
            print ('congrats!!!')
            break        
    words.remove(word)
    break
print ('you failed to guess a letter',tries,'times')
print ('you took too many tries, you have failed')'''





'''words = []
while True:
    word = input('enter any word   ')
    if 'a' == word[0]:
        words.append(word)
    else:
        break
print (words)'''


'''import random
sentence = input('enter any sentece with 5 words minimum   ')
sentence_list = sentence.split(' ')
random.shuffle(sentence_list)
print (sentence_list [4])'''



'''import random
numbers = []
while True:
    number = random.randint(0,100)
    if number not in numbers:
        numbers.append(number)
    if len(numbers) == 50:
        break
print (numbers)
print (len(numbers))'''



'''total = 0
marks = [90,78,34,56,99,12,34,78,53,100]
for count in range(0,len(marks),1):
    total = total + marks[count]
average = total / len(marks)
print (total)
print (average)'''



'''fruits = ('apple','orange','pear','plums','mango')
print (fruits[2])
print (len(fruits))'''

'''months = ('jan','feb','mar','apr','may','jun','jul','agu','sep','oct','nov','dec')
month = int(input('choose a number between 1 and 12  '))
print (months[month - 1])'''


'''john_marks = [90,89,99,78,85]
#print (john_marks[0])
bob_marks = [89,56,34,100,87]
rick_marks = [45,23,67,56,89]
marks = [john_marks,bob_marks,rick_marks]
print (marks)
print (marks[2][3])'''



'''collections = []
for count in range(1,4,1):
    items = []
    for count1 in range(1,4,1):
        value = input('enter a value  ')
        items.append(value)
    collections.append(items)
print (collections)'''



'''animals = ('cat','dog','elephant','parrot','lion')
sounds = ('meow','bark','trumpet','squawk','roar')
for count in range(0,len(animals),1):
    print (animals[count],sounds[count])
    '''



'''words = ('big','hot','nice','smart')
opposites = ('small','cold','rude','dumb')
for count in range(0,len(words),1):
    print (words[count],end = ' ')
    print ('and',opposites[count])'''



'''import random
for count in range(1,4,1):
    numbers = random.randint(1,100)'''


'''groceries = ['cabbage','apples','celery']
toys = ['helicopter','car','baseball bat']
accessories = ['purse','hair band','earring']
super_market = (groceries,toys,accessories)
for count in range(0,3,1):
    print ()
    for count1 in range(0,3,1):
        print (super_market[count][count1],end = ' ')'''

'''count = 0
names = ['jimmy','bob','alex','hayden','rick','chelsea','grinal','leon','ashley','mike']
letters = []
for i in names:
    letters.append(i[count])
    count += 1
    if count == len(i) - 1:
        count = 0
print (letters)'''

'''import random
numbers = []
for i in range(1,11,1):
    number = random.randint(1,20)
    numbers.append(number)
print (numbers)
for i in numbers:
    if i > 10:
        print (i,'is greater than 10')
numbers = numbers.reverse()
print (numbers)'''

'''word = input('enter a word  ')
letters = {}
for i in word:
    if i not in letters:
        letters[i] = 1
    elif i in letters:
        letters[i] += 1
print (letters)'''

'''import random
numbers = []
for i in range(1,4,1):
    number = random.randint(100,999)
    numbers.append(number)
print (numbers)
print (max(numbers))
print (min(numbers))'''

'''import random
numbers = {}
for i in range(1,21):
    numbers[i] = random.randint(1,10)
for i in numbers:
    print (i,':',numbers[i])'''

'''words = ['elephant','table','paper','building','computers','globe','soap']
words2 = {}
vowels = ['a','e','i','o','u']
for word in words:
    for letter in word:
        if letter in vowels and word in words2:
            words2[word] += 1
        elif letter not in vowels:
            pass
        else:
            words2[word] = 1
print (max(words2))'''
        
'''selling_list = []
while True:
    choice = input('would like to add an item to the list or remove something? ')
    if choice == 'add':
        add_item = input('what would you like to add to the list? ')
        selling_list.append(add_item)
    elif choice == 'remove':
        remove_item = input('what would you like to remove ')
        if remove_item in selling_list:
            selling_list.remove(remove_item)
        elif remove_item not in selling_list:
            print ('Sorry, that item is not on the list')  
    elif choice == 'stop' or choice == 'quit':
        break
print (selling_list)'''

'''favorites = {'Alex': {'Desert' : 'Ice-cream','Sport' : 'Hockey'}, 'John': {'Desert' : 'Cheesecake','Sport' : 'Soccer'}}
for i in favorites:
    print (i) 
    for x in favorites[i]:
        print ('{0}:{1}'.format(x,favorites[i][x]))'''

'''def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
    else: 
        leap = False
    return leap
year = int(input())
print(is_leap(year))'''

'''records = {'Hayden': 17, 'Joe': 19, 'Bob': 23, 'Rick': 12, 'Ashley': 20}
choice = input('would like to add a record, delete a record, or update a score ')
if choice == 'add':
    name = input('what is the name of the student ')
    score = int(input('what is the score of the student '))
    records[name] = score
elif choice == 'delete':
    deletion = input('which name would you like to delete ')
    del(records[deletion])
elif choice == 'update':
    update_name = input('which name would you like to update ')
    update_score = int(input('enter their new score '))
    records[update_name] = update_score
print (records)'''

'''items = ['computer','window','house','towels','zebra','box','wires','bread board']
letter = input('enter a letter ')
for i in items:
    if letter in i:
        print (i)'''
'''count = 0
words = ['computer','window','house','towels','zebra','box','wires','bread','board','ten']
for i in words:
    words.pop(count)
    count += 1
print (words)'''

'''import random
numbers = []
for i in range(0,20):
    num = random.randint(-30,30)
    numbers.append(num)
print (numbers)
for i in range(0,20):
    numbers[i] += 10
print (numbers)'''

'''items = ['computer','window','house','towels','zebra','box','wires','bread board']
letter = input('enter a letter ')
for i in items:
    if letter in i:
        print (i)
        print (i.index(letter))'''

word_string = input('enter a string ')
'''words_dict = {}
for i in range(0,len(word_string),1):
    if word_string[i] in words_dict:
        words_dict[word_string[i]].append(i)
    else:
        words_dict[word_string[i]] = [i]
print(words_dict)'''

