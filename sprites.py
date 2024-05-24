import pygame

from constants import SCREEN_WIDTH, WHITE

from sprite_group_functions import all_sprites, cat_sprites, not_camera_moved_sprites
from sprite_group_functions import walls

from collide_functions import colliderect
from load_functions import load_image, load_sprite_sheet


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet_data, x, y):
        super().__init__(all_sprites)
        self.sprite_sheet = pygame.image.load(sprite_sheet_data['filename']).convert_alpha()
        self.image = self.sprite_sheet.subsurface(pygame.Rect(sprite_sheet_data['frames'][0]))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.frame_row = 0
        self.index = 0
        self.count_frame = 60
        self.side_right = True
        self.animation_frames = sprite_sheet_data['frames']
        self.mask = pygame.mask.from_surface(self.image)
        self.step_index = 1

    def update(self):
        """
        Обновление анимации
        """
        self.index += self.step_index
        self.index %= self.count_frame
        frame_index = self.index + self.frame_row * self.count_frame
        # if self.frame_index >= len(self.animation_frames):
        #     self.frame_index = 0
        self.image = self.sprite_sheet.subsurface(pygame.Rect(self.animation_frames[frame_index]))
        if not self.side_right:
            self.image = pygame.transform.flip(self.image, True, False)
        self.mask = pygame.mask.from_surface(self.image)

    def set_coords(self, x, y):
        self.rect.x = x
        self.rect.y = y


class Cat(AnimatedSprite):
    def __init__(self):
        sprite_sheet_data = load_sprite_sheet("sprites.png", 100, 100)
        super().__init__(sprite_sheet_data, 0, 0)
        cat_sprites.add(self)
        self.hp = HP()
        self.speed = 10
        self.collected_points = 0

        self.velocity_y = 0
        self.on_ground = False

        self.side_right = True
        self.got_caught = False
        self.climb_up = False
        self.jumped_away = False

    def move_got_caught_right(self):
        self.frame_row = 5
        self.velocity_y = 0
        if self.index == 58:
            self.got_caught = False

    def move_jumped_away(self):
        self.frame_row = 4
        self.rect.top -= 10
        self.climb_up = False
        self.got_caught = False   
        if self.side_right:
            self.rect.left -= 5
        else:
            self.rect.left += 5
        if self.index == 30:
            self.jumped_away = False

    def move_climb_up(self):
        self.frame_row = 6
        self.rect.top -= 1
        self.velocity_y = 0
        if self.index > 40:
            self.rect.top -= 1        
            if self.side_right:
                self.rect.left += 4
            else:
                self.rect.left -= 4
        if self.index == 58:
            self.climb_up = False
            self.index = 0

    def move_right(self):
        self.frame_row = 1
        self.side_right = True
        self.rect.x += self.speed
        self.check_collision(walls, self.speed, 0)

    def move_left(self):
        self.frame_row = 1
        self.side_right = False
        self.rect.x -= self.speed
        self.check_collision(walls, -self.speed, 0)

    def move_sit_down(self):
        self.frame_row = 3
        self.index = 0
        self.rect.x += 0

    def move_jump(self):
        if self.on_ground:
            self.velocity_y = -15
            self.on_ground = False
            self.index = 0
        self.frame_row = 3
        # self._jump(20)
        self.rect.x += 0

    def move_jump_into_distance(self):
        if self.on_ground:
            self.velocity_y = -10
            self.on_ground = False
            self.index = 0
        self.frame_row = 2
        power_speed = 1.5 * self.speed
        if self.side_right:
            self.rect.x += round(power_speed)
            self.check_collision(walls, power_speed, 0)
        else:
            self.rect.x -= round(power_speed)
            self.check_collision(walls, -power_speed, 0)

    def stop(self):
        self.frame_row = 0

    def fall(self):
        self.frame_row = 4

    def check_collision(self, walls, dx, dy):
        for wall in walls:
            if colliderect(self, wall):
                if dx > 0:
                    self.rect.right = wall.rect.left
                if dx < 0:
                    self.rect.left = wall.rect.right
                if dy > 0:
                    self.rect.bottom = wall.rect.top
                    self.on_ground = True
                    self.velocity_y = 0
                if dy < 0:
                    self.rect.top = wall.rect.bottom
                    self.velocity_y = 0

    def get_hp(self):
        return self.hp.count_of_hp


class Mouse(AnimatedSprite):
    def __init__(self, x1, y1, x2, y2):
        sprite_sheet_data = load_sprite_sheet("mouse.png", 60, 40)
        super().__init__(sprite_sheet_data, (x2 + x1) // 2, (y2 + y1) // 2)
        self.point = 50
        self.count_frame = 22;
        self.maximum_x = x2
        self.minimum_x = x1
        self.speed_x = 3

    def move(self):
        if self.rect.x < self.minimum_x or self.rect.x > self.maximum_x:
            self.speed_x *= -1
            self.side_right = not self.side_right
        self.rect.x += self.speed_x


class Life(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(not_camera_moved_sprites)
        self.image = load_image("hp_life.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class HP(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(not_camera_moved_sprites)
        self.image = load_image("hp_frame.png")
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 20
        self.count_of_hp = 9 
        self.helth = []
        for i in range(self.count_of_hp):
            self.helth.append(Life(self.rect.x + 3 + i * 25, self.rect.y + 2))

    def minus_hp(self):
        self.count_of_hp -= 1
        hp = self.helth.pop()
        hp.kill()

    def get_gount_of_hp(self):
        return self.count_of_hp


class MiceInfo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(not_camera_moved_sprites)
        self.image = load_image("mice_left.png")
        self.rect = self.image.get_rect()
        self.rect.right = SCREEN_WIDTH - 110
        self.rect.y = 25

        self.font = pygame.font.Font("data/font/impact.ttf", 35)

        self.count_of_mice = 0
        self.max_count_of_mice = 0

    def add_mice(self):
        self.max_count_of_mice += 1

    def minus_mice(self):
        self.count_of_mice += 1

    def get_count_of_mice(self):
        return self.count_of_mice

    def all_mice_killed(self):
        return self.count_of_mice == self.max_count_of_mice

    def draw_count_of_mice(self, screen):
        points_to_text = self.font.render(f"{self.count_of_mice} / {self.max_count_of_mice}", 1, WHITE) 
        screen.blit(points_to_text, (SCREEN_WIDTH - 100, 25))



