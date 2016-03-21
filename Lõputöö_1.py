#Arvutimängud lõputöö
#Kivi-paber-käärid
#Koostasid Tarmo Kullas & Tarvo Mäesepp

import pygame, random, time, sys

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

def valimine(n):
    if i.type == pygame.MOUSEBUTTONDOWN:
                        mx, my = pygame.mouse.get_pos()
                        if mx > 70 and mx < 198 and my > (n*147.2)-128 and my < n*147.2:
                            e = False
                            if n == 1:
                                valik = "kivi"
                            if n == 2:
                                valik = "paber"
                            if n == 3:
                                valik = "käärid"
                            return e
                            return valik
            
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.MOUSEBUTTONDOWN:
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
    
                e = True
                while e == True:
                    for k in pygame.event.get():
                        x = random.randint(0, 3)
                        if x == 0:
                            pygame.draw.rect(ekraan, [246, 231, 195], [442, 166.4, 128, 128], 0)
                            ekraan.blit(kivi, (442, 166.4))
                            pygame.display.flip()
                            muutuja = "kivi"
                            time.sleep(0.05)
                        elif x == 1:
                            pygame.draw.rect(ekraan, [246, 231, 195], [442, 166.4, 128, 128], 0)
                            ekraan.blit(paber, (442, 166.4))
                            pygame.display.flip()
                            muutuja = "paber"
                            time.sleep(0.05)
                        elif x == 2:
                            pygame.draw.rect(ekraan, [246, 231, 195], [442, 166.4, 128, 128], 0)
                            ekraan.blit(käärid, (442, 166.4))
                            pygame.display.flip()
                            muutuja = "käärid"
                            time.sleep(0.05)
                        if k.type == pygame.MOUSEBUTTONDOWN:
                            mx, my = pygame.mouse.get_pos()
                            if mx > 70 and mx < 198 and my > (1*147.2)-128 and my < 1*147.2:
                                e = False
                                valik = "kivi"
                            if mx > 70 and mx < 198 and my > (2*147.2)-128 and my < 2*147.2:
                                e = False
                                valik = "paber"
                            if mx > 70 and mx < 198 and my > (3*147.2)-128 and my < 3*147.2:
                                e = False
                                valik = "käärid"
                        elif k.type == pygame.MOUSEBUTTONUP:
                            e = True
                  
                if valik == muutuja:
                    print ("viik")
                elif valik == "kivi" and muutuja == "paber":
                    print ("kaotus")
                elif valik == "kivi" and muutuja == "käärid":
                    print ("võit")
                elif valik == "paber" and muutuja == "kivi":
                    print ("võit")
                elif valik == "paber" and muutuja == "käärid":
                    print ("kaotus")
                elif valik == "käärid" and muutuja == "kivi":
                    print ("kaotus")
                elif valik == "käärid" and muutuja == "paber":
                    print ("võit")
                        
            


               
