import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Learning game clock")

SKY_BLUE = (135, 206, 235)
GREEN = (0, 128, 0)
RED = (255, 0, 0)

player_x = 100
player_y = 440
player_speed = 5

clock = pygame.time.Clock()
FPS = 60
running = True
frame_count = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
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
    
    screen.fill(SKY_BLUE)
    pygame.draw.rect(screen, GREEN, (0, 500, 800, 100))
    pygame.draw.rect(screen, RED, (player_x, player_y, 40, 60))

    frame_count += 1

    actual_fps = clock.get_fps()
    font = pygame.font.Font(None, 36)
    frame_text = font.render(f"Frames: {frame_count}", True, (255,255,255))
    screen.blit(frame_text, (10,10))
    fps_text = font.render(f"FPS:{actual_fps:.1f}", True, (255,255,255))
    screen.blit(fps_text, (10,50))
    pos_text = font.render(f"Charector Position:{player_x}, {player_y}", True, (255,255,255))
    screen.blit(pos_text, (10,90))
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
sys.exit()