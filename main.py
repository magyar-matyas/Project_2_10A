import imp
import pygame
from sys import exit
from Szavak import Szavak
from Gombok import Gombok 
from Corpses import Corpses
from Hangman import *

pygame.init()


def main() -> None:
    
    my_font = pygame.font.SysFont("Comic Sans MS", 30)

    # szavak beolvasás
    szósorok = []
    with open('szavak.txt', 'r', encoding='utf-8') as file:
        for sor in file.read().splitlines():
            szósorok.append(Szavak(sor))

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
            
    #pygame
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption('Hangman')
    clock = pygame.time.Clock()

    # surfaces
    hatter_surface = pygame.Surface((1200, 600))
    hatter_surface.fill((200, 200, 200))
    hatter_rect = hatter_surface.get_rect(midtop = (600, 0))

    fokepernyo_surf = pygame.Surface((1200,600))
    # fokepernyo_surf.fill((255,255,255))
    fokepernyo_rect = fokepernyo_surf.get_rect(topleft =(0,0))

    play_surf = my_font.render('Play',False, (255,255,255) )
    play_surf = pygame.transform.scale(play_surf, (180,70))
    play_rect = play_surf.get_rect(midleft= (150, 300))
    
    exit_surf = my_font.render('Exit',False, (0,0,0) )
    exit_surf = pygame.transform.scale(exit_surf, (100,50))
    exit_rect = exit_surf.get_rect(midleft= (150, 500))

    custom_surf = my_font.render('Custom',False, (255,255,255) )
    custom_surf = pygame.transform.scale(custom_surf, (180,70))
    custom_rect = custom_surf.get_rect(midleft= (150, 400))

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
                    elif custom_rect.collidepoint(pygame.mouse.get_pos()):
                        pass
                    elif exit_rect.collidepoint(pygame.mouse.get_pos()):
                        pygame.quit()
                        exit() 
        if custom_rect.collidepoint(pygame.mouse.get_pos()):
            keretc = 4
        elif play_rect.collidepoint(pygame.mouse.get_pos()):
            keretp = 4
        elif exit_rect.collidepoint(pygame.mouse.get_pos()):
            keretex = 4
                    
        screen.blit(fokepernyo_surf, fokepernyo_rect)
        screen.blit(play_surf, play_rect)
        pygame.draw.rect(screen, 'White', play_rect, keretp)
        screen.blit(custom_surf, custom_rect)
        pygame.draw.rect(screen, 'White', custom_rect, keretc)
        screen.blit(exit_surf, exit_rect)
        pygame.draw.rect(screen, 'Black', exit_rect, keretex)
        keretc = 2
        keretp = 2
        keretex = 2
    
        
        pygame.display.update()
        clock.tick(60)
if __name__ == "__main__":
    main()
