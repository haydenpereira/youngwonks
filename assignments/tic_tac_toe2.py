import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
turn = 0
a = -3000
b = -3000
game_over = False
def text(msg,x,y,color,size):
    font_object = pygame.font.SysFont('Lobster',size)
    message_object = font_object.render(msg,False,color)
    screen.blit(message_object,(x,y))
tic_tac_toe = {1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}
def win():
    global game_over
    if tic_tac_toe[1] == tic_tac_toe[2] == tic_tac_toe[3]:
        if tic_tac_toe[1] != '':
            text(tic_tac_toe[1] + ' Wins!',300,300,green,70)
            game_over = True
    elif tic_tac_toe[4] == tic_tac_toe[5] == tic_tac_toe[6] != '':
        text(tic_tac_toe[4] + ' Wins!',300,300,green,70)
        game_over = True
    elif tic_tac_toe[7] == tic_tac_toe[8] == tic_tac_toe[9] != '':
        text(tic_tac_toe[7] + ' Wins!',300,300,green,70)
        game_over = True
        pygame.display.update()
        pygame.time.delay(100)
    elif tic_tac_toe[1] == tic_tac_toe[4] == tic_tac_toe[7] != '':
        text(tic_tac_toe[1] + ' Wins!',300,300,green,70)
        game_over = True
    elif tic_tac_toe[1] == tic_tac_toe[4] == tic_tac_toe[7] != '':
        text(tic_tac_toe[1] + ' Wins!',300,300,green,70)
        game_over = True
    elif tic_tac_toe[2] == tic_tac_toe[5] == tic_tac_toe[8] != '':
        text(tic_tac_toe[2] + ' Wins!',300,300,green,70)
        game_over = True
    elif tic_tac_toe[3] == tic_tac_toe[6] == tic_tac_toe[9] != '':
        text(tic_tac_toe[3] + ' Wins!',300,300,green,70)
        game_over = True
    elif tic_tac_toe[1] == tic_tac_toe[5] == tic_tac_toe[9] != '':
        text(tic_tac_toe[1] + ' Wins!',300,300,green,70)
        game_over = True
    elif tic_tac_toe[3] == tic_tac_toe[5] == tic_tac_toe[7] != '':
        text(tic_tac_toe[3] + ' Wins!',300,300,green,70)
        game_over = True
def draw_x(x,y):
    pygame.draw.line(screen,red,(x,y),(x + 200,y + 200),7)
    pygame.draw.line(screen,red,(x + 200,y),(x,y + 200),7)
def draw_o(x,y):
    pygame.draw.circle(screen,green,(x,y),80,7)
while True:
    if tic_tac_toe[1] and tic_tac_toe[2] and tic_tac_toe[3] and tic_tac_toe[4] and tic_tac_toe[5] and tic_tac_toe[6] and tic_tac_toe[7] and tic_tac_toe[8] and tic_tac_toe[9] != '':
        text('Tie',300,300,red,70)
        game_over = True
    if game_over == True:
        break
    win()
    for i in range(200,600,200):
        pygame.draw.line(screen,(255,255,255),(i,0),(i,600),7)
        pygame.draw.line(screen,(255,255,255),(0,i),(600,i),7)
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            a = event.pos[0]
            b = event.pos[1]
        if event.type == QUIT:
            pygame.quit()
            quit()
        if a in range(0,200) and b in range(0,200) and tic_tac_toe[1] == '':
            if turn % 2 == 0:
                draw_x(0,0)
                tic_tac_toe[1] = 'x'
            else:
                draw_o(100,100)
                tic_tac_toe[1] = 'o'
            turn += 1
        elif a in range(200,400) and b in range(0,200) and tic_tac_toe[2] == '':
            if turn % 2 == 0:
                draw_x(200,0)
                tic_tac_toe[2] = 'x'
            else:
                draw_o(300,100)
                tic_tac_toe[2] = 'o'
            turn += 1
        elif a in range(400,600) and b in range(0,200) and tic_tac_toe[3] == '':
            if turn % 2 == 0:
                draw_x(400,0)
                tic_tac_toe[3] = 'x'
            else:
                draw_o(500,100)
                tic_tac_toe[3] = 'o'
            turn += 1
        elif a in range(0,200) and b in range(200,400) and tic_tac_toe[4] == '':
            if turn % 2 == 0:
                draw_x(0,200)
                tic_tac_toe[4] = 'x'
            else:
                draw_o(100,300)
                tic_tac_toe[4] = 'o'
            turn += 1
        elif a in range(200,400) and b in range(200,400) and tic_tac_toe[5] == '':
            if turn % 2 == 0:
                draw_x(200,200)
                tic_tac_toe[5] = 'x'
            else:
                draw_o(300,300)
                tic_tac_toe[5] = 'o'
            turn += 1
        elif a in range(400,600) and b in range(200,400) and tic_tac_toe[6] == '':
            if turn % 2 == 0:
                draw_x(400,200)
                tic_tac_toe[6] = 'x'
            else:
                draw_o(500,300)
                tic_tac_toe[6] = 'o'
            turn += 1
        elif a in range(0,200) and b in range(400,600) and tic_tac_toe[7] == '':
            if turn % 2 == 0:
                draw_x(0,400)
                tic_tac_toe[7] = 'x'
            else:
                draw_o(100,500)
                tic_tac_toe[7] = 'o'
            turn += 1
        elif a in range(200,400) and b in range(400,600) and tic_tac_toe[8] == '':
            if turn % 2 == 0:
                draw_x(200,400)
                tic_tac_toe[8] = 'x'
            else:
                draw_o(300,500)
                tic_tac_toe[8] = 'o'
            turn += 1
        elif a in range(400,600) and b in range(400,600) and tic_tac_toe[9] == '':
            if turn % 2 == 0:
                draw_x(400,400)
                tic_tac_toe[9] = 'x'
            else:
                draw_o(500,500)
                tic_tac_toe[9] = 'o'
            turn += 1
    pygame.display.update()