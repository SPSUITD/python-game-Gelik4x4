import os
import pygame
from settings import *

class Camera:
    def __init__(self, target):
        self.x = 0
        self.y = 0
        self.target = target
        self.smoothing_factor = 0.5  # Фактор сглаживания (0.1 = 10% скорости)

    def apply(self, obj):
        obj.rect.x += self.x
        obj.rect.y += self.y

    def update(self):
        if self.target:
            target_x = -(self.target.rect.x + self.target.rect.w / 2 - SCREEN_WIDTH / 2)
            target_y = -(self.target.rect.y + self.target.rect.h / 2 - SCREEN_HEIGHT / 2)
            self.x = self.x * (1 - self.smoothing_factor) + target_x * self.smoothing_factor
            self.y = self.y * (1 - self.smoothing_factor) + target_y * self.smoothing_factor


def load_level(filename):
    fullname = os.path.join('data', filename)
    with open(fullname, 'r') as map_file:
        level_map = [line.strip() for line in map_file]
    max_width = max(map(len, level_map))
    return list(map(lambda x: list(x.ljust(max_width, 'W')), level_map))


def load_image(filename):
    fullname = os.path.join('images', filename)
    image = pygame.image.load(fullname)
    return image


def load_image_tile(tile_image):
    image = load_image(tile_image)
    return pygame.transform.scale(image, (TILE_WIDTH, TILE_HEIGHT))


# Функция для загрузки данных анимации из файла
def load_sprite_sheet(filename, frame_width, frame_height):
    fullname = os.path.join('images', filename)
    sprite_sheet = pygame.image.load(fullname).convert_alpha()
    frames = []
    for y in range(0, sprite_sheet.get_height(), frame_height):
        for x in range(0, sprite_sheet.get_width(), frame_width):
            frames.append((x, y, frame_width, frame_height))
    return {'filename': fullname, 'frames': frames}