'''import random
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
white = (255,255,255)
object_list = []
class Circle:
    def __init__(self):
        self.radius = 20
        self.x = random.randint(0,600)
        self.y = random.randint(0,600)
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    def draw(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
for i in range(0,10,1):
    object = Circle()
    object_list.append(object) 
while True:
    for i in object_list:
        i.draw()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()'''

'''import random
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
x_circle = 0
y_circle = 100
object_list = []
direction = 'right'
def text(msg,x,y,color,size):
    font_object = pygame.font.SysFont('Lobster',size)
    message_object = font_object.render(msg,False,color)
    screen.blit(message_object,(x,y))
class Circle:
    def __init__(self,x,y):
        self.radius = 25
        self.x = x
        self.y = y
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.speed = random.randint(1,4)
        self.key = random.randint(97,122)
        self.flag = True
    def draw(self):
        if self.flag == True:
            pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
            text(chr(self.key),self.x - 10,self.y - 10,(0,0,0),40)
    def move(self):
        self.x += self.speed
        if self.x > 600:
            self.speed = -self.speed
        elif self.x <= 0:
            self.speed = -self.speed
for i in range(0,30,1):
    x_circle += 60
    object1 = Circle(x_circle,y_circle)
    object_list.append(object1)
    if x_circle >= 600:
        y_circle += 200
        x_circle = 0
while True:
    screen.fill((0,0,0))
    for i in object_list:
        i.draw()
        i.move()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            for i in range(0,len(object_list),1):
                if chr(event.key) == chr(object_list[i].key):
                    if object_list[i].flag == True:
                        object_list[i].flag = False
                    else:
                        object_list[i].flag = True

        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()'''

'''import random
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
class Circle:
    def __init__(self,y):
        self.lap_count = 0
        self.speed = random.randint(4,13)
        self.x = 31
        self.y = y
        self.color = (255,255,255)
        self.finished = False
    def draw(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),30)
    def move(self):
        global finishers
        self.x += self.speed
        if self.x >= 570:
            self.speed = -self.speed
        elif self.x <= 30:
            self.speed = -self.speed
            self.lap_count += 1
        if self.lap_count == 5:
            finishers += 1
            if finishers == 1:
                self.color = (255,0,0)
                self.speed = 0
            elif finishers == 2:
                self.color = (0,255,0)
                self.speed = 0
            elif finishers == 3:                   
                self.color = (0,0,255)
                self.speed = 0
            else:
                self.speed = 0
object_list = []
finishers = 0 
y_circle = 30
start = False
for i in range(0,10,1):
    object1 = Circle(y_circle)
    object_list.append(object1)
    y_circle += 75
while True:
    screen.fill((0,0,0))
    for i in object_list:
        i.draw()
        if start == True:
            i.move()
            #for i in object_list:
                #i.draw()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                start = True
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()'''

'''import random
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
object_list = []
increase = False
decrease = False
class Circle:
    radius = 30
    def __init__(self):
        self.x = random.randint(0,600)
        self.y = random.randint(0,600)
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    def draw(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
for i in range(0,10,1):
    object1 = Circle()
    object_list.append(object1)
while True:
    screen.fill((0,0,0))
    for i in object_list:
        i.draw()
        if increase == True:
            Circle.radius += 0.2
        if decrease == True:
            Circle.radius -= 0.2
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
           # if event.button == 1:
            for i in object_list:
                if event.pos[0] in range(i.x - 30,i.x + 30) and event.pos[1] in range(i.y - 30,i.y + 30):
                    if event.button == 1:
                        i.radius += 2
                    if event.button == 3:
                        i.radius -= 2
        if event.type == KEYDOWN:
            if event.key == K_UP:
                Circle.radius += 2
                #increase = True
            if event.key == K_DOWN:
                Circle.radius -= 2
                #decrease = True
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()'''

import random
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
object_list = []
class Circle:
    radius = 30
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.color = random.choice([red,blue])
        self.speedx = 2
        self.speedy = 2
    def draw(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
    def move(self):
        if self.color == red:
            self.speedy = 0
        elif self.color == blue:
            self.speedx = 0
        self.x += self.speedx
        self.y += self.speedy
        if self.x >= 570 or self.x <= 30:
            self.speedx = -self.speedx
        elif self.y >= 570 or self.y <= 30:
            self.speedy = -self.speedy
    def change(self):
        if self.color == blue:
            self.speedx = 0
            self.speedy = 2
        elif self.color == red:
            self.speedx = 2
            self.speedy = 0
for i in range(0,20,1):
    object1 = Circle(random.randint(50,550),random.randint(50,550))
    object_list.append(object1)
while True:
    screen.fill((0,0,0))
    for i in object_list:
        i.draw()
        i.move()
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            for i in object_list:
                if event.pos[0] in range(i.x - 30,i.x + 30) and event.pos[1] in range(i.y - 30, i.y + 30):
                    if i.color == red:
                        i.color = blue
                    elif i.color == blue:
                        i.color = red
                i.change()
                i.move()
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
    