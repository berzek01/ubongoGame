import pygame
from random import randint


while playing:
    # LOGICA GENERAL
    clock.tick(60)  # fps
    playing = command()
    window.blit(background, (0, 0))

    # LOGICA DEL JUEGO
    if info['status'] == 1: # MENU
        menu()
    elif info['status'] == 11: # TUTORIAL
        menu()
    elif info['status'] == 2: # DADO
        print_dado()
    elif info['status'] == 3: # PUZLE
        puzle()
    elif info['status'] == 4: # GEMAS
        gemas(color1,color2)
    elif info['status'] == 5: # RESULTADO
        resultado()
    pygame.display.update()
