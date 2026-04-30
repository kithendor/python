# Grapgics

https://forms.cloud.microsoft/Pages/ResponsePage.aspx?id=ICmsNMDhH0WyH-qGLT9_ftH-xMjQzD1ImH-W-ASIuBZUQTY1S0JMTTBaNUlDUEdNTFJMQ0wzN05LTi4u

    import pygame
    import sys
    import random
    
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
    
    # Bullet settings
    bullet_w = 6
    bullet_h = 12
    bullet_speed = 8
    bullet_color = (255, 255, 0)
    bullets = []
    fire_delay = 250   # milliseconds
    last_shot = 0
    
    game_over=False
    font = pygame.font.SysFont(None, 60)
    
    running = True
    while running:
        clock.tick(FPS)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        keys = pygame.key.get_pressed()
    
        if keys[pygame.K_LEFT]:
            if player_x>0:
                player_x-=player_speed
    
    
        if keys[pygame.K_RIGHT]:
            if player_x<WIDTH-player_w:
                player_x+=player_speed
    
        if keys[pygame.K_SPACE]:
            now = pygame.time.get_ticks()
    
            if now - last_shot >= fire_delay:
                bullet_x = player_x + player_w // 2 - bullet_w // 2
                bullet_y = player_y
                bullets.append([bullet_x, bullet_y])
                last_shot = now
    
        
        for bullet in bullets:
            bullet[1] -= bullet_speed
    
    
        for bullet in bullets:
            if bullet[1] < 0:
                bullets.remove(bullet)
    
        
        enemy_y+=enemy_speed
        if enemy_y > HEIGHT:
            enemy_y = 0
            enemy_x = random.randint(0, WIDTH - enemy_w)
    
        
        enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_w, enemy_h)
        for bullet in bullets:
            bullet_rect = pygame.Rect(bullet[0], bullet[1], bullet_w, bullet_h)
            if bullet_rect.colliderect(enemy_rect):
                bullets.remove(bullet)
                enemy_y = 0
                enemy_x = random.randint(0, WIDTH - enemy_w)
                break
    
    
        player_rect = pygame.Rect(player_x, player_y, player_w, player_h)
    
        if player_rect.colliderect(enemy_rect):
                game_over = True
    
    
    
        # Draw
        screen.fill(background_color)
    
        # Player
        pygame.draw.rect(screen, player_color,(player_x, player_y, player_w, player_h))
    
        # Enemy
        pygame.draw.rect(screen, enemy_color,(enemy_x, enemy_y, enemy_w, enemy_h))
        for bullet in bullets:
            pygame.draw.rect(screen, bullet_color, (bullet[0], bullet[1], bullet_w, bullet_h))
    
    
        if game_over:
            text = font.render("GAME OVER", True, (255, 255, 255))
            screen.blit(text, (WIDTH // 2 - 150, HEIGHT // 2 - 30))
    
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()
