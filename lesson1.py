import pygame
import sys

pygame.init()

WIDTH,HEIGHT = 800,500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MY GAME")

clock = pygame.time.Clock()
FPS = 60
background_color = (150,5,3)

#player
player_w=60
player_h = 20
player_x = WIDTH//2 - player_w//2
player_y = HEIGHT - 60
player_color = (10,10,10)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Draw
    screen.fill(background_color)
    pygame.draw.rect(screen,player_color,(player_x,player_y,player_w,player_h))


    pygame.display.flip()


pygame.quit()
sys.exit()

