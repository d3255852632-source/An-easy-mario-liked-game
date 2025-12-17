import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Leaning to draw graphics")

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
SKY_BLUE = (135,206,235)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(SKY_BLUE)
    pygame.draw.rect(screen, GREEN, (0, 500, 800, 100))
    pygame.draw.rect(screen, RED, (100, 440, 40, 60))
    pygame.draw.circle(screen, YELLOW, (700, 80), 50)
    for i in range(0, 800, 20):
        pygame.draw.line(screen, (0,150,0), (i, 500), (i, 490), 2)
    
    pygame.display.flip()
pygame.quit()
sys.exit()