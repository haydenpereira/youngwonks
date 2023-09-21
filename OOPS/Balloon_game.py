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
class Balloon:
    radius = 30
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.letter = chr(random.randint(97,122))
    def draw(self):
        pygame.draw.circle(screen,blue,(self.x,self.y),self.radius)
        text(self.letter,self.x - 10,self.y - 20,white,50)
    def move(self):
        self.y -= 0.5 
        if self.y <= 0:
            print('game over')
balloon_list = []
for i in range(0,5,1):
    object = Balloon(random.randint(0,600),600)
    balloon_list.append(object)
while True:
    screen.fill((0,0,0))
    for i in balloon_list:
        i.draw()
        i.move()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key ==  i.letter:
                    balloon_list.remove(i)
            if event.type == QUIT:
                pygame.quit()
                quit()
    pygame.display.update()