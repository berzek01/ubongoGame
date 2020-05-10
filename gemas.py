import pygame



gem1 = pygame.image.load("img/cards/card1.png")
gem1 = pygame.transform.scale(gem1, (50, 50))

gem2 = pygame.image.load("img/cards/card1.png")
gem2 = pygame.transform.scale(gem2, (50, 50))

gem3 = pygame.image.load("img/cards/card1.png")
gem3 = pygame.transform.scale(gem3, (50, 50))

gem4 = pygame.image.load("img/cards/card1.png")
gem4 = pygame.transform.scale(gem4, (50, 50))

gem5 = pygame.image.load("img/cards/card1.png")
gem5 = pygame.transform.scale(gem4, (50, 50))


def gem(gem,x,y):
    window.blit(gem,(x,y))
