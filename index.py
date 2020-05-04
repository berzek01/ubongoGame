import pygame as pyg

pyg.init()

# data
_width = 500
_heigth = 500
x = 300
y = 300
x_width = 20
y_height = 20
point = 0
clock = pyg.time.Clock()

window = pyg.display.set_mode((_width, _heigth))
font = pyg.font.SysFont("arial", 24)
text = font.render("TEXT", True, (0, 0, 0))

playing = True

while playing:

    clock.tick(60)  # fps

    # events
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            playing = False
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_p:
                point += 1

    # logic
    text_point = font.render("Points : "+str(point), True, (0, 0, 0))

    # draw
    window.fill((255, 255, 255))

    window.blit(text, (220, 10))
    window.blit(text_point, (10, 10))

    pyg.draw.rect(window, (255, 255, 0), (x, y, x_width, y_height))
    pyg.draw.polygon(window, (255, 0, 0), ((100, 100), (120, 100),
                                           (120, 80), (140, 80), (140, 100), (160, 100), (160, 120), (100, 120)))

    # update
    pyg.display.update()

# pyg.time.delay(5000)
pyg.quit()

"""if event.type == pyg.KEYDOWN:
    if event.key == pyg.K_q:
        si presiono q"""
