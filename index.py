import pygame
import threading
from machine import machineSolution
from random import randint
import math
from cards import boards, pieces
from colors import *
from config import *
from helper import *
machineProcess = None

import cards

def initial():
    #VARIABLES GLOBALES
    data['btn'] = getImage(pygame, "img/btn1.png", True, 240, 60)
    data['menuTitle'] = getText(pygame, "Ubongo", 100, white)
    data['menuPlay'] = getText(pygame, "Play", 30, white)
    data['menuTutorial'] = getText(pygame, "How to play", 30, white)
    data['areaPlay'] = data['menuPlay'].get_rect()
    data['areaTutorial'] = data['menuTutorial'].get_rect()


    info['colorJ1'] = marroon
    info['colorJ2'] = gray
    info['background'] = getImage(pygame, "img/fondo2.jpeg", True, info['width'], info['height'])

    data['areaPlay'].x = 415
    data['areaPlay'].y = 304
    data['areaTutorial'].x = 260
    data['areaTutorial'].y = 350
    # area_data['btn']Play.x = 320
    # area_data['btn']Play.y = 300

def players():
    pygame.draw.circle(window, info['colorJ1'], (120, 168), 12)
    pygame.draw.circle(window, info['colorJ2'],(120, 203), 12)


def command():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
            if (info['status'] == 3 or info['status'] == 4) and event.key == pygame.K_RETURN:
                machine['delay'] = 2000
                pygame.time.delay(machine['delay'])
                machine['delay'] = 50
                # info['pause'] = not info['pause']
            # TEMPORAL
            # if info['status'] == 3 and event.key == pygame.K_p:
            #     info['status'] = 4
            # if (info['status'] == 3 or info['status'] == 4) and event.key == pygame.K_t:
            #     info['turno'] += 1
            # FIN TEMPORAL
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if data['areaPlay'].collidepoint(event.pos):
                info['status'] = 2
            if data['areaTutorial'].collidepoint(event.pos):
                info['status'] = 11
    return True


# ==================================================================================== #
# =================================== MAQUINA ======================================== #
# ==================================================================================== #

def rotate(piece):
    piece_rotate = []
    for j in range(len(piece[0])):
        piece_rotate.append([])
    for j in range(len(piece[0])):
        for i in range(len(piece)):
            piece_rotate[j].append(None)
            
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            piece_rotate[j][len(piece)-1-i] = piece[i][j]
    return piece_rotate

def turn(piece):
    piece_turn = []
    for i in range(len(piece)):
        piece_turn.append([])
        for j in range(len(piece[0])):
            piece_turn[i].append(None)

    for i in range(len(piece)):
        for j in range(len(piece[i])):
            piece_turn[i][len(piece[0])-1-j] = piece[i][j]
    return piece_turn

def pieceInBoard_position(board, piece, index, up, left):
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            x = up + i
            y = left + j
            if (x >= len(board) or y >= len(board[0])) or ((board[x][y] != 0) and (piece[i][j] == 1)):
                return False
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            x = up + i
            y = left + j
            board[x][y] = (index + 1) if piece[i][j] != 0 else board[x][y]
    return True

def pieceInBoard(board, piece, index):
    for left in range(len(board[0])):
        for up in range(len(board)):
            if pieceInBoard_position(board, piece, index, up, left):
                return True
    return False

def eraseSolution(board, piece, index):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == index + 1:
                board[i][j] = 0

def solution(board, pieces, index):
    if (index == len(pieces)):
        return True
    for attemp in range(len(pieces) - index):
        for i in range(4):
            pieces[index] = rotate(pieces[index])
            for j in range(2):
                pygame.time.delay(machine['delay'])
                pieces[index] = turn(pieces[index])
                if pieceInBoard(board, pieces[index], index):
                    if solution(board, pieces, index + 1):
                        machine['solved'] = True
                        return True
                    eraseSolution(board, pieces[index], index)
        piece = pieces.pop(index)
        pieces.append(piece)
    return False



# ==================================================================================== #
# ============================= FUNCIONES DE JUEGO =================================== #
# ==================================================================================== #

def menu():
    window.blit(data['btn'], (320, 300))
    window.blit(data['btn'],(320,365))
    window.blit(data['menuTitle'], (260, 20))
    window.blit(data['menuPlay'], (415, 304))
    window.blit(data['menuTutorial'], (350, 370))

def print_dado():
    info['dado'] = str(randint(0,5))
    dado = getImage(pygame, "img/dado/cara" + info['dado'] + ".png")
    window.blit(dado, (info['dadoX'], info['dadoY']))
    # pygame.display.update()

def draw(pieza, x, y):
    LADO = 50
    MARGEN = 1
    filas = len(pieza)
    columnas = len(pieza[0])
    for fila in range(filas):
        for columna in range(columnas):
            if pieza[fila][columna] == 1:
                pygame.draw.rect(window,
                                black,
                                [((MARGEN + LADO) * columna + MARGEN)+ x,
                                ((MARGEN + LADO) * fila + MARGEN)+ y,
                                LADO,
                                LADO])
            if pieza[fila][columna] == 0 and -1 in pieza[fila] :
                pygame.draw.rect(window,
                                 white,
                                 [((MARGEN + LADO) * columna + MARGEN) + x,
                                 ((MARGEN + LADO) * fila + MARGEN) + y,
                                 LADO,
                                 LADO])

def drawBoard(card, x, y):
    LADO = 50
    MARGEN = 1
    filas = len(card)
    columnas = len(card[0])
    colores = [white, red, magenta, green, orange]
    for fila in range(filas):
        for columna in range(columnas):
            if card[fila][columna] != -1:
                pygame.draw.rect(window,
                                 colores[card[fila][columna]],
                                 [((MARGEN + LADO) * columna + MARGEN) + x,
                                 ((MARGEN + LADO) * fila + MARGEN) + y,
                                 LADO,
                                 LADO])

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
            info['carta'] = str(randint(0,len(boards) - 1))
            machine['boardNumber'] = int(randint(0,len(boards) - 1))
            machine['board'] = boards[machine['boardNumber']]
            pygame.time.delay(2000)
    # if not info['pause']:
    info['miliseconds'] += 1
    if(info['miliseconds'] == 100):
        info['time'] -= 1
        info['miliseconds'] = 0




PositionsX = [50,300,600,900,1200,1500,1700]
PositionsY = [400,400,400,400,400,400,400]

def setPointers(x,y,indice):
    PositionsX[indice] = x
    PositionsY[indice] = y

def puzle():
    card = int(info['carta'])
    piece = int(info['dado'])
    draw(cards.boards[card], 200, 130)

    for i in range(len(cards.pieces[card][piece])):
        m_x, m_y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() == (1, 0, 0):
            x = PositionsX[i]
            y = PositionsY[i]
            dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
            if dis < 50:
                setPointers(m_x, m_y, i)
                print(x, y)
        if pygame.mouse.get_pressed() == (0, 0, 1):
            x = PositionsX[i]
            y = PositionsY[i]
            dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
            if dis < 50:
                cards.pieces[card][piece][i] = rotate(cards.pieces[card][piece][i])
                print(x, y)


    for i in range(len(cards.pieces[card][piece])):
        draw(cards.pieces[card][piece][i], PositionsX[i], PositionsY[i])




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

def gemas():
    text_level = font_game.render(
        "Turno {}".format(info["turno"]), True, white)
    window.blit(text_level, (10, 10))
    text_time = font_game.render(str(info['time']), True, white)
    window.blit(text_time, (400, 10))

    #Gemas
    gemas_aleatorias()

    #Herramientas
    window.blit(tablero,(20,35))
    players()

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
    

def solvePuzle():
    global machineProcess
    if machine['solved']:
        printText(pygame, window, "Resuelto por la PC", 25, blue, 900, 500)
        return
    if not machine['process']:
        machine['process'] = True
        card = int(machine['boardNumber'])
        piece = int(info['dado'])
        machine['boardSolution'] = boards[card]
        machineProcess = threading.Thread(target = solution, args = (machine['boardSolution'], pieces[card][piece], 0))
        machineProcess.start()

# ==================================================================================== #
# ==================================== JUEGO ========================================= #
# ==================================================================================== #

def game():
    playing = True
    while playing:
        # LOGICA GENERAL
        clock.tick(60)  # fps
        playing = command()
        window.blit(info['background'], (0, 0))

        # LOGICA DEL JUEGO
        if info['status'] == 1: # MENU
            menu()
        elif info['status'] == 11: # TUTORIAL
            menu()
        elif info['status'] == 2: # DADO
            print_dado()
            printText(pygame, window, str(info['time']), 20, white, 400, 10)
            contador()
        elif info['status'] == 3: # PUZLE
            printText(pygame, window, "Turno {}".format(info["turno"]), 20, white, 10, 10)
            printText(pygame, window, str(info['time']), 20, white, 400, 10)
            puzle()
            solvePuzle()
            contador()
            if info['time'] % 5 == 0:
                drawBoard(machine['boardSolution'], 800, 100)
            else:
                drawBoard(machine['board'], 800, 100)

        elif info['status'] == 4: # GEMAS
            gemas(info['colorJ1'], info['colorJ2'])
            contador()
        elif info['status'] == 5: # RESULTADO
            resultado()

        estado = getText(pygame, "Estado {}".format(info["status"]), 20, white)
        window.blit(estado, (800, 10))
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    window = pygame.display.set_mode((info['width'], info['height']), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    data = {}
    initial()
    game()

