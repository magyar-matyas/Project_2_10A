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
corpses.append(Corpses(7))
corpses.append(Corpses(8))
corpses.append(Corpses(9))
corpses.append(Corpses(10))
corpses.append(Corpses(11))
corpses.append(Corpses(12))
corpses.append(Corpses(13))
corpses.append(Corpses(14))
corpses.append(Corpses(15))
corpses.append(Corpses(16))
corpses.append(Corpses(17))
corpses.append(Corpses(18))
corpses.append(Corpses(19))
corpses.append(Corpses(20))

       
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
        vonal_rect = vonal_surf.get_rect(midleft = (600 + x * s , 250))
        if x not in spaceind:
            screen.blit(vonal_surf, vonal_rect)
            
def gombok_kiiras(oszt_betulist: list[Gombok], screen):
    h = 350
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
            h = 450
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
                if len(szo) < 11:
                    betu_surf = pygame.transform.scale(betu_surf, (30 + (110 - len(szo) * 10),30 + (100 - len(szo) * 10)))
                for x in range(len(szo)):
                    betu_rect = betu_surf.get_rect(bottomleft=(600 + x * s, 249))
                    if i == x:
                        screen.blit(betu_surf, betu_rect)
    else:
        gomb.value = 0
        if  hiba == 0:
            kirajz_surface = kirajzolaslista[szint - 1].kirajz[hiba]
            kirajz_rect = kirajz_surface.get_rect(bottomleft = (20, 600))
            screen.blit(kirajz_surface, kirajz_rect)
        elif  hiba == 1:
            kirajz_surface = kirajzolaslista[szint - 1].kirajz[hiba]
            kirajz_rect = kirajz_surface.get_rect(bottomleft = (20, 180))
            screen.blit(kirajz_surface, kirajz_rect)
        elif hiba < 12 and hiba > 1:
            kirajz_surface = kirajzolaslista[szint - 1].kirajz[hiba]
            kirajz_rect = kirajz_surface.get_rect(midtop=(250,170))
            screen.blit(kirajz_surface, kirajz_rect)
    
def hs_mentes(szint):
    with open('highscore.txt', 'r', encoding='utf-8') as f:
        sz = f.read().strip()
        sz = int(sz)
        if szint > sz:
            with open('highscore.txt', 'w', encoding='utf-8') as f:
                f.write(f'{szint}')
   
def akasztofa(screen,hatter_surface, hatter_rect, szo: str, spaceindex, gombok, kirajzolaslista, szint, hiba, win):
    # screen = pygame.display.set_mode((1200, 600))
    # pygame.display.set_caption('Hangman')
    jo = 0

    for g in gombok:
        g.value = 1
    guess_buttons = []
    level_surf = my_font.render(f'Level {szint}', False, (0,0,0))
    level_surf = pygame.transform.scale(level_surf, (180,70))
    level_rect = level_surf.get_rect(midtop= (600, 0))
    akaszt_surf = pygame.Surface((40, 430))
    akaszt_rect = akaszt_surf.get_rect(bottomleft = (20, 600))
    akasztr_surf = pygame.Surface((300, 40))
    akasztr_rect = akasztr_surf.get_rect(bottomleft = (20, 180))
    
    
    # running
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
        if hiba >= 0:
            screen.blit(akaszt_surf,akaszt_rect)
        if hiba >= 1:
            screen.blit(akasztr_surf, akasztr_rect)

                

        screen.blit(hatter_surface, hatter_rect)
        screen.blit(level_surf, level_rect)
        if hiba > 1:
            pygame.draw.line(screen, 'Black', (40, 300), (120, 150), 20)
        vonalak(len(szo), spaceindex, screen)
        gombok_kiiras(gombok, screen)
        if hiba >= 0:
            screen.blit(akaszt_surf,akaszt_rect)
        if hiba >= 1:
            screen.blit(akasztr_surf, akasztr_rect)
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
            hs_mentes(szint)
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
            if szint == 20:
                comp_surf = my_font.render('You have Completed all the lvls',False, (0,0,0) )
                comp_surf = pygame.transform.scale(comp_surf, (600,100))
                comp_rect = comp_surf.get_rect(midtop= (600, 150))
                compl_surf = my_font.render('Congratulations, you are a big G, if you havent cheat',False, (0,0,0) )
                compl_surf = pygame.transform.scale(compl_surf, (1000,100))
                compl_rect = compl_surf.get_rect(midtop= (600, 250))
                comple_surf = my_font.render('Thanks for playing!',False, (0,0,0) )
                comple_surf = pygame.transform.scale(comple_surf, (300,100))
                comple_rect = comple_surf.get_rect(midtop= (600, 350))
                next_surf = my_font.render('I liked it',False, (0,0,0) )
                next_surf = pygame.transform.scale(next_surf, (180,70))
                next_rect = next_surf.get_rect(midright= (900, 500))
                homme_surf = my_font.render('I didnt liked it',False, (0,0,0) )
                homme_surf = pygame.transform.scale(homme_surf, (180,70))
                homme_rect = homme_surf.get_rect(midleft= (300, 500))
            
            screen.blit(win_surface, win_rect)
            screen.blit(homme_surf, homme_rect)
            screen.blit(next_surf, next_rect)
            screen.blit(comp_surf, comp_rect)
            if szint == 20:
                screen.blit(compl_surf, compl_rect)
                screen.blit(comple_surf, comple_rect)
        
                
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
        
        if hiba == 12:
            word_surf = my_font.render(f'Your word was: {szo}',False, (0,0,0) )
            word_surf = pygame.transform.scale(word_surf, (400,100))
            word_rect = word_surf.get_rect(midtop= (600, 400))
            homme_surf = my_font.render('Menu',False, (0,0,0) )
            homme_surf = pygame.transform.scale(homme_surf, (200,80))
            homme_rect = homme_surf.get_rect(midtop= (600, 250))
            win_surface = pygame.Surface((1200,600))
            win_surface.fill((220,220,220))
            win_rect = win_surface.get_rect(midtop=(600,0))
            comp_surf = my_font.render('Failed',False, (180,0,0) )
            comp_surf = pygame.transform.scale(comp_surf, (300,100))
            comp_rect = comp_surf.get_rect(midbottom= (600, 200))
            screen.blit(win_surface, win_rect)
            screen.blit(homme_surf, homme_rect)
            screen.blit(comp_surf, comp_rect)
            screen.blit(word_surf, word_rect)
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
