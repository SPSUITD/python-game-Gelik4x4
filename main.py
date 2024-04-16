import pygame
from settings import *
from functions import load_image, load_level
from functions import Camera
from map import Map
from sprites import *


FPS = 60
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
    sprites_back.empty()
    sprites_middle.empty()
    sprites_front.empty()
    sprites_collade.empty()
    cat_sprites.empty()

    background = pygame.transform.scale(load_image('back.png'), SCREEN_SIZE)
    clock = pygame.time.Clock()
    level = load_level(name_level)
    map = Map(screen, level)
    # cat = map.get_cat()
    cat = Cat(0, 0)
    cat_sprites.add(cat)
    camera = Camera(cat)

    fall = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    cat.index = 0

        collade = False
        for sprite in sprites_middle:
            collade_object = pygame.sprite.collide_mask(cat, sprite)
            if collade_object:
                collade = True

        collade_2 = False
        for sprite in sprites_collade:
            collade_object = pygame.sprite.collide_mask(cat, sprite)
            if collade_object:
                collade_2 = collade_object

        if collade_2:
            cat.rect.x += 10
            # cat.stop()

        if collade:
            cat.rect.y += 0
        else:
            cat.rect.y += GRAVITATION

        if not fall:
            list_of_keys = pygame.key.get_pressed()
            if any(list_of_keys):
                if list_of_keys[pygame.K_d] and not list_of_keys[pygame.K_SPACE]:
                    cat.move_right()
                # else:
                #     cat.stop()
                #     print("rs")
            #         for cat in cat_sprites:
            #             collade_obj = pygame.sprite.spritecollideany(cat, tiles_sprites)
            #             if collade_obj and collade_obj.rect.left <= cat.rect.right <= collade_obj.rect.right and \
            #                     cat.rect.bottom >= collade_obj.rect.bottom:
            #                 cat.stop()
            #             else:
            #                 cat.move_right()
                if list_of_keys[pygame.K_a] and not list_of_keys[pygame.K_SPACE]:
                    cat.move_left()
                if list_of_keys[pygame.K_SPACE] and not list_of_keys[pygame.K_a] and not list_of_keys[pygame.K_d]:
                    cat.move_jump()
                if list_of_keys[pygame.K_d] and list_of_keys[pygame.K_SPACE]:
                    cat.side_right = True
                    cat.move_jump_into_distance()
                if list_of_keys[pygame.K_a] and list_of_keys[pygame.K_SPACE]:
                    cat.side_right = False
                    cat.move_jump_into_distance()
                if list_of_keys[pygame.K_s]:
                    cat.move_sit_down()
            else:
                cat.stop()

        camera.update()
        for sprite in all_sprites:
            camera.apply(sprite)

        all_sprites.update()

        screen.fill(WHITE)
        sprites_middle.draw(screen)
        sprites_collade.draw(screen)
        screen.blit(background, (0, 0))
        sprites_back.draw(screen)
        cat_sprites.draw(screen)
        sprites_front.draw(screen)

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