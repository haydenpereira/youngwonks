import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
white = (255,255,255)
blue = (0,0,255)
y1 = 150
y2 = 150
x3 = 300
y3 = 300
speed_x = 2
speed_y = 2
move = None
move2 = None
score1 = 0
score2 = 0
win2 = False
win1 = False
def text(msg,x,y,color,size):
    font_object = pygame.font.SysFont('Lobster',size)
    message_object = font_object.render(msg,False,color)
    screen.blit(message_object,(x,y))
while True:
    screen.fill((0,0,0))
    text(str(score1),0,0,(255,0,0),100)
    text(str(score2),560,0,(255,0,0),100)
    if win2 == True:
        text('player 2 has won',65,200,(0,255,0),80)
        pygame.time.delay(2000)
        break
    if win1 == True:
        text('player 1 has won',65,200,(0,255,0),80)
        pygame.time.delay(2000)
        break
    pygame.draw.rect(screen,(255,0,0),(300,525,100,50))
    pygame.draw.rect(screen,white,(0,y2,30,200))
    pygame.draw.rect(screen,white,(570,y1,30,200))
    pygame.draw.circle(screen,blue,(x3,y3),40)
    x3 += speed_x
    y3 += speed_y
    if x3 >= 600:
        x3 = 300
        score1 += 1
        if score1 == 5:
            win2 = True
    elif x3 <= 0:
        x3 = 300
        score2 += 1
        if score2 >= 5:
            win1 = True
    if x3 + 30 in range(570,600) and y3 in range(y1,y1 + 200):
        speed_x = -speed_x
    elif x3 - 30 in range(0,30) and y3 in range(y2,y2 + 200):
        speed_x = -speed_x
    if y3 + 30 >= 600: 
        speed_y = -speed_y
    elif y3 - 30 <= 0:
        speed_y = -speed_y
    if move == True:
        y1 -= 3
        if y1 <= 0:
            move = None
    elif move == False:
        y1 += 3
        if y1 >= 400:
            move = None
    if move2 == True:
        y2 -= 3
        if y2  <= 0:
            move2 = None
    elif move2 == False:
        y2 += 3
        if y2 >= 400:
            move2 = None
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                move = True
            elif event.key == K_w:
                move2 = True
            if event.key == K_DOWN:
                move = False
            elif event.key == K_s:
                move2 = False
        if event.type == KEYUP:
            if event.key == K_UP or event.key == K_DOWN:
                move = None
            if event.key == K_w or event.key == K_s:
                move2 = None
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()