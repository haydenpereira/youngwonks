import random
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
def text(msg,x,y,color,size):
    font_object = pygame.font.SysFont('Lobster',size)
    message_object = font_object.render(msg,False,color)
    screen.blit(message_object,(x,y))
list_words = ['dog','animal','hangman','computer','window','house']
word = random.choice(list_words)
mistake = 0
blank = ['_']
word_list = list(word)
length = len(word)
underscore = blank * length
letter = ''
stop = False
def first():
    pygame.draw.line(screen,white,(50,450),(250,450),7)
def second():
    first()
    pygame.draw.line(screen,white,(150,450),(150,100),7)
def third():
    second()
    pygame.draw.line(screen,white,(150,100),(300,100),7)
def fourth():
    third()
    pygame.draw.circle(screen,white,(300,135),35)
def fifth():
    fourth()
    pygame.draw.line(screen,white,(300,170),(300,300),7)
def sixth():
    fifth()
    pygame.draw.line(screen,white,(300,210),(350,275),7)
def seventh():
    sixth()
    pygame.draw.line(screen,white,(300,210),(245,275),7)
def eighth():
    seventh()
    pygame.draw.line(screen,white,(300,300),(245,375),7)
def nineth():
    eighth()
    pygame.draw.line(screen,white,(300,300),(350,375),7)
def check():
    global mistake,stop
    if mistake == 1:
        first()
    elif mistake == 2:
        second()
    elif mistake == 3:
        third()
    elif mistake == 4:
        fourth()
    elif mistake == 5:
        fifth()
    elif mistake == 6:
        sixth()
    elif mistake == 7:
        seventh()
    elif mistake == 8:
        eighth()
    elif mistake >= 9:
        nineth()
        text('the word was ' + word,100,0,blue,50)
        pygame.time.delay(500)
        stop = True
while True:
    screen.fill((0,0,0))
    if stop == True:
        break
    if '_' not in underscore:
        text('You Won!!!',200,0,green,50)
        pygame.time.delay(1000)
        stop = True
    check()
    if letter in word:
        for i in range(0,len(word),1):
            if letter == word[i]:
                underscore[i] = letter
    text(str(underscore),100,500,white,50)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            letter = chr(event.key)
            print (word,underscore)
            print (letter)
            if letter not in word:
                mistake += 1
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()