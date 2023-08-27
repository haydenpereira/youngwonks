import time
import random
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
#pong
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
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
game_start = False
game2_start = False
#snake game
food_x = (random.randint(0,600) // 20) * 20
food_y = (random.randint(0,600) // 20) * 20
snake_x = (random.randint(0,600) // 20) * 20
snake_y = (random.randint(0,600) // 20) * 20
down = False
up = False
right = False
left = False
snake_list = [(snake_x,snake_y)]
score = 0
menu1 = True
def grid():
    for i in range(20,600,20):
        pygame.draw.line(screen,white,(0,i),(600,i))
        pygame.draw.line(screen,white,(i,0),(i,600))
def text(msg,x,y,color,size):
    font_object = pygame.font.SysFont('Lobster',size)
    message_object = font_object.render(msg,False,color)
    screen.blit(message_object,(x,y))
def game2():
    global food_x,food_y,snake_x,snake_y,down,up,left,right,snake_list,score
    screen.fill((0,0,0))
    pygame.draw.rect(screen,red,(275,550,100,50),5)
    text('Quit',275,550,white,60)
    text(str(score),0,0,green,100)
    grid()
    if snake_x == food_x and snake_y == food_y:
        score += 1
        food_x = (random.randint(0,600) // 20) * 20
        food_y = (random.randint(0,600) // 20) * 20
        snake_list.append((snake_x,snake_y))
    if snake_x >= 600:
        snake_x = 0
    elif snake_x <= 0:
        snake_x = 600
    elif snake_y >= 600:
        snake_y = 0
    elif snake_y <= 0:
        snake_y = 600
    if down == True:
        snake_y += 20
    if up == True:
        snake_y -= 20
    if right == True:
        snake_x += 20
    if left == True:
        snake_x -= 20
    pygame.draw.rect(screen,red,(food_x,food_y,20,20))
    for i in snake_list:
        pygame.draw.rect(screen,green,(i[0],i[1],20,20))
    snake_list.insert(0,(snake_x,snake_y))
    snake_list.pop()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.time.delay(100)
    pygame.display.update()
def game():
    global win1,win2,score2,score1,move2,move,speed_y,speed_x,y3,x3,y2,y1,blue,green,red,white
    text(str(score1),0,0,(255,0,0),100)
    text(str(score2),560,0,(255,0,0),100)
    pygame.draw.rect(screen,red,(275,550,100,50))
    pygame.draw.rect(screen,white,(0,y2,30,200))
    pygame.draw.rect(screen,white,(570,y1,30,200))
    pygame.draw.circle(screen,blue,(x3,y3),40)
    text('Quit',275,550,white,60)
    x3 += speed_x
    y3 += speed_y
    if x3 >= 600:
        x3 = 300
        score1 += 1
        if score1 == 2:
            win2 = True
    elif x3 <= 0:
        x3 = 300
        score2 += 1
        if score2 >= 2:
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
def menu():
    global game_start,move,move2,game2_start,up,right,left,down,menu1
    while True:
        screen.fill((0,0,0))
        if game_start == True:
            menu1 = False
            game()
        elif game2_start == True:
            menu1 = False
            game2()
        elif menu1 == True:
            pygame.draw.rect(screen,green,(0,0,100,50))
            pygame.draw.rect(screen,red,(500,0,100,50))
            pygame.draw.rect(screen,green,(250,0,100,50))
            text('Game1',0,0,white,45)
            text('Game2',250,0,white,45)
            text('Quit',500,0,white,65)
        if snake_list[0] in snake_list[1:]:
            text('Game over',300,300,red,100)
            pygame.display.update()
            pygame.time.delay(500)
            break
        if win2 == True:
            text('player 2 has won',65,200,(0,255,0),80)
            pygame.display.update()
            pygame.time.delay(500)
            break
        if win1 == True:
            text('player 1 has won',65,200,(0,255,0),80)
            pygame.display.update()
            pygame.time.delay(500)
            break
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_DOWN and up != True:
                    down = True
                    right = up = left = False
                elif event.key == K_UP and down != True:
                    up = True
                    right = down = left = False
                elif event.key == K_RIGHT and left != True:
                    right = True
                    down = up = left = False
                elif event.key == K_LEFT and right != True:
                    left = True
                    right = up = down = False
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
            if event.type == MOUSEBUTTONDOWN:
                if event.pos[0] in range(0,100) and event.pos[1] in range(0,50):
                    game_start = True
                if event.pos[0] in range(250,350) and event.pos[1] in range(0,50):
                    game2_start = True
                if event.pos[0] in range(500,600) and event.pos[1] in range(0,50):
                    pygame.quit()
                    exit()
                if event.pos[0] in range(275,375) and event.pos[1] in range(550,600):
                    menu1 = True
                    game_start = game2_start = False
            if event.type == QUIT:
                pygame.quit()
                exit()
        pygame.display.update()
menu()