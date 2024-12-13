import pygame
from sprite_group_functions import all_sprites, backgound_sprites
from collide_functions import colliderect
from load_functions import load_image


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites, backgound_sprites)
        self.image = load_image('background.png')
        self.rect = self.image.get_rect(center=(0, 600))


class StaticSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__(all_sprites)
        self.image = load_image(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Coin(StaticSprite):
    def __init__(self, x, y):
        image = "crystal.png"
        super().__init__(image, x, y)
        self.point = 100


class Platform(pygame.sprite.Sprite):
    def __init__(self, size, position=(0, 0)):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(pygame.Color(0, 0, 255))
        self.rect = self.image.get_rect(topleft=position)


class Wall(pygame.sprite.Sprite):
    def __init__(self, size, position=(0, 0)):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(pygame.Color(0, 180, 0))
        self.rect = self.image.get_rect(topleft=position)


class DiePlatform(pygame.sprite.Sprite):
    def __init__(self, size, position=(0, 0)):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(pygame.Color(255, 0, 0))
        self.rect = self.image.get_rect(topleft=position)


class Finish(StaticSprite):
    def __init__(self, x, y):
        image = "finish.png"
        super().__init__(image, x, y)
