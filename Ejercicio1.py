#HaxBall

import pygame

pygame.init()

resolution = (720,640)
ventana = pygame.display.set_mode(resolution)
pygame.display.set_caption("Haxball")

# Bucle principal del juego
jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False


    ventana.fill((35, 165, 15))
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()