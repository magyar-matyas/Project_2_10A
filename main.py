import imp
import pygame
from sys import exit
from Szavak import Szavak
from Gombok import Gombok 
from Corpses import Corpses
from Hangman import *

my_font = pygame.font.SysFont("Comic Sans MS", 30)

# szavak beolvasás
szósorok = []
with open('szavak.txt', 'r', encoding='utf-8') as file:
    for sor in file.read().splitlines():
        szósorok.append(Szavak(sor))
custszosorok = []
with open('custom.txt', 'r', encoding='utf-8') as file:
    for sor in file.read().splitlines():
        custszosorok.append(Szavak(sor))

def gomb_beolv():       
    betuk = []
    with open("abc.txt", 'r', encoding='utf-8') as file:
        for b in file.read().strip().split(';'):
            betuk.append(Gombok(b))
gomb_beolv()

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

#highscore beolvasás:
with open('highscore.txt', 'r', encoding='utf-8') as file:
    var = file.read().strip()
    hsc = int(var)
        
#pygame
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption('Hangman Tyranny')
clock = pygame.time.Clock()

# surfaces
hatter_surface = pygame.Surface((1200, 600))
hatter_surface.fill((200, 200, 200))
hatter_rect = hatter_surface.get_rect(midtop = (600, 0))

fokepernyo_surf = pygame.image.load('képek/pixil-frame-1.png')
# fokepernyo_surf.fill((255,255,255))
fokepernyo_rect = fokepernyo_surf.get_rect(topleft =(0,0))

ht_surf = my_font.render('Hangman Tyranny', False, (0,0,0))
ht_surf = pygame.transform.scale(ht_surf, (500,150))
ht_rect = ht_surf.get_rect(midleft= (150, 120))

play_surf = my_font.render(' Play ',False, (0,0,0) )
play_surf = pygame.transform.scale(play_surf, (180,70))
play_rect = play_surf.get_rect(midleft= (150, 300))

exit_surf = my_font.render('Exit',False, (0,0,0) )
exit_surf = pygame.transform.scale(exit_surf, (100,50))
exit_rect = exit_surf.get_rect(midleft= (150, 500))

custom_surf = my_font.render(' Custom ',False, (0,0,0) )
custom_surf = pygame.transform.scale(custom_surf, (180,70))
custom_rect = custom_surf.get_rect(midleft= (150, 400))

hscore_surf = my_font.render('Highscore',False, (0,0,0) )
hscore_surf = pygame.transform.scale(hscore_surf, (170,70))
hscore_rect = hscore_surf.get_rect(midleft= (855, 280))

akaszt_surf = pygame.Surface((50, 500))
akaszt_rect = akaszt_surf.get_rect(bottomleft = (50, 600))
akasztr_surf = pygame.Surface((400, 50))
akasztr_rect = akasztr_surf.get_rect(bottomleft = (50, 100))


win = 1 #ha 0 akkor nincs next
hiba = -1
keretc = 2
keretp = 2
keretex = 2
    
while True:
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(pygame.mouse.get_pos()):
                    szo = szósorok[0].random_szo
                    szo2 = szósorok[1].random_szo
                    szo3 = szósorok[2].random_szo
                    szo4 = szósorok[3].random_szo
                    szo5 = szósorok[4].random_szo
                    szo6 = szósorok[5].random_szo
                    szo7 = szósorok[6].random_szo
                    szo8 = szósorok[7].random_szo
                    szo9 = szósorok[8].random_szo
                    szo10 = szósorok[9].random_szo
                    szo11 = szósorok[10].random_szo
                    szo12 = szósorok[11].random_szo
                    szo13 = szósorok[12].random_szo
                    szo14 = szósorok[13].random_szo
                    szo15 = szósorok[14].random_szo
                    szo16 = szósorok[15].random_szo
                    szo17 = szósorok[16].random_szo
                    szo18 = szósorok[17].random_szo
                    szo19 = szósorok[18].random_szo
                    szo20 = szósorok[19].random_szo
                    akasztofa(screen, hatter_surface, hatter_rect, szo, spaceindex(szo),betuk, corpses, 1, hiba, win)
                    with open('score.txt', 'r', encoding='utf-8') as sc:
                        if sc.read().strip() == '2':
                            gomb_beolv()
                            akasztofa(screen, hatter_surface, hatter_rect, szo2, spaceindex(szo2),betuk, corpses, 2, hiba, win)
                    with open('score.txt', 'r', encoding='utf-8') as sc:
                        if sc.read().strip() == '2':
                            gomb_beolv()
                            akasztofa(screen, hatter_surface, hatter_rect, szo3, spaceindex(szo3),betuk, corpses, 3, hiba, win)
                    with open('score.txt', 'r', encoding='utf-8') as sc:
                        if sc.read().strip() == '2':
                            gomb_beolv()
                            akasztofa(screen, hatter_surface, hatter_rect, szo4, spaceindex(szo4),betuk, corpses, 4, hiba, win)
                    with open('score.txt', 'r', encoding='utf-8') as sc:
                        if sc.read().strip() == '2':
                            gomb_beolv()
                            akasztofa(screen, hatter_surface, hatter_rect, szo5, spaceindex(szo5),betuk, corpses, 5, hiba, win)
                    with open('score.txt', 'r', encoding='utf-8') as sc:
                        if sc.read().strip() == '2':
                            gomb_beolv()
                            akasztofa(screen, hatter_surface, hatter_rect, szo6, spaceindex(szo6),betuk, corpses, 6, hiba, win)
                    with open('score.txt', 'r', encoding='utf-8') as sc:
                        if sc.read().strip() == '2':
                            gomb_beolv()
                            akasztofa(screen, hatter_surface, hatter_rect, szo7, spaceindex(szo7),betuk, corpses, 7, hiba, win)
                    with open('score.txt', 'r', encoding='utf-8') as sc:
                        if sc.read().strip() == '2':
                            gomb_beolv()
                            akasztofa(screen, hatter_surface, hatter_rect, szo8, spaceindex(szo8),betuk, corpses, 8, hiba, win)
                    with open('score.txt', 'r', encoding='utf-8') as sc:
                        if sc.read().strip() == '2':
                            gomb_beolv()
                            akasztofa(screen, hatter_surface, hatter_rect, szo9, spaceindex(szo9),betuk, corpses, 9, hiba, win)
                    with open('score.txt', 'r', encoding='utf-8') as sc:
                        if sc.read().strip() == '2':
                            gomb_beolv()
                            akasztofa(screen, hatter_surface, hatter_rect, szo10, spaceindex(szo10),betuk, corpses, 10, hiba, win)
                    with open('score.txt', 'r', encoding='utf-8') as sc:
                        if sc.read().strip() == '2':
                            gomb_beolv()
                            akasztofa(screen, hatter_surface, hatter_rect, szo11, spaceindex(szo11),betuk, corpses, 11, hiba, win)
                    with open('score.txt', 'r', encoding='utf-8') as sc:
                        if sc.read().strip() == '2':
                            gomb_beolv()
                            akasztofa(screen, hatter_surface, hatter_rect, szo12, spaceindex(szo12),betuk, corpses, 12, hiba, win)
                    with open('score.txt', 'r', encoding='utf-8') as sc:
                        if sc.read().strip() == '2':
                            gomb_beolv()
                            akasztofa(screen, hatter_surface, hatter_rect, szo13, spaceindex(szo13),betuk, corpses, 13, hiba, win)
                    with open('score.txt', 'r', encoding='utf-8') as sc:
                        if sc.read().strip() == '2':
                            gomb_beolv()
                            akasztofa(screen, hatter_surface, hatter_rect, szo14, spaceindex(szo14),betuk, corpses, 14, hiba, win)
                    with open('score.txt', 'r', encoding='utf-8') as sc:
                        if sc.read().strip() == '2':
                            gomb_beolv()
                            akasztofa(screen, hatter_surface, hatter_rect, szo15, spaceindex(szo15),betuk, corpses, 15, hiba, win)
                    with open('score.txt', 'r', encoding='utf-8') as sc:
                        if sc.read().strip() == '2':
                            gomb_beolv()
                            akasztofa(screen, hatter_surface, hatter_rect, szo16, spaceindex(szo16),betuk, corpses, 16, hiba, win)
                    with open('score.txt', 'r', encoding='utf-8') as sc:
                        if sc.read().strip() == '2':
                            gomb_beolv()
                            akasztofa(screen, hatter_surface, hatter_rect, szo17, spaceindex(szo17),betuk, corpses, 17, hiba, win)
                    with open('score.txt', 'r', encoding='utf-8') as sc:
                        if sc.read().strip() == '2':
                            gomb_beolv()
                            akasztofa(screen, hatter_surface, hatter_rect, szo18, spaceindex(szo18),betuk, corpses, 18, hiba, win)
                    with open('score.txt', 'r', encoding='utf-8') as sc:
                        if sc.read().strip() == '2':
                            gomb_beolv()
                            akasztofa(screen, hatter_surface, hatter_rect, szo19, spaceindex(szo19),betuk, corpses, 19, hiba, win)
                    with open('score.txt', 'r', encoding='utf-8') as sc:
                        if sc.read().strip() == '2':
                            gomb_beolv()
                            akasztofa(screen, hatter_surface, hatter_rect, szo20, spaceindex(szo20),betuk, corpses, 20, hiba, win)                 
                elif custom_rect.collidepoint(pygame.mouse.get_pos()):
                    custszo = custszosorok[1].random_szo
                    akasztofa(screen, hatter_surface, hatter_rect, custszo, spaceindex(custszo),betuk, corpses, 1, hiba, win)
                elif exit_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    exit()  
    if custom_rect.collidepoint(pygame.mouse.get_pos()):
        keretc = 4
    elif play_rect.collidepoint(pygame.mouse.get_pos()):
        keretp = 4
    elif exit_rect.collidepoint(pygame.mouse.get_pos()):
        keretex = 4
       
    with open('highscore.txt', 'r', encoding='utf-8') as file:
        var = file.read().strip()
        hsc = int(var)  
        hscoren_surf = my_font.render(f'{hsc}',False, (0,0,0) )
        hscoren_surf = pygame.transform.scale(hscoren_surf, (100,100))
        hscoren_rect = hscoren_surf.get_rect(midtop= (935, 320))    
    screen.blit(fokepernyo_surf, fokepernyo_rect)
    screen.blit(play_surf, play_rect)
    pygame.draw.rect(screen, 'Black', play_rect, keretp)
    screen.blit(custom_surf, custom_rect)
    pygame.draw.rect(screen, 'Black', custom_rect, keretc)
    screen.blit(exit_surf, exit_rect)
    pygame.draw.rect(screen, 'Black', exit_rect, keretex)
    screen.blit(hscore_surf, hscore_rect)
    screen.blit(hscoren_surf, hscoren_rect)
    screen.blit(ht_surf,ht_rect)
    # screen.blit(akaszt_surf, akaszt_rect)
    # screen.blit(akasztr_surf, akasztr_rect)
    keretc = 2
    keretp = 2
    keretex = 2
    
    
    
    pygame.display.update()
    clock.tick(60)