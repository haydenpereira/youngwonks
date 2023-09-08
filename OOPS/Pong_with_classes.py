import time
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
move1 = None
move2 = None
def text(msg,x,y,color,size):
    font_object = pygame.font.SysFont('Lobster',size)
    message_object = font_object.render(msg,False,color)
    screen.blit(message_object,(x,y))
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
    def move(self):
        self.x += self.speedx
        self.y += self.speedy
        if self.y >= 570 or self.y <= 30:
            self.speedy = -self.speedy
class Paddle:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.speedy = 3
        self.width = 20
        self.length = 125
        self.color = white
        self.score = 0
    def draw(self):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.length))
ball = Ball()
paddle1 = Paddle(30,250)
paddle2 = Paddle(550,250)
ball.speedx = ball.speedy = 2
while True:
    screen.fill((0,0,0))
    ball.draw()
    paddle1.draw()
    paddle2.draw()
    text(str(paddle1.score),0,0,white,80)
    text(str(paddle2.score),570,0,white,80)
    if ball.x >= 570:
        paddle1.score += 1
        ball.x = 300
        ball.y = 300
        
    elif ball.x <= 30:
        paddle2.score += 1
        ball.x = 300
        ball.y = 300
        
    if move1 == 'up':
        paddle1.y -= paddle1.speedy
    elif move1 == 'down':
        paddle1.y += paddle1.speedy
    if paddle1.y >= 475:
        paddle1.y = 474
    elif paddle1.y <= 0:
        paddle1.y = 1
    if move2 == 'up':
        paddle2.y -= paddle2.speedy
    elif move2 == 'down':
        paddle2.y += paddle2.speedy
    if paddle2.y >= 475:
        paddle2.y = 474
    elif paddle2.y <= 0:
        paddle2.y = 1
    ball.move()
    if (ball.x - 30 in range(paddle1.x,paddle1.x + 20) and ball.y in range(paddle1.y,paddle1.y + 125)) or (ball.x + 30 in range(paddle2.x,paddle2.x + 20) and ball.y in range(paddle2.y,paddle2.y + 125)):
        ball.speedx = -ball.speedx
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_w:
                move1 = 'up'
            elif event.key == K_s:
                move1 = 'down'
            if event.key == K_UP:
                move2 = 'up'
            elif event.key == K_DOWN:
                move2 = 'down'
        if event.type == KEYUP:
            move1 = move2 = None
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()