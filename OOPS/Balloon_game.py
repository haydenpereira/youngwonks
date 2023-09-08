import random
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
class Balloon:
    radius = 30
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.letter = chr(random.randint(97,122))
    def draw(self):
        pygame.draw.circle(screen,blue,(self.x,self.y),self.radius)
balloon_list = []
for i in range(0,5,1):
    Balloon(random.randint(0,600),600)
    
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()