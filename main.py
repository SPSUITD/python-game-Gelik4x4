import pygame
from settings import *
from functions import load_image, load_level
from functions import Camera
from map import Map
from sprites import *


FPS = 30
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('CAT-LIFE')


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
    cat_sprites.empty()

    background = pygame.transform.scale(load_image('background.png'), SCREEN_SIZE)

    clock = pygame.time.Clock()
    camera = Camera()
    level = load_level(name_level)
    map = Map(screen, level)
    cat = map.get_cat()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_SPACE:
            #         cat.move_jump_right()
        if pygame.key.get_pressed()[pygame.K_d]:
            cat.move_right()
        if pygame.key.get_pressed()[pygame.K_a]:
            cat.move_left()
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            cat.move_jump_right()

        # camera.update(cat)
        # for sprite in all_sprites:
        #     camera.apply(sprite)
        tiles_sprites.update()
        screen.blit(background, (0, 0))
        tiles_sprites.draw(screen)
        cat.blit(screen)
        # screen.blit(load_image("sprites.png"), (0, 0))
        # cat_sprites.draw(screen)
        pygame.display.flip()
        # pygame.time.wait(5000)
        screen.fill(WHITE)
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