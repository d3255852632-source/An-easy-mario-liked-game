import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Leaning Keyboard Control")

SKY_BLUE = (135, 206, 235)
GREEN = (0,128,0)
RED = (255,0,0)

player_x = 100
player_y = 440
player_speed = 5

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_r:
                player_x = 100
                player_y = 440
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    
    if keys[pygame.K_UP]:
        player_y -= player_speed
    
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    if player_x < 0:
        player_x = 0
    if player_x > 760:
        player_x = 760
    if player_y < 0:
        player_y = 0
    if player_y > 540:
        player_y = 540
    screen.fill((SKY_BLUE))
    screen.fill(SKY_BLUE)
    pygame.draw.rect(screen, GREEN, (0, 500, 800, 100))
    pygame.draw.rect(screen, RED, (player_x, player_y, 40, 60))
    font = pygame.font.Font(None, 36)
    text = font.render("Use the arow keys to move,R to reset, ESC to quit", True, (255, 255, 255))
    screen.blit(text, (10,10))
    pygame.display.flip()
pygame.quit()
sys.exit()