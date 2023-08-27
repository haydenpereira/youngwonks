'''import random
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('shapes')
red = (255,0,0)
black = (0,0,0)
x = 0
y = 0
color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
while True:
    screen.fill(black)
    pygame.draw.rect(screen,color,(x,y,100,100))
    x += 5
    if x >= 600:
        y += 100
        x = 0
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        if y >= 600:
            y = 0
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
pygame.display.set_caption('shapes')
black = (0,0,0)
color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
x = 0
y = 0
while True:
    screen.fill(black)
    pygame.draw.rect(screen,color,(x,y,100,100))
    x += 5
    y += 5
    if x >= 600 and y >= 600:
        x = 0
        y = 0
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()'''

'''import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Shapes')
white = (255,255,255)
black = (0,0,0)
x1 = 0
y1 = 0
x2 = 500
y2 = 0
while True:
    screen.fill(black)
    pygame.draw.rect(screen,white,(x1,y1,100,100))
    pygame.draw.rect(screen,white,(x2,y2,100,100))
    x1 += 5
    y1 += 5
    x2 -= 5
    y2 += 5
    if x1 == 600 and y1 == 600:
        x1 = 0
        y1 = 0
    if x2 == -100 and y2 == 600:
        x2 = 500
        y2 = 0
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()'''

'''import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Robot')
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
while True:
    pygame.draw.rect(screen,white,(225,225,150,150))
    pygame.draw.rect(screen,white,(290,165,25,60))
    pygame.draw.rect(screen,white,(250,100,100,100))
    pygame.draw.rect(screen,black,(275,125,20,10))
    pygame.draw.rect(screen,black,(320,125,20,10))
    pygame.draw.rect(screen,white,(375,225,50,20))
    pygame.draw.rect(screen,white,(425,225,20,70))
    pygame.draw.rect(screen,white,(445,280,20,30))
    pygame.draw.rect(screen,white,(405,280,20,30))
    pygame.draw.rect(screen,white,(175,225,50,20))
    pygame.draw.rect(screen,white,(155,225,20,70))
    pygame.draw.rect(screen,white,(175,280,20,30))
    pygame.draw.rect(screen,white,(135,280,20,30))
    pygame.draw.rect(screen,white,(355,375,20,100))
    pygame.draw.rect(screen,white,(225,375,20,100))
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
pygame.display.set_caption('Shapes')
green = (0,255,0)
radius = 50
expand = True
black = (0,0,0)
incremnt = 5
color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
while True:
    screen.fill(black)
    pygame.draw.circle(screen,color,(300,300),radius)
    radius += incremnt
    if radius >= 300 or radius <= 10:
        incremnt = -incremnt
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    if expand == True:
        radius += 5
    elif expand == False:
        radius -= 5
    if radius >= 300:
        expand = False
    elif radius <= 10:
        expand = True

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()'''

'''import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('shapes')
color1 = (0,0,255)
color2 = (255,0,0)
x = 0
y = 0
while True:
    pygame.draw.rect(screen,color1,(x,y,50,50))
    x += 50
    color1,color2 = color2,color1
    if x >= 600:
        y += 50
        x = 0
        color1,color2 = color2,color1
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()'''

'''import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('wagon')
brown = (158,97,17)
black = (0,0,0)
x1 = 125
x2 = 125
x3 = 475
while True:
    screen.fill(black)
    pygame.draw.rect(screen,brown,(x1,150,350,150))
    pygame.draw.circle(screen,brown,(x2,300),60)
    pygame.draw.circle(screen,brown,(x3,300),60)
    x1 += 3
    x2 += 3
    x3 += 3
    if x2 >= 600:
        x1 = -125
        x2 = -125
        x3 = 225
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()'''

'''import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('shapes')
color1 = (255,0,0)
color2 = (0,0,255)
x = 0
y = 0
def checkerboard():
    global x,y,color1,color2
    pygame.draw.rect(screen,color1,(x,y,100,100))
    x += 100
    color1,color2 = color2,color1
    if x >= 600:
        y += 100
        x = 0
        color1,color2 = color2,color1
while True:
    checkerboard()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()'''

'''import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('shapes')
red = (255,0,0)
blue = (0,0,255)
black = (0,0,0)
x1 = 50
x2 = 550
number = 2
while True:
    screen.fill(black)
    pygame.draw.circle(screen,red,(x1,300),50)
    pygame.draw.circle(screen,blue,(x2,300),50)
    x1 += number
    x2 -= number
    if (x1 >= 250 and x2 <= 350) or (x1 <= 50 and x2 >= 550):
        number = -number
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
pygame.display.set_caption('shapes')
white = (255,255,255)
yellow = (255,251,0)
black = (0,0,0)
coordinates = []
colors = [white,yellow]
for i in range(1,101,1):
    coordinate = [random.randint(0,600),random.randint(0,600)]
    coordinates.append(coordinate)
def text(msg,x,y,color,size):
    font_object = pygame.font.SysFont('freesans',size)
    message_object = font_object.render(msg,False,color)
    screen.blit(message_object,(x,y))
while True:
    screen.fill(black)
    text('Falling Stars',250,0,white,20)
    for i in coordinates:
        pygame.draw.circle(screen,random.choice(colors),(i[0],i[1]),3)
        i[1] += 2
        if i[1] >= 600:
            i[1] = 0
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()'''

'''import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('shapes')
red = (255,0,0)
green = (0,255,0)
def text(msg,x,y,color,size):
    font_object = pygame.font.SysFont('Lobster',size)
    message_object = font_object.render(msg,False,color)
    screen.blit(message_object,(x,y))
while True:
    text('Quit',0,0,red,30)
    text('Play',555,0,green,30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()'''