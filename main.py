import pygame
import random
from sys import exit
# achtergrond
pygame.init()
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption('Runner')

img = pygame.image.load('backgroundimagegrid.jpg')


while True:
    screen.blit(img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

          
    pygame.display.update()    
    #kaarten
    CARDWIDTH = 100
    CARDHEIGHT = 150
    MARGIN = 10
    XSPACING = CARDWIDTH + 2*MARGIN
    YSPACING = CARDHEIGHT + 4*MARGIN
    OFFSET = 5


    HARTEN = 'hart'
    DIAMANTEN = 'diamant'
    CLUBS = 'club'
    SPADES = 'spade'

    RED = 'red'
    BLACK = 'black'
    COLOR = {}

    for s in (HARTEN, DIAMANTEN):
     COLOR [s] = RED
    for s in (CLUBS, SPADES):
     COLOR[s] = BLACK

    ALLSUITS = COLOR.keys()
    NSUITS = len(ALLSUITS)
    ACE = 1
    JACK = 11
    QUEEN = 12
    KING = 13
    ALLVALUES = range(1, 14) # (one more than the highest value)
    NVALUES = len(ALLVALUES)
    ALNAMES = ["", "A"] + map(str, range(2, 11)) + ["J", "Q", "K"]
    



