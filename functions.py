import os
import pygame
from settings import *

class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - SCREEN_WIDTH // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - SCREEN_HEIGHT // 2)


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