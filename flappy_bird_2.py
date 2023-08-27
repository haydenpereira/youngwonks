import random
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
x = 100
y = 300
y_pipe_1 = 0
y_pipe_2 = 600 
pipe_x = 0
length_1 = 250
score = 0
speed = 2
length_2 = 250
pipe_x_2 = 300
def text(msg,x,y,color,size):
    font_object = pygame.font.SysFont('Lobster',size)
    message_object = font_object.render(msg,False,color)
    screen.blit(message_object,(x,y))
while True:
    screen.fill((0,0,0))
    if pipe_x_2 <= 0:
        pipe_x_2 = 600
    text(str(score),0,0,blue,70)
    y += 1
    pipe_x -= speed
    pipe_x_2 -= speed
    if pipe_x <= 0:
        pipe_x = 600
        length_1 = random.randint(50,350)
    if x + 25 in range(pipe_x,pipe_x + 50) and (y - 25 in range(0,length_1) or y + 25 in range(length_1 + 175,600)):
        text('Game over',250,250,red,50)
        pygame.display.update()
        pygame.time.delay(100)
        break
    elif x + 25 in range(pipe_x_2,pipe_x_2 + 50) and (y - 25 in range(0,length_2) or y + 25 in range(length_2 + 175,600)):
        text('Game over',250,250,red,50)
        pygame.display.update()
        pygame.time.delay(100)
        break
    elif y + 25 >= 600 or y - 25 <= 0:
        text('Game over',250,250,red,50)
        pygame.display.update()
        pygame.time.delay(100)
        break
    pygame.draw.circle(screen,yellow,(x,y),25)
    pygame.draw.rect(screen,green,(pipe_x,0,50,length_1))
    pygame.draw.rect(screen,green,(pipe_x,length_1 + 175,50,600 - (length_1 + 175)))
    pygame.draw.rect(screen,green,(pipe_x_2,0,50,length_2))
    pygame.draw.rect(screen,green,(pipe_x_2,length_2 + 175,50,600 - length_2 + 175))
    if pipe_x == 100 or pipe_x_2 == 100:
        score += 1
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                y -= 45
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.time.delay(10)
    pygame.display.update()