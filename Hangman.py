import imp
import pygame
from sys import exit
from Szavak import Szavak
from Gombok import Gombok 
from Corpses import Corpses

my_font = pygame.font.SysFont("Comic Sans MS", 30)
clock = pygame.time.Clock()

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
            pygame.draw.rect(screen, 'Black', g.rect, g.keret)
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
    #running
    while True:
        keretesc = 2
        keretnxt = 2
        if win == 0:
            break
        elif win == 2:
            break
        for g in gombok:
            g.keret = 1
            if g.rect.collidepoint(pygame.mouse.get_pos()) and g.value == 1:
                g.keret = 2
        
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
            
        for g in guess_buttons:
            if g.value == 2:
                jo += 1
        
        ellenorzes = []
        for b in  szo.replace(" ",""):
            if b not in ellenorzes:
                ellenorzes.append(b)
    
        if jo == len(ellenorzes):
            next_surf = my_font.render('Next',False, (0,0,0) )
            next_surf = pygame.transform.scale(next_surf, (180,70))
            next_rect = next_surf.get_rect(midright= (900, 400))
            homme_surf = my_font.render('Menu',False, (0,0,0) )
            homme_surf = pygame.transform.scale(homme_surf, (180,70))
            homme_rect = homme_surf.get_rect(midleft= (300, 400))
            win_surface = pygame.Surface((1200,600))
            win_surface.fill((220,220,220))
            win_rect = win_surface.get_rect(midtop=(600,0))
            comp_surf = my_font.render('Completed',False, (0,0,0) )
            comp_surf = pygame.transform.scale(comp_surf, (300,100))
            comp_rect = comp_surf.get_rect(midbottom= (600, 300))
            screen.blit(win_surface, win_rect)
            screen.blit(homme_surf, homme_rect)
            screen.blit(next_surf, next_rect)
            screen.blit(comp_surf, comp_rect)
            level_surf = pygame.transform.scale(level_surf, (300,100))
            level_rect = level_surf.get_rect(midtop= (600, 0))
            screen.blit(level_surf, level_rect)
            if homme_rect.collidepoint(pygame.mouse.get_pos()):
                keretesc = 4
            elif next_rect.collidepoint(pygame.mouse.get_pos()):          
                keretnxt = 4
            pygame.draw.rect(screen, 'Black', next_rect, keretnxt)
            pygame.draw.rect(screen, 'Black', homme_rect, keretesc)
            for event in pygame.event.get():
                   
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if homme_rect.collidepoint(pygame.mouse.get_pos()):
                            win = 0
                            with open('score.txt', 'w', encoding='utf-8' ) as sc:
                                sc.write(f'{win}')
                
                    elif next_rect.collidepoint(pygame.mouse.get_pos()):
                            win = 2
                            with open('score.txt', 'w', encoding='utf-8' ) as sc:
                                sc.write(f'{win}')
                
            
            
        jo = 0
        
        if hiba == 9:
            homme_surf = my_font.render('Menu',False, (0,0,0) )
            homme_surf = pygame.transform.scale(homme_surf, (180,70))
            homme_rect = homme_surf.get_rect(midtop= (600, 400))
            win_surface = pygame.Surface((1200,600))
            win_surface.fill((220,220,220))
            win_rect = win_surface.get_rect(midtop=(600,0))
            comp_surf = my_font.render('Failed',False, (180,0,0) )
            comp_surf = pygame.transform.scale(comp_surf, (300,100))
            comp_rect = comp_surf.get_rect(midbottom= (600, 300))
            screen.blit(win_surface, win_rect)
            screen.blit(homme_surf, homme_rect)
            screen.blit(comp_surf, comp_rect)
            level_surf = pygame.transform.scale(level_surf, (300,100))
            level_rect = level_surf.get_rect(midtop= (600, 0))
            screen.blit(level_surf, level_rect)
            if homme_rect.collidepoint(pygame.mouse.get_pos()):
                keretesc = 4
            pygame.draw.rect(screen, 'Black', homme_rect, keretesc)
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if homme_rect.collidepoint(pygame.mouse.get_pos()):
                            win = 0
                            with open('score.txt', 'w', encoding='utf-8' ) as sc:
                                sc.write(f'{win}')
                
            
        pygame.display.update()
        clock.tick(60)