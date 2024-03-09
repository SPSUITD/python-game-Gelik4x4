import os
import pygame


def load_level(filename):
    fullname = os.path.join('data', filename)
    with open(fullname, 'r') as map_file:
        level_map = [line.strip() for line in map_file]
    max_width = max(map(len, level_map))
    return list(map(lambda x: list(x.ljust(max_width, 'W')), level_map))


def load_image(filename):
    fullname = os.path.join('images', filename)
    image = pygame.image.load(fullname).convert()
    image = image.convert_alpha()
    return image