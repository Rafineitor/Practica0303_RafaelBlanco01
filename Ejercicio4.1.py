#HaxBall

import pygame  

pygame.init()  

ventana = pygame.display.set_mode((720, 640))  
pygame.display.set_caption("HaxBall")  

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
speedball = [3, 3]

ballrect.move_ip((ventana.get_width()-(ball.get_width()))/2, (ventana.get_height()-(ball.get_width()))/2)

player1 = pygame.image.load("player1.png")
player1rect = player1.get_rect()
player1rect.move_ip(450, 300)

player2 = pygame.image.load("player2.png")
player2rect = player2.get_rect()
player2rect.move_ip(150, 300)

ballrect.center = (ventana.get_width() // 2, ventana.get_height() // 2)

clock = pygame.time.Clock()

# Bucle principal del juego
jugando = True  
while jugando:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            jugando = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player1rect.move_ip(-5, 0)
    if keys[pygame.K_RIGHT]:
        player1rect.move_ip(5, 0)
    if keys[pygame.K_UP]:
        player1rect.move_ip(0,-5)
    if keys[pygame.K_DOWN]:
        player1rect.move_ip(0,5)

    if keys[pygame.K_a]:
        player2rect.move_ip(-5, 0)
    if keys[pygame.K_d]:
        player2rect.move_ip(5, 0)
    if keys[pygame.K_w]:
        player2rect.move_ip(0,-5)
    if keys[pygame.K_s]:
        player2rect.move_ip(0,5)

    player1rect.clamp_ip(ventana.get_rect())
    player2rect.clamp_ip(ventana.get_rect())

    if ballrect.colliderect(player1rect):
        speedball[0] = -speedball[0]
        speedball[1] = -speedball[1]

    if ballrect.colliderect(player2rect):
        speedball[0] = -speedball[0]
        speedball[1] = -speedball[1]

    ballrect = ballrect.move(speedball)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speedball[0] = -speedball[0]
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speedball[1] = -speedball[1]

    if ballrect.colliderect(player1rect):
        speedball[0] = abs(speedball[0])
        speedball[1] = (ballrect.centery - player1rect.centery) // 2  

    if ballrect.colliderect(player2rect):
        speedball[0] = -abs(speedball[0])
        speedball[1] = (ballrect.centery - player2rect.centery) // 2
        
    ventana.fill((35, 165, 15))
    ventana.blit(ball, ballrect)
    ventana.blit(player1, player1rect)
    ventana.blit(player2, player2rect)
    pygame.display.flip()
    clock.tick(60)


pygame.quit()