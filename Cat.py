import pygame

class Cat:
    def __init__(self, x, y):
        cat = pygame.image.load('sprites/right_1.png')
        self.image = pygame.transform.scale(cat, (100, 100))
