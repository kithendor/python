# colliders

#Πριν την while

    game_over=False
    font = pygame.font.SysFont(None, 60)

#Μέσα στην while, πριν απο τα draw

    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_w, enemy_h) #collider για τον enemy
    
    for bullet in bullets:
        bullet_rect = pygame.Rect(bullet[0], bullet[1], bullet_w, bullet_h) #collider για κάθε σφαίρα
        if bullet_rect.colliderect(enemy_rect): #αν το collider της σφαιρας αγγίξει τον enemy
            bullets.remove(bullet)
            enemy_y = 0
            enemy_x = random.randint(0, WIDTH - enemy_w)
            break


    # TASK 1: Δημιουργήστε collider για τον player
    # TASK 2: Αν το collider του player αγγιξει τον enemy τότε game_over=True

#Μέσα στην while, μετά τα draw

    if game_over:
        text = font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(text, (WIDTH // 2 - 150, HEIGHT // 2 - 30))





# Bullet settings
    
    bullet_w = 6
    bullet_h = 12
    bullet_speed = 8
    bullet_color = (255, 255, 0)
    bullets = []
    fire_delay = 250   # milliseconds
    last_shot = 0

#...


#μέσα στη while

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

#μέασ στο draw

    for bullet in bullets:
        pygame.draw.rect(screen, bullet_color, (bullet[0], bullet[1], bullet_w, bullet_h))
