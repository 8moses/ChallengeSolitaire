import pygame
import random
from sys import exit
from enum import Enum

#scherm
pygame.init()
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption('Runner')
font = pygame.font.Font(None, 40)

#achtergrond
achtergrond = pygame.image.load('backgroundimagegrid.jpg')

#Text voor Stages, Timer Moves enzo
stagetext = font.render('Stage:', True, 'White')
timertext = font.render('Timer:', True, 'White')
movestext = font.render('Moves:', True, 'White')


# 4 Transparante kaarten + Die blauwe kaart stapel rechts
transparantkaart = pygame.image.load('transparantcard.png')
transparantkaart = pygame.transform.scale(transparantkaart,(130, 200))

transparantkaart2 = pygame.image.load('transparantcard.png')
transparantkaart2 = pygame.transform.scale(transparantkaart2,(130, 200))

transparantkaart3 = pygame.image.load('transparantcard.png')
transparantkaart3 = pygame.transform.scale(transparantkaart3,(130, 200))

transparantkaart4 = pygame.image.load('transparantcard.png')
transparantkaart4 = pygame.transform.scale(transparantkaart3,(130, 200))

blauwkaart = pygame.image.load('blauwkaart.jpg')
blauwkaart = pygame.transform.scale(blauwkaart, (130, 200))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(achtergrond, (0, 0))
    screen.blit(transparantkaart, (20, 60))  
    screen.blit(transparantkaart2, (200, 60)) 
    screen.blit(transparantkaart3, (380, 60)) 
    screen.blit(transparantkaart4, (560, 60)) 
    screen.blit(blauwkaart, (860, 60))
    screen.blit(stagetext,(50, 15))
    screen.blit(timertext,(250, 15))
    screen.blit(movestext,(450, 15))

    pygame.display.update()   






