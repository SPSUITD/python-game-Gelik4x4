import pygame
from settings import *
from functions import load_image, load_image_tile


all_sprites = pygame.sprite.Group()
tiles_sprites = pygame.sprite.Group()
cat_sprites = pygame.sprite.Group()

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(cat_sprites, all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns, sheet.get_height() // rows)
        for i in range(rows):
            self.frames.append([])
            for j in range(columns):
                frame_location = (self.rect.w * j, self.rect.h * i)
                self.frames[i].append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


class Cat(AnimatedSprite):
    def __init__(self, i, j):
        sheet = load_image("sprites.png")
        columns, rows = 6, 3
        self.i, self.j = i, j
        self.x, self.y = j * CELL_SIZE, i * CELL_SIZE
        super().__init__(sheet, columns, rows, self.x, self.y)
        self.index_frame = 0
        self.char = 'C'
        self.speed = 10

    def blit(self, screen):
        image = self.frames[self.index_frame][self.cur_frame]
        #self.image = pygame.transform.scale(image, (TILE_WIDTH, TILE_HEIGHT))
        screen.blit(image, (self.x, self.y))

    def get_i_and_j(self):
        return self.i, self.j

    def get_coords(self):
        return self.x, self.y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def move_right(self):
        self.index_frame = 0
        self.cur_frame = (self.cur_frame + 1) % 6
        self.x += self.speed

    def move_left(self):
        self.index_frame = 1
        self.cur_frame = (self.cur_frame + 1) % 6
        self.x -= self.speed

    def move_jump_right(self):
        self.index_frame = 2
        self.cur_frame = 3
        self.x += self.speed

    # def update(self):
    #     index_frame = 0
    #     self.cur_frame = 0
    #     image = self.frames[index_frame][self.cur_frame]
    #     self.image = pygame.transform.scale(image, (TILE_WIDTH, TILE_HEIGHT))

    def get_char(self):
        return self.char

    def __str__(self):
        return self.char


class Tile(pygame.sprite.Sprite):
    def __init__(self, i, j):
        super().__init__(tiles_sprites, all_sprites)
        self.image = load_image_tile(tile_images['unknown'])
        self.rect = self.image.get_rect().move(TILE_WIDTH * j, TILE_HEIGHT * i)
        self.char = '?'

    def get_char(self):
        return self.char

    def __str__(self):
        return self.char


class Wall(Tile):
    def __init__(self, i, j):
        super().__init__(i, j)
        self.image = load_image_tile(tile_images['wall'])
        self.char = 'W'
