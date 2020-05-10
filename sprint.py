import pygame
import sys

def load_image(name):
    image = pygame.image.load(name)
    return image

class TestSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(TestSprite, self).__init__()
        self.images = []
        self.images.append(load_image('img/dado/dado1.png'))
        self.images.append(load_image('img/dado/dado2.png'))
        self.images.append(load_image('img/dado/dado3.png'))
        # assuming both images are 64x64 pixels

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(0, 0, 64, 64)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

def main():
    pygame.init()
    screen = pygame.display.set_mode((250, 250))

    my_sprite = TestSprite()
    my_group = pygame.sprite.Group(my_sprite)

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        # Calling the 'my_group.update' function calls the 'update' function of all 
        # its member sprites. Calling the 'my_group.draw' function uses the 'image'
        # and 'rect' attributes of its member sprites to draw the sprite.
        my_group.update()
        my_group.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()
