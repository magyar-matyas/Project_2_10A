import pygame


def main() -> None:
    
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption('Hangman')
    clock = pygame.time.Clock()
    
    
    while True:
    
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

        pygame.display.update()
        clock.tick(60)
if __name__ == "__main__":
    main()
