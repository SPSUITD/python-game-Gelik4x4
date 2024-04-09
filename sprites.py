import pygame
import os
from settings import *
from functions import load_image, load_image_tile, load_sprite_sheet


all_sprites = pygame.sprite.Group()
sprites_back = pygame.sprite.Group()
sprites_middle = pygame.sprite.Group()
sprites_front = pygame.sprite.Group()
cat_sprites = pygame.sprite.Group()


# Класс для создания анимированных спрайтов
class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet_data, x, y):
        super().__init__(all_sprites)
        self.sprite_sheet = pygame.image.load(sprite_sheet_data['filename']).convert_alpha()
        self.image = self.sprite_sheet.subsurface(pygame.Rect(sprite_sheet_data['frames'][0]))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.frame_row = 0  # номер ряда фрейма, если несколько рядов фреймов в одном файле
        self.frame_index = 0
        self.animation_frames = sprite_sheet_data['frames']
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        # Обновляем анимацию
        self.frame_index += 1
        self.frame_index %= 24 # ToDO: поменять
        self.frame_index += self.frame_row * 24
        if self.frame_index >= len(self.animation_frames):
            self.frame_index = 0
        self.image = self.sprite_sheet.subsurface(pygame.Rect(self.animation_frames[self.frame_index]))
        self.mask = pygame.mask.from_surface(self.image)


class Cat(AnimatedSprite):
    def __init__(self, x, y):
        sprite_sheet_data = load_sprite_sheet("sprites.png", 100, 100)
        super().__init__(sprite_sheet_data, x, y)
        self.char = 'C'
        self.speed = 10
        self.side_right = True

    def move_right(self):
        self.frame_row = 1
        self.side_right = True
        self.rect.x += self.speed
        self.rect.y -= 5

    def move_left(self):
        self.frame_row = 1
        self.side_right = False
        self.rect.x -= self.speed
        self.rect.y -= 5
#
#     def move_jump(self):
#         self.index_frame = 2
#         self.cur_frame = (self.cur_frame + 1) % 24
#         if self.cur_frame < 5:
#             self.y += 0
#         elif self.cur_frame < 10:
#             self.y -= (40 + GRAVITATION)
#         elif self.cur_frame < 15:
#             self.y += 0
#         elif self.cur_frame < 20:
#             self.y += (20 - GRAVITATION)
#         else:
#             self.y += 0
#         # if self.side_right:
#         #     self.x += round(2.5 * self.speed)
#         # else:
#         #     self.x -= round(2.5 * self.speed)
#
    def stop(self):
        self.frame_row = 0


    # def update(self, dx, dy):
    #     self.x += dx
    #     self.y += dy


# Класс для создания статических спрайтов
class StaticSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__(all_sprites)
        fullname = os.path.join('images', image_path)
        self.image = pygame.image.load(fullname).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)


# class Tile(pygame.sprite.Sprite):
#     def __init__(self, i, j):
#         super().__init__(tiles_sprites, all_sprites)
#         self.image = load_image_tile(tile_images['unknown'])
#         self.rect = self.image.get_rect().move(TILE_WIDTH * j, TILE_HEIGHT * i)
#         self.char = '?'
#
#     def get_char(self):
#         return self.char
#
#     def __str__(self):
#         return self.char
#
#
# class Wall(Tile):
#     def __init__(self, i, j):
#         super().__init__(i, j)
#         self.image = load_image_tile(tile_images['wall'])
#         self.char = 'W'
#
# class Test(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super().__init__(tiles_sprites, all_sprites)
#         self.image = load_image(tile_images['wall2'])
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y