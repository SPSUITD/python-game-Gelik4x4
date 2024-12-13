import pygame


def colliderect(self, other):
    """
    Проверка пересечения self и other
    """
    return self.rect.left < other.rect.right and \
           self.rect.right > other.rect.left and \
           self.rect.top < other.rect.bottom and \
           self.rect.bottom > other.rect.top


def colliderect_right(self, other):
    """
    Проверка пересечения правого края self с левым краем other
    """
    return self.rect.right > other.rect.left and \
           self.rect.left < other.rect.left and \
           self.rect.top < other.rect.bottom and \
           self.rect.bottom > other.rect.top


def colliderect_left(self, other):
    """
    Проверка пересечения левого края self с правым краем other
    """
    return self.rect.left < other.rect.right and \
           self.rect.right > other.rect.right and \
           self.rect.top < other.rect.bottom and \
           self.rect.bottom > other.rect.top


def colliderect_bottom(self, other):
    """
    Проверка пересечения нижнего края self с с серединой верхним края other
    """
    return self.rect.bottom >= other.rect.top and \
           self.rect.left < other.rect.left
