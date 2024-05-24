import pygame

from constants import SCREEN_SIZE, SCREEN_WIDTH, FPS
from constants import WHITE, BLACK
from constants import LOSE, WIN

from load_functions import load_image, play_sound
from sprite_group_functions import clear_groups_sprites
from sprite_group_functions import all_sprites, cat_sprites

from board import Board
from sprites import Cat


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
            if i == 1:
                play_sound("slash1.mp3")
            elif i == 12:
                play_sound("slash2.mp3")
            elif i == 25:
                play_sound("meow.mp3")
            background = pygame.transform.scale(load_image(f'start_screen/start{i}.jpg'), SCREEN_SIZE)
            i += 1

        screen.blit(background, (0, 0))
        pygame.display.flip()
        clock.tick(FPS // 1.8)
    return None


def game_screen(screen, cat, level):
    clock = pygame.time.Clock()

    clear_groups_sprites()
    all_sprites.add(cat)
    board = Board(screen, cat, level)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        board.update()
        if board.result_game is not None:
            running = False

        pygame.display.flip()
        clock.tick(FPS)

    return board.result_game


def points_screen(screen, cat, result_game):
    clock = pygame.time.Clock()
    font = pygame.font.Font("data/font/impact.ttf", 40)
    points_to_text = font.render(f"SCORE {cat.collected_points}", 1, WHITE) 

    if result_game == LOSE:
        image = 'lose.png' 
    elif result_game == WIN:
        image = 'win.png'

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return True

        screen.fill(BLACK)
        background = pygame.transform.scale(load_image(image), SCREEN_SIZE)
        screen.blit(background, (0, 0))
        screen.blit(points_to_text, (SCREEN_WIDTH // 2 - points_to_text.get_rect().width // 2, 496))
        pygame.display.flip()
        clock.tick(FPS)

    return False


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('CAT-LIFE')
    icon = load_image('icon.png')
    pygame.display.set_icon(icon)

    cat = Cat()
    number_of_level = 1
    game = start_screen(screen)
    pygame.mixer.music.load('data/sounds/back_music.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()
    while game:
        pygame.mixer.music.unpause()
        result_game = game_screen(screen, cat, f'level_{number_of_level}.txt')
        if result_game is None:
            pygame.mixer.music.pause()
            game =  False
        elif result_game == LOSE:
            pygame.mixer.music.pause()
            points_screen(screen, cat, result_game)
            cat_sprites.empty()
            cat = Cat()
            number_of_level = 1
            game = start_screen(screen)
        elif result_game == WIN:
            pygame.mixer.music.pause()
            points_screen(screen, cat, result_game)
            number_of_level = number_of_level + 1 if number_of_level != 2 else 1
        else:
            pygame.mixer.music.pause()
            game = False
        screen.fill(BLACK)
    pygame.quit()


if __name__ == "__main__":
    main()