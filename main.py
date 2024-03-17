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
    clock = pygame.time.Clock()
    running = True
    i = 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return True

        screen.fill(BLACK)
        if i <= 52:
            background = pygame.transform.scale(load_image(f'start{i}.jpg'), SCREEN_SIZE)
            i += 1

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
    time_fall = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_SPACE:
            #         cat.move_jump_right()
        list_of_keys = pygame.key.get_pressed()

        # print(cat.rect)
        if any(list_of_keys):
            if list_of_keys[pygame.K_d]:
                for cat in cat_sprites:
                    collade_obj = pygame.sprite.spritecollideany(cat, tiles_sprites)
                    if collade_obj and collade_obj.rect.left <= cat.rect.right <= collade_obj.rect.right and \
                             cat.rect.bottom >= collade_obj.rect.bottom:
                        cat.stop()
                    else:
                        cat.move_right()
            if list_of_keys[pygame.K_a]:
                for cat in cat_sprites:
                    collade_obj = pygame.sprite.spritecollideany(cat, tiles_sprites)
                    if collade_obj and collade_obj.rect.left <= cat.rect.left <= collade_obj.rect.right and \
                             cat.rect.bottom >= collade_obj.rect.bottom:
                        cat.stop()
                    else:
                        cat.move_left()
            if list_of_keys[pygame.K_SPACE]:
                cat.move_jump()
                if time_fall is None:
                    time_fall = pygame.time.get_ticks() + 400
                elif pygame.time.get_ticks() > time_fall:
                    cat.stop()
        else:
            time_fall = None
            cat.stop()

        for cat in cat_sprites:
            collade_obj = pygame.sprite.spritecollideany(cat, tiles_sprites)
            if collade_obj and collade_obj.rect.top <= cat.rect.bottom:
                cat.y += 0
            else:
                cat.y += 20
        # camera.update(cat)
        # for sprite in all_sprites:
        #     camera.apply(sprite)
        tiles_sprites.update()
        # screen.blit(background, (0, 0))
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