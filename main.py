import pygame
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





