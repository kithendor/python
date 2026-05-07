# Grapgics

https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize?client_id=c9a559d2-7aab-4f13-a6ed-e7e9c52aec87&redirect_uri=https%3a%2f%2fforms.cloud.microsoft%2flanding&state=eyJ2ZXJzaW9uIjoxLCJkYXRhIjp7IklkZW50aXR5UHJvdmlkZXIiOiJBWENOMi1SRmxvLUk0OTZCa3MxMkZSeDlaZHFKS2FOdENYTjZMS19sVWFaYUpTb0Zjb1A4VXh5VjdKNXkxazcza2d5QVd0UTVBRmxETDg1bFZqMmRtbGMiLCIucmVkaXJlY3QiOiJodHRwczovL2Zvcm1zLmNsb3VkLm1pY3Jvc29mdC9wYWdlcy9yZXNwb25zZXBhZ2UuYXNweD9pZD1JQ21zTk1EaEgwV3lILXFHTFQ5X2ZpNW9sd212aGlKRXFWZlBBVjJab294VVFWVTNRVll5VEVWRVdVNVdNVEU0TmxwQldWcFpSamM1U1M0dSZyb3V0ZT1zaG9ydHVybCZzaWQ9NjZiMWRiN2QtZjkyNi00OTIwLTlkN2EtNjk2MzdjMzE1ZjQyIiwiLnhzcmYiOiJBYkRHbFN4ekt6MHNURjVidURnX2tweXlBaWZ6WUxRdVA1eGhOSEtudWxOTXg2TkdTck1VNGphMnp3TXdZcGJnWjBYczJnWkdRNmszRTdVNkFiQ2hPbktJanhKVnMtRDFReU1iVXFjcmpVRHMwZWRiY2lUbFpyZmZJYXk4Z0hMbUJRIiwiT3BlbklkQ29ubmVjdC5Db2RlLlJlZGlyZWN0VXJpIjoiQWZ6YlNoT0F2OGF6X3lHTGJCTnpnemRqenRMNUVDQWlia01ZSTg4UnEyZkEwU1pKZXJPdll6M1ZkRFNDR19JNWNFQnhndmZGYzdrbG45b3ZhNXpNNUZfQkpBNG5lVXcydTVBUGZ3azVXakVaaHhJODkzamZRc0xOVnA2dzY0eTliZyJ9fQ&response_type=code&scope=openid+profile&response_mode=form_post&nonce=639137338671059715.NTQ5Nzc4ZTUtZjE2MS00MWRmLWJhNmQtZmZjN2QwYWQ0MjJhZDM4YzBhZjQtNWU4ZS00NmRmLWFjNzctOGE3MzFlYzUwODZj&msafed=0&x-client-SKU=ID_NET10_0&x-client-ver=8.15.0.0&sso_nonce=AwABEgEAAAADAOz_BQD0_0V2b1N0c0FydGlmYWN0cwUAAAAAAOxbpeDeQqs5DtSfI-h7_I8wGiflbaege7JNiKp1bRKMovPepVL17z9STlgafZEzKiL3vOJ-JY_uTdFG7L9CQwsgAA&client-request-id=a2d7ce7c-2728-439f-878d-72e5186cbedd&mscrid=a2d7ce7c-2728-439f-878d-72e5186cbedd

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
