import pygame
SIZE = WIDTH, HEIGHT = 1200, 600
SCREEN = pygame.display.set_mode(SIZE)
TILE_SIZE = 40
FPS = 30
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('CAT-LIFE')
bg_image = pygame.image.load('images/background.png')

def main():
    walk_right = [
        pygame.image.load('sprites/right_1.png'),
        pygame.image.load('sprites/right_2.png'),
        pygame.image.load('sprites/right_3.png'),
        pygame.image.load('sprites/right_4.png'),
        pygame.image.load('sprites/right_5.png'),
        pygame.image.load('sprites/right_6.png'),
    ]
    an_count = 0
    pygame.init()
    game = True
    while game:
        SCREEN.blit(bg_image, (0, 0))
        SCREEN.blit(walk_right[an_count], (300, 300))
        if an_count == 5:
            an_count = 0
        else:
            an_count += 1
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()


if __name__ == "__main__":
    main()