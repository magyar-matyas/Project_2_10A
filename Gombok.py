import pygame
pygame.font.init()

my_font = pygame.font.SysFont("Comic Sans MS", 30)

class Gombok:
     
    
    def __init__(self, betu: str) -> None:
        self.betu = betu
        self.surf = my_font.render(betu, False, (255, 255, 255))
        self.value = 1
        self.rect = self.surf.get_rect(midleft = (0,0))