import pygame
# CONSTANTES
WIDTH = 900
HEIGHT = 500

info = {}
info['pause'] = False
info['win'] = False
info['status'] = 1
info['time'] = 120
info['miliseconds'] = 0
# STATUS:
# MENU      1
# TUTORIAL  2
# PLAYING   3
# END       4

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()

background = pygame.image.load("fondo.jpeg").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# MENU
font_game = pygame.font.SysFont("Comic Sans MS", 100)
menu_title = font_game.render("Ubongo", True, (255, 255, 255))

font_menu = pygame.font.SysFont("Comic Sans MS", 40)
menu_play = font_menu.render("Play", True, (255, 255, 255))
menu_tutorial = font_menu.render("How to play", True, (255, 255, 255))

area_play = menu_play.get_rect()
area_tutorial = menu_tutorial.get_rect()



def initial():
    area_play.x = 260
    area_play.y = 300
    area_tutorial.x = 260
    area_tutorial.y = 350


def menu():
    window.blit(background, (0, 0))
    window.blit(menu_title, (260, 20))
    window.blit(menu_play, (260, 300))
    window.blit(menu_tutorial, (260, 350))

level = 1
font_game = pygame.font.SysFont("Comic Sans MS", 20)

def game():
    window.blit(background, (0, 0))
    text_level = font_game.render("Turno {}".format(level), True, (255, 255, 255))
    window.blit(text_level, (10, 10))
    text_time = font_game.render(str(info['time']), True, (255, 255, 255))
    window.blit(text_time, (400, 10))

    if not info['pause']:
        info['miliseconds']+=1
    if(info['miliseconds'] == 10):
        info['time']-=1
        info['miliseconds'] = 0

def end():
    font_game = pygame.font.SysFont("Comic Sans MS", 100)
    window.blit(background, (0, 0))
    if info['win']:
        text_level = font_game.render("You Won", True, (255, 255, 255))
        
    else:
        text_level = font_game.render("You Lose", True, (255, 255, 255))
    window.blit(text_level, (100, 100))


def command():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
            if info['status'] == 3 and event.key == pygame.K_RETURN:
                info['pause'] = not info['pause']
        if event.type == pygame.MOUSEBUTTONUP:
            if area_play.collidepoint(event.pos):
                info['status'] = 3
            if area_tutorial.collidepoint(event.pos):
                info['status'] = 2
    return True

initial()
playing = True
while playing:
    clock.tick(60) # fps
    playing = command()
    if info['time'] == 0:
       info['status'] = 4
       info['win'] = False 
    if info['status'] == 1:
        menu()
    if info['status'] == 2:
        menu()
    elif info['status'] == 3:
        game()
    elif info['status'] == 4:
        end()
    pygame.display.update()