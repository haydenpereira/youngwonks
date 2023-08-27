import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
x = 0
y = 300
move = None
jump_images = []
jump_index_position = 0
for i in range(1,13,1):
    jump = pygame.image.load('Jump' + str(i) + '.png')
    jump = pygame.transform.scale(jump,(140,100))
    jump_images.append(jump)
while True:
    screen.fill((0,0,0))
    screen.blit(jump_images[jump_index_position],(x,y))
    if move == 'jump':
        if jump_index_position == 11:
            jumping = False
        if jump_index_position == 0:
            jumping = True
        if jumping == True:
            y -= 10
            jump_index_position += 1
        else:
            y += 110
            jump_index_position = 0
            move = None
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                move = 'jump'
        
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.time.delay(50)
    pygame.display.update()