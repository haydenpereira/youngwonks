import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
walk_index_position = 0
idle_index_position = 0
run_index_position = 0
dead_index_position = 0
walk1_index_position = 0
jump_index_position = 0
x = 0
y = 300
jumping = None
move = None
walk_images = []
walk_images1 = []
idle_images = []
run_images = []
dead_images = []
jump_images = []
clock = pygame.time.Clock()
for i in range(1,11,1):
    walk1 = pygame.image.load('Walk' + str(i) + '.png')
    walk1 = pygame.transform.scale(walk1,(140,100))
    walk_images.append(walk1)
for i in range(1,11,1):
    idle1 = pygame.image.load('Idle' + str(i) + '.png')
    idle1 = pygame.transform.scale(idle1,(140,100))
    idle_images.append(idle1) 
for i in range(1,9,1):
    run1 = pygame.image.load('Run' + str(i) + '.png')
    run1 = pygame.transform.scale(run1,(140,100))
    run_images.append(run1)
for i in range(1,9,1):
    dead1 = pygame.image.load('Dead' + str(i) + '.png')
    dead1 = pygame.transform.scale(dead1,(140,100))
    dead_images.append(dead1)
for i in range(1,11,1):
    walk1 = pygame.image.load('Walk' + str(i) + '.png')
    walk1 = pygame.transform.scale(walk1,(140,100))
    walk1 = pygame.transform.flip(walk1,True,False)
    walk_images1.append(walk1)
for i in range(1,13,1):
    jump = pygame.image.load('Jump' + str(i) + '.png')
    jump = pygame.transform.scale(jump,(140,100))
    jump_images.append(jump)
while True:
    screen.fill((0,0,0))
    clock.tick(15)
    if move == 'walk right':
        screen.blit(walk_images[walk_index_position],(x,y))
        walk_index_position += 1
        if walk_index_position >= 10:
            walk_index_position = 0
        x += 3
        if x >= 600:
            x = -100
    if move == 'idle':
        screen.blit(idle_images[idle_index_position],(x,y))
        idle_index_position += 1
        if idle_index_position >= 10:
            idle_index_position = 0
    if move == 'run':
        screen.blit(run_images[run_index_position],(x,y))
        run_index_position += 1
        if run_index_position >= 8:
            run_index_position = 0
        x += 10
        if x >= 600:
            x = -100
    if move == 'dead':
        screen.blit(dead_images[dead_index_position],(x,y))
        dead_index_position += 1
        if dead_index_position >= 8:
            dead_index_position = 0
    if move == 'walk left':
        screen.blit(walk_images1[walk1_index_position],(x,y))
        walk1_index_position += 1
        if walk1_index_position >= 10:
            walk1_index_position = 0
        x -= 3
        if x <= -100:
            x = 600   
    if move == 'jump':
        screen.blit(jump_images[jump_index_position],(x,y))
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
            move = 'idle'
    else:
        pass
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                move = 'walk right'
            elif event.key == K_LEFT:
                move = 'walk left'
            elif chr(event.key) == 'z':
                move = 'run'
            elif chr(event.key) == 'd':
                move = 'dead'
            elif event.key == K_SPACE:
                move = 'jump'
        if event.type == KEYUP:
            move = 'idle'
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()