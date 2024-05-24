import pygame


all_sprites = pygame.sprite.Group()
sprites_back = pygame.sprite.Group()
sprites_front = pygame.sprite.Group()

walls = pygame.sprite.Group()
platforms = pygame.sprite.Group()
collision_objects = pygame.sprite.Group()

cat_sprites = pygame.sprite.Group()
mice_sprites = pygame.sprite.Group()
coins_sprites = pygame.sprite.Group()

not_camera_moved_sprites = pygame.sprite.Group()
finish_sprites = pygame.sprite.Group()
backgound_sprites = pygame.sprite.Group()


def clear_groups_sprites():
    """
    Очистка группы спрайтов, кроме cat_sprites, not_camera_moved_sprites 
    """
    all_sprites.empty()
    sprites_back.empty()
    sprites_front.empty()

    walls.empty()
    platforms.empty()
    collision_objects.empty()

    mice_sprites.empty()
    coins_sprites.empty()
    finish_sprites.empty()
