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
