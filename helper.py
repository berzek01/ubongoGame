
def getImage(pygame, image, resize = False, width = 0, height = 0):
	img = pygame.image.load(image).convert_alpha()
	if resize:
		img = pygame.transform.scale(img, (width, height))
	return img

def getText(pygame, text, size, color):
	Font = pygame.font.SysFont("Comic Sans MS", size)
	return Font.render(text, True, color)

def printText(pygame, window, text, size, color, x, y):
	text = getText(pygame, text, size, color)
	window.blit(text, (x, y))

# 	background = pygame.image.load("img/fondo2.jpeg").convert()
# 	background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# 	bPlay = pygame.image.load("img/btn1.png")
# 	bPlay = pygame.transform.scale(bPlay, (240, 60))

# tablero = pygame.image.load("img/tableroMejorado.png")
# tablero = pygame.transform.scale(tablero, (850, 300))


# # MENU
# font_game = pygame.font.SysFont("Comic Sans MS", 100)
# menu_title = font_game.render("Ubongo", True, white)

# font_menu = pygame.font.SysFont("Comic Sans MS", 30)
# menu_play = font_menu.render("Play", True, white)
# menu_tutorial = font_menu.render("How to play", True, white)