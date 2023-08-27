import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
bg = pygame.image.load('BG 2.png')
tile = pygame.image.load('2.png')
tile = pygame.transform.scale(tile,(60,60))
dino = pygame.image.load('idle1.png')
dino = pygame.transform.scale(dino,(100,110))
coin = pygame.image.load('Coins-Transparent-PNG.png')
coin = pygame.transform.scale(coin,(50,50))
door = pygame.image.load('door4.png')
door = pygame.transform.scale(door,(100,160))
def text(msg,x,y,color,size):
    font_object = pygame.font.SysFont('Lobster',size)
    message_object = font_object.render(msg,False,color)
    screen.blit(message_object,(x,y))
layer1 = [[0,0,2,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,2,0,0,0],
          [1,1,1,1,1,1,0,0,2,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,2,0,0,0,2,0,0,2,0],
          [0,0,0,2,0,0,0,0,0,0],
          [1,1,1,1,0,0,0,1,1,1],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0]]
x = 0
y = 0
jump = None
right = None
left = None
x_dino = 0
y_dino = 0
gravity = True
tile_list = []
coin_list = []
win = True
while True:
    screen.blit(bg,(0,0))
    gravity = True
    dinosaur = screen.blit(dino,(x_dino,y_dino))
    for i in layer1:
        for pos in range(0,len(i),1):
            if i[pos] == 1:
                block = screen.blit(tile,(x,y))
                tile_list.append(block)
            if i[pos] == 2:
                win = False
                point = screen.blit(coin,(x,y))
                if dinosaur.colliderect(point):
                    i[pos] = 0
            x += 60
        y += 60
        x = 0
    y = 0
    x = 0
    if win == True:
        screen.blit(door,(500,205))
        if x_dino in range(500,600) and y_dino in range(205,365):
            screen.fill((0,0,0))
            text('level 1 completed',0,250,(0,255,0),100)
    win = True
    for i in tile_list:
        if dinosaur.colliderect(i):
            if dinosaur.bottom - 2 == i.top:
                gravity = False 
    if left == True:
        x_dino -= 3
    if right == True:
        x_dino += 3
    if gravity == True:
        y_dino += 2
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                left = True
            if event.key == K_RIGHT:
                right = True
            if event.key == K_SPACE and gravity == False:
                y_dino -= 110
        if event.type == KEYUP:
            if event.key == K_LEFT:
                left = False
            if event.key == K_RIGHT:
                right = False
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()