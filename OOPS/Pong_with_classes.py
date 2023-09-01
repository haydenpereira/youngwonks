import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
class Ball:
    radius = 30
    def __init__(self):
        self.x = 300
        self.y = 300
        self.speedx = 0
        self.speedy = 0
        self.color = green
    def draw(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),Ball.radius)
    #def move(self):
class Paddle:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.speedy = 3
        self.width = 20
        self.length = 125
        self.color = white
    def draw(self):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.length))
ball = Ball()
paddle1 = Paddle(30,250)
paddle2 = Paddle(550,250)
while True:
    screen.fill((0,0,0))
    ball.draw()
    paddle1.draw()
    paddle2.draw()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()