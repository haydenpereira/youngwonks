#scores = {'bob': 12,'james':10,'hayden': 9, 'chelsea': 7,'rick': 5}
'''scores['hayden'] = 20
scores['emily'] = 11
print (list(scores.keys()))
print (list(scores.values()))
del scores['bob']
print (len(scores))'''
'''for key in scores:
    print (key,scores[key])




print (scores['hayden'])
print (scores)'''



#favorite_foods = {'hayden': 'pizza','james': 'cupcakes','chelsea': 'cake','bob': 'apple'}
'''print (favorite_foods['bob'])
favorite_foods['emily'] == 'pear'''
'''if 'james' in favorite_foods:
    print (favorite_foods['james'])''' 





'''login_data = {'hayden': 1234,'bob3':4321,'james':2345,'chelsea': 10987,'bob1':3232}
choice = input('do you want to login or register  ')
if choice == 'login':
    username = input('what is your username  ')
    if username in login_data:
        password = int(input('what is your password  '))
        if password == login_data[username]:
            print ('login successful')
    else:
        choice2 = input('your login failed do you want to register  ')
        if choice2 == 'yes':
            while True:
                new_username = input('enter your new username  ')
                if new_username in login_data:
                    print ('your username has already been used enter another username  ')
                else:
                    new_password = input('enter your new password  ')
                    login_data[new_username] = new_password
                    break
elif choice == 'register':
    while True:
        new_username = input('enter your new username  ')
        if new_username in login_data:
            print ('your username has already been used enter another username  ')
        else:
            new_password = input('enter your new password  ')
            login_data[new_username] = new_password
            break        
print (login_data)'''




'''items = {'plant':5.99,'carpet':10.99,'pen': .99}
print (items)
new_item = input('pick any item that you want to add to the list of items  ')
new_item2 = input('pick another item that you want to add to the list of items  ')
price = input('now choose the price of the first item  ')
price2 = input('choose the price of the second item  ')
items[new_item] = price
items[new_item2] = price2
print (items)
remove = input('now pick an item from the list that you want to remove  ')
remove2 = input('now pick another item from the list that you want to remove  ')
del items[remove]
del items[remove2]
print (items)'''





'''items = {'plant':5.99,'carpet':10.99,'pen': .99,'bed':100,'pencil':.20}
print (list(items.keys()))
purchase = input('which item do you want to buy  ')
if purchase in items:
    print (items[purchase])
else:
    print ('we dont have that item, please try another store')'''




'''family = {'hayden': 1234,'chelsea': 4321,'leon':2341,'grinal':1603}
account = input('what is your username  ')
if account in family:
    password = int(input('what is the password  '))
    if password == family[account]:
        print ('access granted  ')
    else:
        print ('access denied ')
else:
    print ('No account found  ')'''


'''correct_answers = 0
quiz = {'1 + 1': 2,'12 * 12': 144,'43 + 59': 102,'10 to the power of 3 is equal to? ': 1000,'6 * 6': 36}
for i in quiz:
    print (i)
    print (quiz[i])
for count in quiz:
    answer = int(input(count)  )
    if answer == quiz[count]:
        correct_answers += 1
        print ('CORRECT!!!')
    else:
        print (quiz[count],'is the correct answer')
print ('you got ',correct_answers,' questions correct')'''



'''numbers = {}
for count in range(1,21,1):
    value = count * count 
    numbers[count] = value
print (numbers)'''


'''import random
numbers = {}
for count in range(1,11,1):
    random_number = random.randint(20,30)
    numbers[count] = random_number
for i in numbers:
    if i % 2 == 0:
        print (i,numbers[i])'''



'''items = {'plant':5.99,'carpet':10.99,'pen': .99,'bed':100,'pencil':.20}
for count in items:
    if count[0] == 'p':
        print (count,items[count])'''


'''letters = {}
sentence = input('enter a sentence  ')
for count in sentence:
    if count not in letters:
        letters[count] = 1
    else:
        letters[count] += 1
print (letters)'''



'''friends = ['hayden','chelsea','james','emily']
chocolates = ['hersheys','lindor','milk chocolate','dark chocolate']
dictionary = {}
for count in range(0,4,1):
    dictionary[friends[count]] = chocolates[count]
print (dictionary)'''


'''food = {'hamburger':'','pizza':'','sandwich': ''}
for count in food:
    ingredients = input('what are the ingredients in a',count)
    food[count] = ingredients
print (food)'''    

'''import random
numbers = {}
for count in range(1,41,1):
    key = random.randint(1,30)
    value = key * key * key
    numbers[key] = value
print (numbers)'''


'''points = 0
import random
jumbled_words = {}
words = ['apple','house','computer','picture','frame','cabinet','plants','books','hamburger','dictionary']
jumbled_words_list = []
for count in words:
    list_word = list(count)
    random.shuffle(list_word)
    shuffled = ''.join(list_word)
    jumbled_words[shuffled] = count
print (jumbled_words)
for count in jumbled_words:
    question = input('what word is ' + count + ' ')
    if question == jumbled_words[count]:
        print ('CORRECT!!!')
        points += 1
    else:
        print ('incorrect')
print ('you got ',points,' out of 10 correct')'''



'''letters = {}
sentence = input('enter a sentence  ')
for count in sentence:
    if count not in letters:
        letters[count] = 1
    else:
        letters[count] += 1
print (letters)'''




'''ice_cream = {'chocolate': 2.99,'vanilla': 2.50,'cookie dough': 1.99,'chocolate chip': 2.30,'strawberry': 5.99,'macha': 3.99,'chocolate fudge': 4.60}
for count in ice_cream:
    ice_cream[count] += 5
print (ice_cream)
flavor = input('what ice cream do you want  ')
print (flavor,ice_cream[flavor])'''



'''numbers = {1:2,3:4,5:6,7:8}
for count in numbers:
    print (count,end = '')
    print (numbers[count])
    print ()'''


'''items = {'couch': 300,'basketball': 5.78,'bed': 500,'plant': 3.24,'desk': 100}
storage = {'couch': 3,'basketball': 12,'bed': 10,'plant': 18,'desk': 1}
for count in items:
    print ('the',count,'is for',items[count],'and there are',storage[count],'left in storage')'''




'''fruits = {'apple': 6,'pear': 7,'plum': 2,'orange': 15}
quantity = list(fruits.values())
quantity.sort()
for count in quantity:
    for i in fruits:
        if fruits[i] == count:
            print (i,count)'''


'''fruits = {'apple': 6,'pear': 7,'plum': 2,'orange': 15}
fruit = list(fruits.keys())
fruit.sort()
for count in fruit:
    for i in fruits:
        if count == i:
            print (count,fruits[i])'''


'''fruits = {6: 'apple',7:'pear',2:'plum',15:'orange',16:'mango'}
del(fruits['pear'])
print (fruits)
values = list(fruits.keys())
for count in values:
    if count % 2 == 0:
        del(fruits[count])
print (fruits)'''




'''turn = 'X'
board = {1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}
while True:
    for i in board:
        if i % 3 == 0:
            print (i,':',board[i])
            print ()
        else:
            print (i,':',board[i],end = ' ')
    number = int(input('where do you want to place your marker  '))
    if board[number] == '':  
        if turn == 'X':
            board[number] = turn
            turn = 'O'
        else:
            board[number] = turn
            turn = 'X'
    else:
        print ('this spot has already been taken try again')
    
    if board[1] == board[2] == board[3] != '':
        print (board[1],'wins')
        print ('c1')
        break
    elif board[4] == board[5] == board[6]:
        print (board[4],'wins')
        break
    elif board[7] == board[8] == board[9] != '':
        print (board[7],'wins')
        break
    elif board[1] == board[4] == board[7] != '':
        print (board[1],'wins')
        print ('c2')
        break
    elif board[2] == board[5] == board[8] != '':
        print (board[2],'wins')
        break
    elif board[3] == board[6] == board[9] != '':
        print (board[3],'wins')
        break
    elif board[1] == board[5] == board[9] != '':
        print (board[1],'wins')
        print ('c3')
        break
    elif board[3] == board[5] == board[7] != '':
        print (board[3],'wins')
        break
    if board[1] != board[2] != board[3] != board[4] != board[5] != board[6] != board[7] != board[8] != board[9]:
        print ('it is a tie')'''
            

            


        
        
        

'''letters = {}
sentence = input('enter a sentence ')
for count in sentence:
    print (count)
    if count not in letters:
        letters[count] = 1
    elif count in letters:
        letters[count] += 1
print (letters)'''


'''numbers = {1:[1,1],2:[4,8],3:[9,27],4:[16,64],5:[25,125],6:[36,216],7:[49,343],8:[64,512],9:[81,729],10:[100,1000],11:[121,1331],12:[144,1728],13:[169,2197],14:[196,2744],15:[225,3375],16:[256,4096],17:[289,4913],18:[324,5832],19:[361,6859],20:[400,8000]}
key = list(numbers.keys())
for i in key:
    if i % 3 == 0:
        del numbers[i]
print (numbers)'''



'''numbers = {1:'',2:'',3:'',4:'',5:'',6:'',7:'',9:'',10:''}
for i in numbers:
    if i % 2 == 0:
        numbers[i] = 'even'
    else:
        numbers[i] = 'odd'
print (numbers)'''




'''names_and_passwords = {}
names = input('enter a 5 names with a comma to seperate them  ')
passwords = input('enter 5 passwords with a comma separating each one  ')
names2 = names.split(',')
passwords2 = passwords.split(',')
for count in range(0,len(names2),1):
    names_and_passwords[names2[count]] = passwords2[count]
print (names_and_passwords)'''




'''d = {'A': 10, 'B': 20, 'C': 35, 'D': 40, 'E': 19, 'F': 11}
d2 = {}
for i in d:
    if d[i] % 10 == 0:
        d2[i] = d[i]
print (d2)'''




'''import random
numbers = {}
for count in range(0,10,1):
    number = random.randint(5,150)
    number = str(number)
    length = len(number)
    numbers[number] = length
print (numbers)'''




'''for count in range(1,101,1):
    if count % 10 != 0:
        print (count)'''

'''word = 'Youngwonks'
for count in word:
    print (count)'''

'''cars = ['toyota','honda','audi','tesla','bugatti']
cars.sort()
for count in cars:
    print (count)'''



'''import random
numbers = []
for count in range(0,10,1):
    number = random.randint(-100,25)
    numbers.append(number)
print (numbers)'''



'''names = {'hayden':23,'chelsea': 5,'leon':34,'grinal':15}
for i in names:
    if names[i] >= 16:
        print (i)'''

'''sum = 0
fruits = {'orange':3.00,'apple': 2.99,'plum':3.40,'pear':1.99,'mango':5.99}
for i in fruits:
    sum += fruits[i]
print (sum)'''


'''numbers = []
import random
while True:
    number = random.randint(1,100)
    if number % 5 == 0 and number % 2 == 0:
        numbers.append(number)
    elif len(numbers) == 5:
        break
print (numbers)'''

'''letters = {}
sentence = list(input('enter a sentence '))
for i in sentence:
    if i not in letters:
        letters[i] = 1
    else:
        letters[i] += 1
print (letters)'''

'''inventory = {'Pencil':[15, 3],'Eraser':[20, 5],'Pen':[50, 6],'Notebook':[5, 10],'Paper Weight':[20, 12]}
pencil_amount = inventory['Pencil'][0] * inventory['Pencil'][1]
eraser_amount = inventory['Eraser'][0] * inventory['Eraser'][1]
pen_amount = inventory['Pen'][0] * inventory['Pen'][1]
notebook_amount = inventory['Notebook'][0] * inventory['Notebook'][1]
paper_weight_amount = inventory['Paper Weight'][0] * inventory['Paper Weight'][1]
print (pencil_amount + eraser_amount + pen_amount + notebook_amount + paper_weight_amount,'$')'''

'''count = 0
questions = ['what is 4 + 8','what is 17 + 28','what is 4 times 4','what is 4 times 9']
answers = [12,45,16,36]
for i in questions:
    user_answer = input(i + ' ')
    if user_answer == answers[count]:
        print ('Correct!')
    elif user_answer != answers[count]:
        print ('Wrong answer!')
count += 1'''

'''info = [['Arun', 25], ['John', 40], ['Mark',34], ['Richie', 32]]
names = []
ages = []
for i in info:
    names.append(i[0])
    ages.append(i[1])
print (names)
print (ages)'''

