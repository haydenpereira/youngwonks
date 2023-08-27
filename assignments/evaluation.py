import random
import time
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
motion = False
x = 300
y = 300
circle = 0
circles = {}
while True:
    screen.fill((0,0,0))
    pygame.draw.circle(screen,blue,(x,y),40)
    for i in circles:
        pygame.draw.circle(screen,circles[i],i,20)
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.pos[0] in range(x - 40,x + 40) and event.pos[1] in range(y - 40,y + 40):
                motion = True
        if motion == True:
            x = event.pos[0]
            y = event.pos[1]
            if x >= 500 or x <= 100 or y >= 500 or y <= 100:
                circles[(random.randint(0,600),random.randint(0,600))] = green
                time.sleep(.5)
        if event.type == MOUSEBUTTONUP:
            motion = False
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()