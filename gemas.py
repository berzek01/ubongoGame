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

# import random
# gema_roja=[1,1,1,1,1,1,1,1,1,1,1,1]
# gema_azul=[2,2,2,2,2,2,2,2,2,2,2,2]
# gema_morada=[3,3,3,3,3,3,3,3,3,3,3,3]
# gema_rosada=[4,4,4,4,4,4,4,4,4,4,4,4]
# gema_verde=[5,5,5,5,5,5,5,5,5,5,5,5]
# gema_blanca=[6,6,6,6,6,6,6,6,6,6,6,6]
# allGems=[gema_roja,gema_azul,gema_morada,gema_rosada,gema_verde,gema_blanca]
# def crearTableroGemas():
#     gemas=[]
#     for i in range(6):
#         gemas.append([])
#         for j in range(12):
#             color_gem=random.choice(allGems)
#             if len(color_gem)==1:
#                 gema=color_gem.pop()
#                 allGems.remove(color_gem)#quitar arreglo incomleto sad
#                 gemas[i].append(gema)
#                 break
#             gema=color_gem.pop()
#             gemas[i].append(gema)
    
#     return gemas
# print(crearTableroGemas())
