'''import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
white = (255,255,255)
blue = (0,0,255)
color = white
while True:
    pygame.draw.circle(screen,color,(300,300),100)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                color = blue
        elif event.type == KEYUP:
            if event.key == K_SPACE:
                color = white
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()'''

'''import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
white = (255,255,255)
blue = (0,0,255)
color = white
while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            print (chr(event.key))
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()'''

'''import pygame
import random
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
color = (0,255,0)
while True:
    pygame.draw.rect(screen,color,(300,300,50,100))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()'''

'''import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
red = (255,0,0)
black = (0,0,0)
x = 300
y = 300
while True:
    screen.fill(black)
    pygame.draw.circle(screen,red,(x,y),30)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                x += 50
                if x >= 600:
                    x = 0
            if event.key == K_LEFT:
                x -= 50
                if x <= 0:
                    x = 600
            if event.key == K_UP:
                y -= 50
                if y <= 0:
                    y = 600
            if event.key == K_DOWN and event.key == KEYDOWN:
                y += 50
                if y >= 600:
                    y = 0
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()'''

'''import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
red = (255,0,0)
green = (0,255,0)
black = (0,0,0)
x1 = 275
y1 = 0
x2 = 275
y2 = 550
move = True
while True:
    screen.fill(black)
    pygame.draw.rect(screen,green,(x1,y1,50,50))
    pygame.draw.rect(screen,red,(x2,y2,50,50))
    if y1 != 250:
        y1 += 2
    if y1 == 250 and move != False:
        x1 += 2
    if y2 != 300:
        y2 -= 2
    if y2 == 300:
        x2 -= 2
    if x1 >= 600:
        move = False
        x1 -= 2
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()'''

'''import random
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
for i in range(1,11,1):
    coordinates = (random.randint(0,600),random.randint(0,600))
    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    pygame.draw.rect(screen,color,(coordinates[0],coordinates[1],20,20))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()'''

'''import random
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
x = 0
coord = []
color_list = []
for i in range(1,11,1):
    coordinates = (random.randint(0,600),random.randint(0,600))
    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    coord.append(coordinates)
    color_list.append(color)
while True:
    for i in coord:
        pygame.draw.rect(screen,color_list[x],(i[0],i[1],20,20))
        x += 1
    x = 0
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()'''

'''import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
red = (255,0,0)
green = (0,255,0)
black = (0,0,0)
y1 = 0
y2 = 550
move1 = True
speed = 2
while True:
    screen.fill(black)
    pygame.draw.rect(screen,green,(275,y1,50,50))
    pygame.draw.rect(screen,red,(275,y2,50,50))'''
'''if y1 != 250 and move1 == True:
        y1 += 2
    elif y1 <= 250:
        y1 -= 2
        move1 = False
    if y2 != 300 and move1 == True:
        y2 -= 2
    elif y2 >= 300 and move1 == False:
        y2 += 2
    if y1 <= 0:
        move1 = True
    y1 += speed
    y2 -= speed
    if y1 >= 250 or y1 <= 0:
        speed = -speed
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()'''

'''import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
red = (255,0,0)
black = (0,0,0)
x = 300
y = 300
up_down = None
right_left = None
while True:
    screen.fill(black)
    pygame.draw.circle(screen,red,(x,y),30)
    if right_left == 'right':
        x += 3
    elif right_left == 'left':
        x -= 3
    elif up_down == 'up':
        y -= 3
    elif up_down == 'down':
        y += 3
    if y <= 0:
        y = 600
    if x <= 0:
        x = 600
    elif x >= 600:
        x = 0
    for event in pygame.event.get():
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                right_left = None
            elif event.key == K_LEFT:
                right_left = None
            elif event.key == K_UP:
                up_down = None
            elif event.key == K_DOWN:
                up_down = None
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                right_left = 'right'
            if event.key == K_LEFT:
                right_left = 'left'
            if event.key == K_UP:
                up_down = 'up'
            if event.key == K_DOWN:
                up_down = 'down'
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()'''

'''import random
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
black = (0,0,0)
color = [(255,0,0),(0,0,255)]
location = []
counter = 0
for i in range(1,7,1):
    coordinate = (random.randint(0,600),random.randint(0,600))
    location.append(coordinate)
while True:
    screen.fill(black)
    pygame.draw.circle(screen,random.choice[color],location[counter],50)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()'''

'''import random
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
black = (0,0,0)
white = (255,255,255)
trigger_var = None
while True:
    if trigger_var == 'up':
        coordinate = (random.randint(0,600),random.randint(0,600))
        pygame.draw.rect(screen,white,(coordinate[0],coordinate[1],20,20))
    elif trigger_var == 'down':
        coordinate = (random.randint(0,600),random.randint(0,600))
        pygame.draw.circle(screen,(255,0,0),(coordinate[0],coordinate[1]),10)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                trigger_var = 'up'
            elif event.key == K_DOWN:
                trigger_var = 'down'
        if event.type == KEYUP:
            if event.key == K_UP:
                trigger_var = None
            if event.key == K_DOWN:
                trigger_var = None
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()'''

'''import random
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
black = (0,0,0)
color = [(255,0,0),(0,0,255)]
color2 = []
location = []
counter = 0
red_blue = None
for i in range(1,7,1):
    coordinate = [random.randint(0,600),random.randint(0,600)]
    color2.append(random.choice(color))
    location.append(coordinate)
while True:
    screen.fill(black)
    for i in location:
        pygame.draw.circle(screen,color2[counter],(i[0],i[1]),50)
        if color2[counter] == (255,0,0):
            if red_blue == 'swap':
                i[1] -= 2
                if i[1] <= 0:
                    i[1] = 600
            elif red_blue == True:
                i[0] += 2
                if i[0] >= 600:
                    i[0] = 0
        elif color2[counter] == (0,0,255):
            if red_blue == 'swap':
                i[0] -= 2
                if i[0] <= 0:
                    i[0] = 600
            elif red_blue == True:
                i[1] += 2
                if i[1] >= 600:
                    i[1] = 0
        counter += 1
    counter = 0
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                red_blue = True
        if event.type  == KEYUP:
            if event.key == K_SPACE:
                red_blue = 'swap'
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()'''

'''import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
def text(msg,x,y,color,size):
    font_object = pygame.font.SysFont('Lobster',size)
    message_object = font_object.render(msg,False,color)
    screen.blit(message_object,(x,y))
white = (255,255,255)
character = ''
while True:
    screen.fill((0,0,0))
    text(character,300,300,white,100)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            character = chr(event.key)
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()'''

'''import random
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
location = (random.randint(50,550),random.randint(50,550))
def text(msg,x,y,color,size):
    font_object = pygame.font.SysFont('Lobster',size)
    message_object = font_object.render(msg,False,color)
    screen.blit(message_object,(x,y))
def text2(msg,x,y,color,size):
    font_object = pygame.font.SysFont('Impact',size)
    message_object = font_object.render(msg,False,color)
    screen.blit(message_object,(x,y))
letter = chr(random.randint(97,122))
score = 0
lost = False
while True:
    screen.fill((0,0,0))
    if lost == True:
        text2('You lost',150,200,(255,0,0),100)
    text(str(score),0,0,(0,255,0),100)
    pygame.draw.circle(screen,(0,0,255),(location[0],location[1]),60)
    text(letter,location[0] - 31,location[1] - 40,(255,255,255),120)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if chr(event.key) == letter:
                score += 1
                location = (random.randint(50,550),random.randint(50,550))
                letter = chr(random.randint(97,122))
            else:
                lost = True
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()'''

'''import random
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
color = (255,0,0)
while True:
    pygame.draw.circle(screen,color,(300,300),30)
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if event.pos[0] in range(270,330) and event.pos[1] in range(270,330):
                    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()'''

'''import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
x = 300
y = 300
while True:
    screen.fill((0,0,0))
    pygame.draw.circle(screen,(255,255,255),(x,y),20)
    for event in pygame.event.get():
        if event.type == MOUSEMOTION:
            x = event.pos[0]
            y = event.pos[1]
            x,y = event.pos
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()'''

'''import random
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
color = (255,255,255)
shape = 'circle'
x = 300
y = 300
while True:
    screen.fill((0,0,0))
    if shape == 'rectangle':
        pygame.draw.rect(screen,color,(x,y,40,20))
    else:
        pygame.draw.circle(screen,color,(x,y),10)
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            x,y = event.pos
            color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            if shape == 'circle':
                shape = 'rectangle'
            else:
                shape = 'circle'
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()'''

'''import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
a = 0
while True:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            a += 1
            if a == 1:
                point1 = event.pos
            if a == 2:
                point2 = event.pos
                pygame.draw.line(screen,(255,255,255),point1,point2,20)
                a = 0
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()'''

'''import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
x = 300
y = 300
a = None
while True:
    if a == True:
        x = event.pos[0]
        y = event.pos[1]
    screen.fill((0,0,0))
    pygame.draw.circle(screen,(255,255,255),(x,y),20)
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.pos[0] in range(x - 20,x + 20) and event.pos[1] in range(y - 20,y + 20):
                a = True
        if event.type == MOUSEBUTTONUP:
            a = None
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()'''

'''import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
x1 = x2 = y1 = y2 = 0
while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            x1 = event.pos[0]
            y1 = event.pos[1]
        if event.type == MOUSEBUTTONUP:
            x2 = event.pos[0]
            y2 = event.pos[1]
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.draw.rect(screen,(255,255,255),(x1,y1,x2 - x1,y2 - y1))
    pygame.display.update()'''

'''import random
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
clicks = 0
while True:
    pygame.draw.rect(screen,(255,255,255),(0,0,20,20))
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.pos[0] in range(0,20) and event.pos[1] in range(0,20):
                clicks += 1
                if clicks == 2:
                    clicks = 0
                    pygame.draw.rect(screen,(255,255,255),(random.randint(0,600),random.randint(0,600),20,20))
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()'''

'''import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
clicks = 0
l = 10
w = 10
while True:
    pygame.draw.rect(screen,(255,255,255),(0,0,l,w))
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.pos[0] in range(0,l) and event.pos[1] in range(0,w):
                clicks += 1
                if clicks == 2:
                    clicks = 0
                    l *= 2
                    w *= 2
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()'''

'''import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
clicks = 0
l = 10

while True:
    screen.fill((0,0,0))
    pygame.draw.circle(screen,(255,255,255),(300,300),l)
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if event.pos[0] in range(300 - l,300 + l) and event.pos[1] in range(300 - l,300 + l):
                    clicks += 1
                    if clicks == 2:
                        clicks = 0
                        l *= 2
            elif event.button == 3:
                if event.pos[0] in range(300 - l,300 + l) and event.pos[1] in range(300 - l,300 + l):
                    l = l // 2
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()'''

'''import random
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
clicks = 0
while True:
    pygame.draw.rect(screen,(255,255,255),(0,0,20,20))
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.pos[0] in range(0,20) and event.pos[1] in range(0,20):
                clicks += 1
                if clicks == 2:
                    clicks = 0
                    pygame.draw.rect(screen,(255,255,255),(random.randint(0,600),random.randint(0,600),20,20))
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()'''

'''import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
color = red
while True:
    pygame.draw.rect(screen,blue,(550,550,50,50))
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.pos[0] in range(550,600) and event.pos[1] in range(550,600):
                screen.fill((0,0,0))
                pygame.draw.circle(screen,color,(300,300),20)
                if color == red:
                    color = green
                elif color == green:
                    color = red
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()'''

'''import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
position_x = None
position_y = None
while True:
    for event in pygame.event.get():
        if event.type == MOUSEMOTION:
            position_x = event.pos[0]
            position_y = event.pos[1]
            if event.pos[0] > position_x:
                print ('West')
            elif event.pos[0] < position_x:
                print ('East')
            elif event.pos[1] < position_y:
                print ('South')
            elif event.pos[1] > position_y:
                print ('North')
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()'''

'''import random
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
location = (random.randint(50,550),random.randint(50,550))
def text(msg,x,y,color,size):
    font_object = pygame.font.SysFont('Lobster',size)
    message_object = font_object.render(msg,False,color)
    screen.blit(message_object,(x,y))
def text2(msg,x,y,color,size):
    font_object = pygame.font.SysFont('Impact',size)
    message_object = font_object.render(msg,False,color)
    screen.blit(message_object,(x,y))
letter = chr(random.randint(97,122))
score = 0
lost = False
while True:
    screen.fill((0,0,0))
    if lost == True:
        text2('You lost',150,200,(255,0,0),100)
    text(str(score),0,0,(0,255,0),100)
    pygame.draw.circle(screen,(0,0,255),(location[0],location[1]),60)
    text(letter,location[0] - 31,location[1] - 40,(255,255,255),120)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if chr(event.key) == letter:
                score += 1
                location = (random.randint(50,550),random.randint(50,550))
                letter = chr(random.randint(97,122))
            else:
                lost = True
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()'''

'''import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
shape = None
while True:
    screen.fill((0,0,0))
    if shape == 'circle':
        pygame.draw.circle(screen,red,(300,300),20)
    elif shape == 'square':
        pygame.draw.rect(screen,green,(290,290,20,20))
    pygame.draw.rect(screen,blue,(550,550,50,50))
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.pos[0] in range(550,600) or event[1] in range(550,600):
                if shape == 'square' or shape == None:
                    shape = 'circle'
                else:
                    shape = 'square'
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()'''

'''import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
color = red
x = False
while True:
    for event in pygame.event.get():
        if event.type == MOUSEMOTION and x == True:
            pygame.draw.rect(screen,color,(event.pos[0],event.pos[1],20,20))
            if color == red:
                color = green
            elif color == green:
                color = red
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()'''


import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
red = (255,0,0)
while True:
    pygame.draw.rect(screen,red,(275,275,50,50))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
