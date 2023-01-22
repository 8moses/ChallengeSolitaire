import pygame
import random
from sys import exit
from enum import Enum

#scherm
pygame.init()
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption('Runner')
font = pygame.font.Font(None, 50)

#achtergrond
achtergrond = pygame.image.load('backgroundimagegrid.jpg')
Text = font.render('Stage', True, 'White')

#stapel met kaarten
transparantkaart1 = pygame.image.load('transparantcard.jpg')
transparantkaart1 = pygame.transform.scale('transparantcard.jpg', (100, 200))

blauwkaart = pygame.image.load('blauwkaart.jpg')
blauwkaart = pygame.transform.scale(blauwkaart, (100, 200))

width = blauwkaart.get_rect().width
height = blauwkaart.get_rect().height

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    blauwkaart = pygame.transform.scale(blauwkaart, (100, 200))
    screen.blit(achtergrond, (0, 0))    
    screen.blit(blauwkaart, (800, 50))
    screen.blit(Text,(50, 20))

    pygame.display.update()   






