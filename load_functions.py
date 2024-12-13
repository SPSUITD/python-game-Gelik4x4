import os
import pygame


def load_image(filename):
    """
    Функция для загрузки картинок из файла
    """
    fullname = os.path.join('data/images', filename)
    image = pygame.image.load(fullname).convert_alpha()
    return image


def load_sprite_sheet(filename, frame_width, frame_height):
    """
    Функция для загрузки данных анимации из файла
    """
    fullname = os.path.join('data/images', filename)
    sprite_sheet = pygame.image.load(fullname).convert_alpha()
    frames = []
    for y in range(0, sprite_sheet.get_height(), frame_height):
        for x in range(0, sprite_sheet.get_width(), frame_width):
            frames.append((x, y, frame_width, frame_height))
    return {'filename': fullname, 'frames': frames}


def play_sound(filename):
    """
    Функция для проигрывания звука
    """
    fullname = os.path.join('data/sounds', filename)
    sound = pygame.mixer.Sound(fullname)
    sound.set_volume(0.2)
    sound.play()
