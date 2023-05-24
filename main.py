import pygame
import imp
from sys import exit
import pygame.font

pygame.init()


def main() -> None:
    
    my_font = pygame.font.SysFont("Comic Sans MS", 30)
    
    #pygame
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption('Hangman')
    clock = pygame.time.Clock()
    
    
    
    #surfaces
    
    fokepernyo_surf = pygame.Surface((1200,600))
    # fokepernyo_surf.fill((255,255,255))
    fokepernyo_rect = fokepernyo_surf.get_rect(topleft =(0,0))

    play_surf = my_font.render('Play',False, (255,255,255) )
    play_surf = pygame.transform.scale(play_surf, (180,70))
    play_rect = play_surf.get_rect(midleft= (150, 300))

    custom_surf = my_font.render('Custom',False, (255,255,255) )
    custom_surf = pygame.transform.scale(custom_surf, (180,70))
    custom_rect = custom_surf.get_rect(midleft= (150, 400))
    
    while True:
    
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


        screen.blit(fokepernyo_surf, fokepernyo_rect)
        screen.blit(play_surf, play_rect)
        pygame.draw.rect(screen, 'White', play_rect, 2)
        screen.blit(custom_surf, custom_rect)
        pygame.draw.rect(screen, 'White', custom_rect, 2)
        
        
        pygame.display.update()
        clock.tick(60)
if __name__ == "__main__":
    main()
