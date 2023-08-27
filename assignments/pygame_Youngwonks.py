import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
white = (255,255,255)
while True:
    '''for i in range(0,700,6):
        pygame.draw.line(screen,white,(i,0),(i,600),1)
        pygame.draw.line(screen,white,(0,i),(600,i),1)'''
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()