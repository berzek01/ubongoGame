import pygame
from random import randint


# CONSTANTES
WIDTH = 900
HEIGHT = 600

# COLORS
def getRandomColor():
    return (randint(0,255),randint(0,255),randint(0,255))
white = ((255,255,255))
blue = ((0,0,255))
green = ((0,255,0))
red = ((255,0,0))
black = ((0,0,0))
orange = ((255,100,10))
yellow = ((255,255,0))
blue_green = ((0,255,170))
marroon = ((115,0,0))
lime = ((180,255,100))
pink = ((255,100,180))
purple = ((240,0,255))
gray = ((127,127,127))
magenta = ((255,0,230))
brown = ((100,40,0))
forest_green = ((0,50,0))
navy_blue = ((0,0,100))
rust = ((210,150,75))
dandilion_yellow = ((255,200,0))
highlighter = ((255,255,100))
sky_blue = ((0,255,255))
light_gray = ((200,200,200))
dark_gray = ((50,50,50))
tan = ((230,220,170))
coffee_brown =((200,190,140))
moon_glow = ((235,245,255))

long  = 20

info = {}
info['pause'] = False
info['win'] = False
info['status'] = 1
info['time'] = 5
info['miliseconds'] = 0
info['turno'] = 1
info['carta'] = 1
info['printed_gema'] = False

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()

background = pygame.image.load("img/fondo2.jpeg").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

bPlay = pygame.image.load("img/btn1.png")
bPlay = pygame.transform.scale(bPlay, (240, 60))

bHowToPlay = pygame.image.load("img/btn1.png")
bHowToPlay = pygame.transform.scale(bHowToPlay, (240, 60))

tablero = pygame.image.load("img/tableroMejorado.png")
tablero = pygame.transform.scale(tablero, (850, 300))

# MENU
font_game = pygame.font.SysFont("Comic Sans MS", 100)
menu_title = font_game.render("Ubongo", True, white)

font_menu = pygame.font.SysFont("Comic Sans MS", 30)
menu_play = font_menu.render("Play", True, white)
menu_tutorial = font_menu.render("How to play", True, white)

area_play = menu_play.get_rect()
area_tutorial = menu_tutorial.get_rect()
area_bPlay= bPlay.get_rect();

def initial():
    area_play.x = 415
    area_play.y = 304
    area_bPlay.x = 320
    area_bPlay.y = 300
    area_tutorial.x = 260
    area_tutorial.y = 350


def players(color1, color2):
    pygame.draw.circle(window, color1, (120, 168), 12)
    pygame.draw.circle(window, color2,(120, 203), 12)

# PIEZAS

def P1(X,Y):
    pygame.draw.polygon(window, white, (      (X, Y), (X + long, Y),
                                            (X + long, Y-long), (X+(2*long), Y-long),
                                            (X+(long*2), Y), (X+(3*long), Y),
                                            (X+(long*3), Y+long), (X, Y + long) ))
def P2(X,Y):
    pygame.draw.polygon(window, red,   ((X, Y), (X+(long*4),Y),
                                        (X+(long*4), Y + long), (X, Y+long)))
def P3(X,Y):
    pygame.draw.polygon(window, blue, ( (X, Y), (X+(long*2), Y),
                                         (X+(long*2), Y+(long*2)), ( X+(long*3), Y+(long*2)),
                                         (X+(long*3), Y+(long*3)), ( X+long,  Y+(long*3)),
                                         (X+long, Y+long), (X, Y+long)))
def P4(X,Y):
    pygame.draw.polygon(window, green, ((X, Y), (X+(long*2), Y),
                                        (X+(long*2), Y+(long)), (X+(long), Y+(long)),
                                        (X+(long), Y+(long*3)), (X+(long), Y+(long*3)),
                                        (X, Y+(long*3))))
def P5(X,Y):
    pygame.draw.polygon(window, purple, ((X, Y), (X+(long*2), Y),
                                         (X+(long*2), Y+(long*2)), (X, Y+(long*2))))
def P6(X,Y):
    pygame.draw.polygon(window, brown, ((X, Y), (X+long, Y),
                                        (X + long, Y+(long*2)), (X, Y+(long*2))))
def P7(X,Y):
    pygame.draw.polygon(window, blue_green, ((X, Y), (X+(long*4), Y),
                                        (X+(long*4), Y+long), (X+(long*3), Y+long),
                                        (X+(long*3), Y+(2*long)), (X+(long*2), Y+(2*long)),
                                        (X+(long*2), Y+(2*long)), (X+(2*long), Y+long),
                                        (X,Y+long)))
def P8(X,Y):
    pygame.draw.polygon(window, lime, ((X, Y), (X+(long*3), Y),
                                        (X+(long*3), Y+(long*2)), (X+long, Y+(long*2)),
                                        (X+long, Y+long), (X, Y+long)))

def P9(X,Y):
    pygame.draw.polygon(window, dark_gray, ((X, Y+long), (X+long, Y+long),
                                        (X+long, Y), (X+(long*3), Y),(X+(long*3), Y+long),
                                        (X+(long*2), Y+long), (X+(long*2), Y+(long*2)),
                                        (X, Y+(long*2))))
def P10(X,Y):
    pygame.draw.polygon(window, tan, ((X, Y), (X+(long*3), Y),
                                        (X+(long*3), Y+long), (X, Y+long)))
def P11(X,Y):
    pygame.draw.polygon(window, orange, ((X, Y), (X+(long*4), Y),
                                        (X+(long*4), Y+(long*2)), (X+(long*3), Y+(long*2)),
                                        (X+(long*3), Y+long), (X, Y+long)))
def P12(X,Y):
    pygame.draw.polygon(window, moon_glow, ((X, Y), (X+(long*2), Y),
                                        (X+(long*2), Y+long), (X+long, Y+long),
                                        (X+long, Y+(long*2)), (X, Y+(long*2))))


font_game = pygame.font.SysFont("Comic Sans MS", 20)


def command():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
            if (info['status'] == 3 or info['status'] == 4) and event.key == pygame.K_RETURN:
                info['pause'] = not info['pause']
            # TEMPORAL
            if info['status'] == 3 and event.key == pygame.K_p:
                info['status'] = 4
            if (info['status'] == 3 or info['status'] == 4) and event.key == pygame.K_t:
                info['turno'] += 1
            # FIN TEMPORAL
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if area_play.collidepoint(event.pos) or area_bPlay.collidepoint(event.pos):
                info['status'] = 2
            if area_tutorial.collidepoint(event.pos):
                info['status'] = 11
    return True

# ==================================================================================== #
# ============================= FUNCIONES DE JUEGO =================================== #
# ==================================================================================== #

def menu():
    window.blit(bPlay, (320, 300))
    window.blit(bHowToPlay,(320,365))
    window.blit(menu_title, (260, 20))
    window.blit(menu_play, (415, 304))
    window.blit(menu_tutorial, (350, 370))

dadoPosX = int((WIDTH - 188) / 2)
dadoPosY = int((HEIGHT - 177) / 2)
def print_dado():
    dado = pygame.image.load("img/dado/cara" + str(randint(1,6)) + ".png").convert_alpha()
    window.blit(dado, (dadoPosX, dadoPosY))
    pygame.display.update()
    contador()



# CARTAS
def print_card(num):
    card = pygame.image.load("img/cards/card" + num + ".png").convert_alpha()
    card = pygame.transform.scale(card, (520, 290))
    window.blit(card,(170, 80))

# GEMAS
def print_gema(num, x, y):
    gema = pygame.image.load("img/gemas/gema{}.png".format(num)).convert_alpha()
    gema = pygame.transform.scale(gema, (50, 50))
    window.blit(gema,(x, y))

def contador():
    if info['time'] == 0:
        if info['status'] == 3: # PUZLE
            info['time'] = 120
        elif info['status'] == 4: # GEMAS
            info['status'] = 2 if info['turno'] < 9 else 5
            info['turno'] += 1
            info['time'] = 5
        elif info['status'] == 2: # DADO
            info['status'] = 3
            info['time'] = 120
            info['carta'] = str(randint(1,5))
            pygame.time.delay(2000)
    if not info['pause']:
        info['miliseconds'] += 1
    if(info['miliseconds'] == 10):
        info['time'] -= 1
        info['miliseconds'] = 0


def moverPieza(pieza):
    mouseX, mouseY = pygame.mouse.get_pos()


def puzle():
    text_level = font_game.render(
        "Turno {}".format(info["turno"]), True, white)
    window.blit(text_level, (10, 10))
    text_time = font_game.render(str(info['time']), True, white)
    window.blit(text_time, (400, 10))
    print_card(info['carta'])
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
    contador()


gemasJugador = []
def gemas_aleatorias():
    if not info['printed_gema']:
        info['printed_gema'] = True
        ngemas = randint(0, 10)
        for i in range(ngemas):
            n = randint(1, 15)
            x = randint(70, 830)
            y = randint(360, 500)
            gemasJugador.append((n, (x, y)))
    else:
        for i in range(len(gemasJugador)):
            print_gema(gemasJugador[i][0], gemasJugador[i][1][0], gemasJugador[i][1][1])

def gemas(color1,color2):
    text_level = font_game.render(
        "Turno {}".format(info["turno"]), True, white)
    window.blit(text_level, (10, 10))
    text_time = font_game.render(str(info['time']), True, white)
    window.blit(text_time, (400, 10))

    #Gemas
    gemas_aleatorias()

    #Herramientas
    window.blit(tablero,(20,35))
    players(color1,color2)
    contador()

def resultado():
    titulo = pygame.font.SysFont("Comic Sans MS", 100).render("Resultados", True, white)
    window.blit(titulo, (190, 20))

    tu = pygame.font.SysFont("Comic Sans MS", 50).render("Tu", True, white)
    window.blit(tu, (100, 150))
    tu_resultado = pygame.font.SysFont("Comic Sans MS", 25).render("15 gemasdel mismo color", True, white)
    window.blit(tu_resultado, (50, 500))

    pc = pygame.font.SysFont("Comic Sans MS", 50).render("Rival", True, white)
    window.blit(pc, (600, 150))
    pc_resultado = pygame.font.SysFont("Comic Sans MS", 25).render("12 gemas del mismo color", True, white)
    window.blit(pc_resultado, (550, 500))

    gemas_aleatorias()
    


# ==================================================================================== #
# ==================================== JUEGO ========================================= #
# ==================================================================================== #

initial()
color1 = getRandomColor();
color2 = getRandomColor();

playing = True
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

    # estado = font_game.render(
    #     "Estado {}".format(info["status"]), True, white)
    # window.blit(estado, (800, 10))
    pygame.display.update()