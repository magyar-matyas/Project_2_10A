import imp
import pygame
from sys import exit
from Szavak import Szavak
from Gombok import Gombok 
from Corpses import Corpses

my_font = pygame.font.SysFont("Comic Sans MS", 30)


# szavak beolvasás
szósorok = []
with open('szavak.txt', 'r', encoding='utf-8') as file:
    for sor in file.read().splitlines():
        szósorok.append(Szavak(sor))
        
# gombok beolv
betuk = []
with open("abc.txt", 'r', encoding='utf-8') as file:
    for b in file.read().strip().split(';'):
        betuk.append(Gombok(b))
 
 
  # emberek beolvasása
corpses = []
corpses.append(Corpses(1))
corpses.append(Corpses(2))
corpses.append(Corpses(3))
corpses.append(Corpses(4))
corpses.append(Corpses(5))
corpses.append(Corpses(6))


#functions
def spaceindex(szo):
    spacek = []
    i = 0
    for b in szo:
        if b == " ":
            spacek.append(i)
        i += 1
    return spacek

def vonalak(betűszám: int, spaceind: list, screen):
    w = 500 / betűszám
    s = 600 / betűszám
    vonal_surf = pygame.Surface((w, 3))
    for x in range(betűszám):
        vonal_rect = vonal_surf.get_rect(midleft = (600 + x * s , 150))
        if x not in spaceind:
            screen.blit(vonal_surf, vonal_rect)
            
def gombok_kiiras(oszt_betulist: list[Gombok], screen):
    h = 300
    w = 600
    ar = 500 / (len(oszt_betulist) / 2)
    for g in oszt_betulist:
        g.rect = g.surf.get_rect(center = (w, h))
        # pygame.draw.rect(screen, '#30e8ec', g.rect, 15)
        if g.value == 1:
            pygame.draw.rect(screen, 'Black', g.rect, 1)
        elif g.value == 0:
            pygame.draw.rect(screen, 'Red', g.rect, 2)
        elif g.value == 2:
            pygame.draw.rect(screen, 'Green', g.rect, 2)
        screen.blit(g.surf, g.rect)
        w += ar
        if w > 1150:
            h = 400
            w = 600
            
hiba = -1
       
def guess(szo: str, gomb, kirajzolaslista: list, szint, hiba, screen):
    if gomb.betu in szo.upper():
        gomb.value = 2
        for i in range(len(szo)):
            if gomb.betu == szo[i].upper():
                w = 500 / len(szo)
                s = 600 / len(szo)
                betu_surf = my_font.render(gomb.betu, False, (255,255,255))
                for x in range(len(szo)):
                    betu_rect = betu_surf.get_rect(midleft=(600 + x * s, 130))
                    if i == x:
                        screen.blit(betu_surf, betu_rect)
    else:
        gomb.value = 0
        kirajz_surface = kirajzolaslista[szint - 1].kirajz[hiba]
        kirajz_rect = kirajz_surface.get_rect(midtop=(200,200))
        screen.blit(kirajz_surface, kirajz_rect)
        
def akasztofa(screen,hatter_surface, hatter_rect, szo: str, spaceindex, gombok, kirajzolaslista, szint, hiba, win):
    jo = 0
    for g in gombok:
        g.value = 1
    guess_buttons = []
    level_surf = my_font.render(f'Level {szint}', False, (0,0,0))
    level_surf = pygame.transform.scale(level_surf, (180,70))
    level_rect = level_surf.get_rect(midtop= (600, 0))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for g in gombok:
                    if g.rect.collidepoint(pygame.mouse.get_pos()) and g.value == 1:
                        guess_buttons.append(g)
                        if g.betu not in szo.upper():
                            hiba += 1
                            g.value = 0
                            
        screen.blit(hatter_surface, hatter_rect)
        screen.blit(level_surf, level_rect)
        
        vonalak(len(szo), spaceindex, screen)
        gombok_kiiras(gombok, screen)
        for gues in guess_buttons:
            guess(szo, gues, kirajzolaslista, szint, hiba, screen)
    