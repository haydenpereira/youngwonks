import time
import random
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
food_x = (random.randint(0,600) // 20) * 20
food_y = (random.randint(0,600) // 20) * 20
snake_x = (random.randint(0,600) // 20) * 20
snake_y = (random.randint(0,600) // 20) * 20
def text(msg,x,y,color,size):
    font_object = pygame.font.SysFont('Lobster',size)
    message_object = font_object.render(msg,False,color)
    screen.blit(message_object,(x,y))
def grid():
    for i in range(20,600,20):
        pygame.draw.line(screen,white,(0,i),(600,i))
        pygame.draw.line(screen,white,(i,0),(i,600))
down = False
up = False
right = False
left = False
snake_list = [(snake_x,snake_y)]
score = 0
while True:
    screen.fill((0,0,0))
    text(str(score),0,0,green,100)
    if snake_list[0] in snake_list[1:]:
        text('Game over',300,300,red,100)
        pygame.time.delay(200)
        break
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
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.time.delay(100)
    pygame.display.update()