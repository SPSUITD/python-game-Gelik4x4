import pygame
from settings import *
from functions import load_image


all_sprites = pygame.sprite.Group()
tiles_sprites = pygame.sprite.Group()


class Cat:
    def __init__(self, x, y):
        cat = pygame.image.load('images/sprites.png')
        self.image = pygame.transform.scale(cat, (100, 100))


class Tile(pygame.sprite.Sprite):
    def __init__(self, i, j):
        super().__init__(tiles_sprites, all_sprites)
        self.image = load_image(tile_images['unknown'])
        self.rect = self.image.get_rect().move(TILE_WIDTH * j, TILE_HEIGHT * i)
        self.char = '?'

    def get_char(self):
        return self.char

    def __str__(self):
        return self.char


class Wall(Tile):
    def __init__(self, i, j):
        super().__init__(i, j)
        self.image = load_image(tile_images['wall'])
        self.char = 'W'
