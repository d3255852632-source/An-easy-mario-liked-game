import pygame
import sys
pygame.init()

SCREEN_LENGTH = 800
SCREEN_WIDTH = 600
screen = pygame.display.set_mode((SCREEN_LENGTH, SCREEN_WIDTH))

pygame.display.set_caption("My First Game")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((135, 206, 235))
    pygame.display.flip()
pygame.quit()
sys.exit()
