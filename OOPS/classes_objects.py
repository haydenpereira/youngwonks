'''class Ball:
    def __init__(self):
        self.name = 'basketball'
        self.color = 'brown'
        self.shape = 'sphere'
        self.weight = 'medium'
object = Ball()
print(object.name)'''



'''class Ball:
    def __init__(self,name,color,weight):
        self.name = name 
        self.color = color
        self.shape = 'sphere'
        self.weight = weight
    def display(self):
        print('Name:',self.name)
        print('color:',self.color)
        print('shape:',self.shape)
        print('weight:',self.weight)
object = Ball('basketball','brown','medium')
object2 = Ball('tennis ball','green','light')
object.display()
object2.display()'''

'''class Shapes:
    def __init__(self,sides,name):
        self.sides = sides
        self.name = name
    def display(self):
        print('Name:',self.name)
        print('sides:',self.sides)
object1 = Shapes(4,'square')
object2 = Shapes(0,'circle')
object3 = Shapes(3,'triangle')
object1.display()
object2.display()
object3.display()'''

'''class Dog:
    def __init__(self,name,eye_color,fur_color,breed,age):
        self.name = name
        self.eye_color = eye_color
        self.fur_color = fur_color
        self.breed = breed
        self.age = age
    def display(self):
        print('My dogs name is',self.name,'and he/she is a',self.age,'year old',self.breed,'with',self.eye_color,'eyes and',self.fur_color,'colored fur.'
)
object1 = Dog('Toby','blue','brown','golden retriever',8)
object2 = Dog('Marley','brown','black','border collie',5)
object3 = Dog('Happy','green','white','golden retriever',3)
class Person:
    def __init__(self,name,age,petlist):
        self.name = name
        self.age = age
        self.petlist = petlist
    def display(self):
        print('Name:',self.name)
        print('Age:',self.age)
        for i in self.petlist:
            print(i.name)
    def add_pet(self,object3):
        self.petlist.append(object3)
p_object = Person('Hayden',13,[object1,object2])
p_object.display()
p_object.add_pet(object3)'''

'''class Account:
    def __init__(self,name,account_num,balance):
        self.name = name
        self.account_num = account_num
        self.balance = balance
    def display(self):
        print('The name of your account is',self.name,'account number is',self.account_num,'and total balance is',self.balance,'dollars')
    def deposit(self,value):
        self.balance += value
    def withdraw(self):
        value2 = int(input('how much do you want to withdraw '))
        self.balance -= value2
object1 = Account('Hayden\'s account',934593,15)
choice = input('do you want to withdraw or deposit to your account ')
if choice == 'withdraw':
    object1.withdraw()
elif choice == 'deposit':
    amount = int(input('how much money do you want to deposit '))
    object1.deposit(amount)
object1.display()'''
'''object1.deposit()
object1.withdraw()
object1.display()'''

'''class State:
    def __init__(self,name,capital_city,population):
        self.name = name
        self.capital_city = capital_city
        self.population = population
object1 = State('California','Sacramento',20000)
object2 = State('Texas','Austin',743852)
object3 = State('Utah','Salt Lake City',818343)
object4 = State('Florida','Tallahassee',839292) 
object5 = State('Wyoming','Cheyenne',485768)
states = [object1,object2,object3,object4,object5]
choice = input('pick a state ')
for i in states:
    if choice == i.name:
        print(i.capital_city,i.population)'''


'''class Shopping_List:
    def __init__(self,name,cart):
        self.name = name
        self.cart = cart
    def add_item(self,item_name,quantity):
        self.cart[item_name] = quantity
    def remove_item(self):
        item_name2 = input('choose which item you want to remove ')
        if item_name2 in self.cart:
            del(self.cart[item_name2])
    def display(self):
        print(self.name,self.cart)
object1 = Shopping_List('Costco',{'flour':4,'tomato':5,'watermelon':6,'mango': 4,'lettuce': 7})
object2 = Shopping_List('Safeway',{'watermelon':2,'mango': 5})
shops = [object1,object2]
stop = False
choice = input('pick a shop ')
while True:
    if stop == True:
        break
    for i in shops:
        if choice == i.name:
            choice2 = input('do you want to add or remove an item or are you done shopping? ')
            if choice2 == 'add':
                item = input('which item do you want to add' )
                number = int(input('how many do you want '))
                i.add_item(item,number)
            elif choice2 == 'remove':
                i.remove_item()
            elif choice2 == 'done shopping':
                stop = True
            i.display()'''

'''class Phonebook:
    def __init__(self,phonebook):
        self.phonebook = phonebook
    def add_number(self):
        new_name = input('what is the new name ')
        new_number = int(input('what is the new number '))
        if new_number in self.phonebook:
            print('you already have this number in your phonebook ')
        else:
            self.phonebook[new_name] = new_number
        self.phonebook[new_name] = new_number
    def remove_number(self):
        name = input('which person do you want to remove ')
        print('Are you sure you want to remove',name)
        confirmation = input()
        if confirmation == 'yes':
            del(self.phonebook[name])
    def display(self):
        print(self.phonebook)
object1 = Phonebook({})
while True:
    choice = input('do you want to add or remove a phone number ')
    if choice == 'add':
        object1.add_number()
    elif choice == 'remove':
        object1.remove_number()
    object1.display()'''

class Zoo:
    def __init__(self,name,population,food,habitat):
        self.name = name
        self.population = population
        self.food = food
        self.habitat = habitat
    def display(self):
        for i in self.population:
            print('There are',self.population[i],i,'who live in a predominantly',self.habitat[i],'habitat that eat',self.food[i])
    def add(self):
        choice = input('which animal do you want to add to the zoo ')
        if choice in self.population:
            increase = int(input('how many do you want to increase it by '))
            self.population[choice] += increase
        else:
            choice2 = int(input('how many of it do you want to add '))
            choice3 = input('what does it eat ')
            choice4 = input('which habitat does it live in ')
            self.population[choice] = choice2
            self.food[choice] = choice3
            self.habitat[choice] = choice4
        self.display()
    def remove(self,name,amount):
        if amount == 'all':
            del(self.population[name])
            del(self.food[name])
            del(self.habitat[name])
        elif amount == 'some':
            amount2 = int(input('how many do you want to remove '))
            self.population[name] -= amount2
        self.display()
object1 = Zoo('Oakland zoo',{'lions':4,'elephants':6},{'lions':'meat','elephants':'sugarcane'},{'lions':'land','elephants':'land'})
zoo_choice = input('which zoo do you want to add or remove to ')
if zoo_choice == object1.name:
    choice5 = input('would you like to add, remove, or display ' )
    if choice5 == 'add':
        object1.add()
    elif choice5 == 'remove':
        choice6 = input('which animal do you want to remove ')
        choice7 = input('do you want to remove all of them or some ')
        object1.remove(choice6,choice7)
    elif choice5 == 'display':
        object1.display()
    





        
        

        





    







































































































































































































































