#Arvutimängud lõputöö
#Kivi-paber-käärid
#Koostasid Tarmo Kullas & Tarvo Mäesepp

import pygame, random, sys, time

#Ekraan
pygame.init()
ekraan = pygame.display.set_mode([640, 480])
ekraan.fill([246, 231, 195])

#Esileht
header = pygame.image.load("header.png") #493x71 px
ekraan.blit(header, (73.5, 60))

alusta = pygame.image.load("alusta.png") #260x61 px
ekraan.blit(alusta, (190, 260))

pygame.display.flip()
            
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
            mx, my = pygame.mouse.get_pos()
            if mx > 190 and mx < 450 and my > 260 and my < 321:

                #Kui on vajutatud nuppu alusta
                ekraan.fill([246, 231, 195])

                #Elemendid
                kivi = pygame.image.load("kivi.png") #128x128px
                paber = pygame.image.load("paber.png") #128x128px
                käärid = pygame.image.load("k22rid.png") #128x128px

                ekraan.blit(kivi, (70, 19.2))
                ekraan.blit(paber, (70, 166.4))
                ekraan.blit(käärid, (70, 313.6))

                pygame.display.flip()

                i = "õige"
                while i == "õige":
                    pygame.draw.rect(ekraan, [246, 231, 195], [442, 166.4, 128, 128], 0)
                    ekraan.blit(kivi, (442, 166.4))
                    pygame.display.flip()
                    time.sleep(0.1)
                    pygame.draw.rect(ekraan, [246, 231, 195], [442, 166.4, 128, 128], 0)
                    ekraan.blit(paber, (442, 166.4))
                    pygame.display.flip()
                    time.sleep(0.1)
                    pygame.draw.rect(ekraan, [246, 231, 195], [442, 166.4, 128, 128], 0)
                    ekraan.blit(käärid, (442, 166.4))
                    pygame.display.flip()
                    time.sleep(0.1)

Tarvo on pede
               
