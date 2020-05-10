import pygame

card1 = pygame.image.load("img/cards/card1.png")
card1 = pygame.transform.scale(card1, (200, 120))

card2 = pygame.image.load("img/cards/card1.png")
card2 = pygame.transform.scale(card1, (200, 120))

card3 = pygame.image.load("img/cards/card1.png")
card3 = pygame.transform.scale(card1, (200, 120))

card4 = pygame.image.load("img/cards/card1.png")
card4 = pygame.transform.scale(card1, (200, 120))

card4 = pygame.image.load("img/cards/card1.png")
card4 = pygame.transform.scale(card1, (200, 120))


def Card(card,x,y):
    window.blit(card,(x,y))
