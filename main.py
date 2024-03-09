from functions import load_level
from map import Map
from sprites import *


FPS = 30
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('CAT-LIFE')
bg_image = pygame.image.load('images/background.png')


def start_screen(screen):
    background = pygame.transform.scale(load_image('start_background.png'), SCREEN_SIZE)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return True

        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        pygame.display.flip()
        clock.tick(FPS)
    return None


def game_screen(screen, name_level):
    all_sprites.empty()
    tiles_sprites.empty()

    clock = pygame.time.Clock()
    level = load_level(name_level)
    map = Map(screen, level)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()
        screen.fill(BLACK)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)



def main():
    pygame.init()
    game = True
    while game:
        screen = pygame.display.set_mode(SCREEN_SIZE)
        if start_screen(screen) is not None:
            for i in range(1, 2):
                result_game = game_screen(screen, f'level {i}.txt')
        else:
            game = False
        screen.fill(BLACK)
    pygame.quit()


if __name__ == "__main__":
    main()