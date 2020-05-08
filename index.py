import pygame
# CONSTANTES
WIDTH = 900
HEIGHT = 600

# colors
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
purple = (255, 0, 255)
brown = (128, 64, 0)

long  = 20

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

background = pygame.image.load("img/fondo2.jpeg").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

bPlay = pygame.image.load("img/btn1.png")
bPlay = pygame.transform.scale(bPlay, (240, 60))


bHowToPlay = pygame.image.load("img/btn1.png")
bHowToPlay = pygame.transform.scale(bHowToPlay, (240, 60))


tablero = pygame.image.load("img/tablero.png")
tablero = pygame.transform.scale(tablero, (900, 450))

# MENU
font_game = pygame.font.SysFont("Comic Sans MS", 100)
menu_title = font_game.render("Ubongo", True, white)

font_menu = pygame.font.SysFont("Comic Sans MS", 40)
menu_play = font_menu.render("Play", True, white)
menu_tutorial = font_menu.render("How to play", True, white)

area_play = menu_play.get_rect()
area_tutorial = menu_tutorial.get_rect()

area_bPlay= bPlay.get_rect();

def initial():
    area_play.x = 260
    area_play.y = 300
    area_tutorial.x = 260
    area_tutorial.y = 350


def gems():
    pygame.draw.circle(window, red,   (120, 165), 12)
    pygame.draw.circle(window, blue,  (120, 205), 12)
    pygame.draw.circle(window, green, (120, 240), 12)
    pygame.draw.circle(window, yellow,(120, 280), 12)
    pygame.draw.circle(window, purple,(120, 320), 12)
    pygame.draw.circle(window, brown, (120, 360), 12)


def P1(X,Y):
    pygame.draw.polygon(window, white, (      (X, Y), (X + long, Y),
                                            (X + long, Y-long), (X+(2*long), Y-long),
                                            (X+(long*2), Y), (X+(3*long), Y),
                                            (X+(long*3), Y+long), (X, Y + long) ))
def P2(X,Y):
    pygame.draw.polygon(window, white,   ((X, Y), (X+(long*4),Y),
                                        (X+(long*4), Y + long), (X, Y+long)))
def P3(X,Y):
    pygame.draw.polygon(window, white, ( (X, Y), (X+(long*2), Y),
                                         (X+(long*2), Y+(long*2)), ( X+(long*3), Y+(long*2)),
                                         (X+(long*3), Y+(long*3)), ( X+long,  Y+(long*3)),
                                         (X+long, Y+long), (X, Y+long)))
def P4(X,Y):
    pygame.draw.polygon(window, white, ((X, Y), (X+(long*2), Y),
                                        (X+(long*2), Y+(long)), (X+(long), Y+(long)),
                                        (X+(long), Y+(long*3)), (X+(long), Y+(long*3)),
                                        (X, Y+(long*3))))
def P5(X,Y):
    pygame.draw.polygon(window, white, ((X, Y), (X+(long*2), Y),
                                         (X+(long*2), Y+(long*2)), (X, Y+(long*2))))
def P6(X,Y):
    pygame.draw.polygon(window, white, ((X, Y), (X+long, Y),
                                        (X + long, Y+(long*2)), (X, Y+(long*2))))
def P7(X,Y):
    pygame.draw.polygon(window, white, ((X, Y), (X+(long*4), Y),
                                        (X+(long*4), Y+long), (X+(long*3), Y+long),
                                        (X+(long*3), Y+(2*long)), (X+(long*2), Y+(2*long)),
                                        (X+(long*2), Y+(2*long)), (X+(2*long), Y+long),
                                        (X,Y+long)))
def P8(X,Y):
    pygame.draw.polygon(window, white, ((X, Y), (X+(long*3), Y),
                                        (X+(long*3), Y+(long*2)), (X+long, Y+(long*2)),
                                        (X+long, Y+long), (X, Y+long)))

def P9(X,Y):
    pygame.draw.polygon(window, white, ((X, Y+long), (X+long, Y+long),
                                        (X+long, Y), (X+(long*3), Y),(X+(long*3), Y+long),
                                        (X+(long*2), Y+long), (X+(long*2), Y+(long*2)),
                                        (X, Y+(long*2))))
def P10(X,Y):
    pygame.draw.polygon(window, white, ((X, Y), (X+(long*3), Y),
                                        (X+(long*3), Y+long), (X, Y+long)))
def P11(X,Y):
    pygame.draw.polygon(window, white, ((X, Y), (X+(long*4), Y),
                                        (X+(long*4), Y+(long*2)), (X+(long*3), Y+(long*2)),
                                        (X+(long*3), Y+long), (X, Y+long)))
def P12(X,Y):
    pygame.draw.polygon(window, white, ((X, Y), (X+(long*2), Y),
                                        (X+(long*2), Y+long), (X+long, Y+long),
                                        (X+long, Y+(long*2)), (X, Y+(long*2))))
def menu():

    
    window.blit(background, (0, 0))
    window.blit(bPlay, (320, 300))
    window.blit(bHowToPlay,(320,355))
    window.blit(menu_title, (260, 20))
    window.blit(menu_play, (400, 300))
    window.blit(menu_tutorial, (340, 350))


    
level = 1
font_game = pygame.font.SysFont("Comic Sans MS", 20)


def game():
    window.blit(background, (0, 0))
    text_level = font_game.render(
        "Turno {}".format(level), True, white)
    window.blit(text_level, (10, 10))
    text_time = font_game.render(str(info['time']), True, white)
    window.blit(text_time, (400, 10))

    #Herramientas
    window.blit(tablero,(20,35))
    gems()
    P1(20,420)
    P2(120,420)
    P3(220,420)
    P4(320,420)
    P5(420,420)
    P6(520,420)
    P7(620,420)
    P8(720,420)
    P9(20,510)
    P10(120,510)
    P11(220,510)
    P12(320,510)
    
    if not info['pause']:
        info['miliseconds'] += 1
    if(info['miliseconds'] == 10):
        info['time'] -= 1
        info['miliseconds'] = 0


def end():
    font_game = pygame.font.SysFont("Comic Sans MS", 100)
    window.blit(background, (0, 0))
    if info['win']:
        text_level = font_game.render("You Won", True, white)

    else:
        text_level = font_game.render("You Lose", True, white)
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
            if area_play.collidepoint(event.pos) or area_bPlay.collidepoint(event.pos):
                info['status'] = 3
            if area_tutorial.collidepoint(event.pos):
                info['status'] = 2
    return True


initial()

playing = True
while playing:
    clock.tick(60)  # fps
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
