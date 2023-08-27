import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
white = (255,255,255)
yellow = (255,255,0)
animation = []
run = []
run_left = []
count = 0
x = 200
y = 300
move = None
for i in range(1,11,1):
    image = pygame.image.load('idle1.png')
    image = pygame.transform.scale(image,(125,135))
    animation.append(image)
for i in range(1,8,1):
    image = pygame.image.load('Walk' + str(i) + '.png')
    image = pygame.transform.scale(image,(125,135))
    run.append(image)
for i in range(1,8,1):
    image = pygame.image.load('Walk' + str(i) + '.png')
    image = pygame.transform.scale(image,(125,135))
    image = pygame.transform.flip(image,True,False)
    run_left.append(image)
while True:
    screen.fill((0,0,0))
    if move == 'right':
        x += 2
        if x >= 600:
            x = 1
        screen.blit(run[count],(x,y))
        count += 1
        if count == len(run):
            count = 0
    elif move == 'left':
        x -= 2
        if x <= 0:
            x = 600
        screen.blit(run_left[count],(x,y))
        count += 1
        if count == len(run_left):
            count = 0
    elif move == 'up':
        y -= 2
    elif move == 'down':
        y += 2
    else:
        screen.blit(animation[0],(x,y))
    for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    move = 'right'
                if event.key == K_LEFT:
                    move = 'left'
                if event.key == K_UP:
                    move = 'up'
                if event.key == K_DOWN:
                    move = 'down'
            if event.type == KEYUP:
                move = None
            if event.type == QUIT:
                pygame.quit()
                exit()
    
                pygame.display.update()

'''import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
white = (255,255,255)
x = 300
y = 300
click = None
def text(msg,x,y,color):
    font = pygame.font.SysFont('freesans',32)
    message = font.render(msg,False,color)
    screen.blit(message,(x,y))
while True:
    screen.fill((0,0,0))
    text('hello',200,0,(255,255,0))
    if click == True:
        x = event.pos[0]
        y = event.pos[1]
    pygame.draw.circle(screen,white,(x,y),50)
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.pos[0] in range(250,350) and event.pos[1] in range(250,350):
                click = True
        if event.type == MOUSEBUTTONUP:
            click = False
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()'''