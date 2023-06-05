import pygame

class Corpses:
    
    def __init__(self, szint) -> None:
        self.kirajz = []
        self.kirajz.append(pygame.Surface((40, 430)))
        self.kirajz.append(pygame.Surface((300, 40)))
        self.kirajz.append(pygame.Surface((1,1)))
        self.kirajz.append(pygame.image.load(f'akasztottak/lvl{szint}/h0.png'))
        self.kirajz.append(pygame.image.load(f'akasztottak/lvl{szint}/h1.png'))
        self.kirajz.append(pygame.image.load(f'akasztottak/lvl{szint}/h2.png'))
        self.kirajz.append(pygame.image.load(f'akasztottak/lvl{szint}/h3.png'))
        self.kirajz.append(pygame.image.load(f'akasztottak/lvl{szint}/h4.png'))
        self.kirajz.append(pygame.image.load(f'akasztottak/lvl{szint}/h5.png'))
        self.kirajz.append(pygame.image.load(f'akasztottak/lvl{szint}/h6.png'))
        self.kirajz.append(pygame.image.load(f'akasztottak/lvl{szint}/h7.png'))
        self.kirajz.append(pygame.image.load(f'akasztottak/lvl{szint}/h8.png'))
        
     