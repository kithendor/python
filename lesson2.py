import pygame
import sys

pygame.init()

# Window settings
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

clock = pygame.time.Clock()
FPS = 60

background_color = 15, 15, 30

# Player settings
player_w = 60
player_h = 20
player_x = WIDTH // 2 - player_w // 2
player_y = HEIGHT - 60
player_speed = 6
player_color = 80, 200, 255

# Enemy settings
enemy_w = 40
enemy_h = 40
enemy_x = WIDTH // 2 - enemy_w // 2
enemy_y = 0
enemy_speed = 3
enemy_color = 255, 80, 80 

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # LEVEL 1: Κίνηση αριστερά
    # if keys[pygame.K_LEFT]:
    #     ...
    
    # LEVEL 2: Κίνηση δεξιά
    # if keys[pygame.K_RIGHT]:
    #     ...

    # LEVEL 3: Να μην βγαίνει εκτός οθόνης
    # Πχ να πηγαίνει αριστερά μόνο αν η θέση x του Player είναι μεγαλύτερη απο 0

    # LEVEL 4: Ο enemy να πέφτει προς τα κάτω (να αλλάζει το y)

    # LEVEL 5: Αν φτάσει κάτω, να ξεκινάει πάλι από πάνω 


    # Draw
    screen.fill(background_color)

    # Player
    pygame.draw.rect(screen, player_color,(player_x, player_y, player_w, player_h))

    # Enemy
    pygame.draw.rect(screen, enemy_color,(enemy_x, enemy_y, enemy_w, enemy_h))

    pygame.display.flip()

pygame.quit()
sys.exit()
