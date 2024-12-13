from constants import LOSE, WIN
from constants import GRAVITATION

from sprites import *
from tiles import *

from collide_functions import colliderect, colliderect_right, colliderect_left, colliderect_bottom
from load_functions import load_image, play_sound

from sprite_group_functions import *

from camera import Camera


class Board:
    def __init__(self, screen, cat, level):
        self.background = Background()
        self.screen = screen
        self.result_game = None
        self.cat = cat

        self.mice_info = MiceInfo()

        self.create_level(level)
        collision_objects.add(walls, platforms)
        self.camera = Camera(self.cat)

    def create_level(self, level):
        with open(f"data/map/{level}", 'r') as map_file:
            for string in map(str.strip, map_file.readlines()):
                if string and string[0] != '#':
                    name, *data = string.split()
                    if name == "StaticSprite":
                        name_file, x, y = data
                        x, y = int(x), int(y)
                        if name_file[-1] == 'b':
                            sprites_back.add(StaticSprite(f'art/{name_file}.png', x, y))
                        elif name_file[-1] == 'f':
                            sprites_front.add(StaticSprite(f'art/{name_file}.png', x, y))
                    elif name == "Wall":
                        width, height, x, y = map(int, data)
                        walls.add(Wall((width, height), (x, y)))
                    elif name == "Platform":
                        width, height, x, y = map(int, data)
                        platforms.add(Platform((width, height), (x, y)))
                    elif name == "DiePlatform":
                        width, height, x, y = map(int, data)
                        platforms.add(DiePlatform((width, height), (x, y)))
                    elif name == "Mouse":
                        x1, y1, x2, y2 = map(int, data)
                        mice_sprites.add(Mouse(x1, y1, x2, y2))
                        self.mice_info.add_mice()
                    elif name == "Coin":
                        x, y = map(int, data)
                        coins_sprites.add(Coin(x, y))
                    elif name == "Cat":
                        x, y = map(int, data)
                        self.cat.set_coords(x, y)
                    elif name == "Finish":
                        x, y = map(int, data)
                        finish_sprites.add(Finish(x, y))

    def update(self):
        if not self.cat.got_caught and not self.cat.climb_up:
            if not self.cat.on_ground:
                self.cat.velocity_y += GRAVITATION
            self.cat.rect.y += self.cat.velocity_y

        # Проверка коллизий с платформами
        self.cat.on_ground = False
        for platform in platforms:
            if colliderect(self.cat, platform) and not self.cat.climb_up:
                if self.cat.velocity_y > 0:  # Падение вниз
                    self.cat.rect.bottom = platform.rect.top
                    self.cat.velocity_y = 0
                    self.cat.on_ground = True
                elif self.cat.velocity_y < 0:  # Прыжок вверх
                    self.cat.rect.top = platform.rect.bottom
                    self.cat.velocity_y = 0
                # Конец игры если упал в пропасть
                if isinstance(platform, DiePlatform):
                    self.result_game = LOSE
        
        list_of_keys = pygame.key.get_pressed()

        for mouse in mice_sprites:
            mouse.move()
            if colliderect(self.cat, mouse):
                if list_of_keys[pygame.K_SPACE] and self.cat.velocity_y > 0:
                    play_sound("mouse_kill.mp3")
                    mouse.kill()
                    self.mice_info.minus_mice()
                    self.cat.collected_points += mouse.point
                elif not self.cat.jumped_away:
                    play_sound("cat_harm.mp3")
                    self.cat.jumped_away = True
                    self.index = 0
                    self.cat.velocity_y = 0
                    self.cat.hp.minus_hp()

        # Конец игры, если кончилась жизнь
        if self.cat.get_hp() <= 0:
            self.result_game = LOSE
        # Следующий уровень, если финиш
        for finish in finish_sprites:
            if colliderect(self.cat, finish) and self.mice_info.all_mice_killed():
                self.result_game = WIN

        if self.cat.jumped_away:
            self.cat.move_jumped_away()
        elif self.cat.got_caught:
            self.cat.move_got_caught_right()
            if (list_of_keys[pygame.K_d] or list_of_keys[pygame.K_a]) and self.cat.index >= 30:
                self.cat.climb_up = True
        elif self.cat.climb_up:
            self.cat.move_climb_up()
        elif any(list_of_keys):
            if list_of_keys[pygame.K_d] and not list_of_keys[pygame.K_SPACE]:
                self.cat.move_right()
                for platform in platforms:
                    if colliderect_right(self.cat, platform):
                        self.cat.got_caught = True
                        self.index = 0
                        self.cat.rect.topright = (platform.rect.left - 5, platform.rect.top - 20)
            if list_of_keys[pygame.K_a] and not list_of_keys[pygame.K_SPACE]:
                self.cat.move_left()
                for platform in platforms:
                    if colliderect_left(self.cat, platform):
                        self.cat.got_caught = True
                        self.index = 0
                        self.cat.rect.topleft = (platform.rect.right + 5, platform.rect.top - 20)
            if list_of_keys[pygame.K_SPACE] and not list_of_keys[pygame.K_a] and not list_of_keys[pygame.K_d]:
                self.cat.move_jump()
            if list_of_keys[pygame.K_d] and list_of_keys[pygame.K_SPACE]:
                self.cat.side_right = True
                self.cat.move_jump_into_distance()
                for platform in platforms:
                    if colliderect_right(self.cat, platform):
                        self.cat.got_caught = True
                        self.index = 0
                        self.cat.rect.topright = (platform.rect.left - 5, platform.rect.top - 20)
            if list_of_keys[pygame.K_a] and list_of_keys[pygame.K_SPACE]:
                self.cat.side_right = False
                self.cat.move_jump_into_distance()
                for platform in platforms:
                    if colliderect_left(self.cat, platform):
                        self.cat.got_caught = True
                        self.index = 0
                        self.cat.rect.topleft = (platform.rect.right + 5, platform.rect.top - 20)
            if list_of_keys[pygame.K_s]:
                self.cat.move_sit_down()
        else:
            if self.cat.velocity_y != 0:
                self.cat.fall()
            else:
                self.cat.stop()

        for coin in coins_sprites:
            if colliderect(self.cat, coin):
                play_sound("crystal.mp3")
                self.cat.collected_points += coin.point
                coin.kill()

    

        self.camera.update()
        for sprite in all_sprites:
            self.camera.apply(sprite)
        all_sprites.update()

        for obj in collision_objects:
            self.camera.apply(obj)
        collision_objects.draw(self.screen)


        backgound_sprites.draw(self.screen)
        sprites_back.draw(self.screen)
        cat_sprites.draw(self.screen)
        coins_sprites.draw(self.screen)
        finish_sprites.draw(self.screen)
        mice_sprites.draw(self.screen)
        sprites_front.draw(self.screen)
        not_camera_moved_sprites.draw(self.screen)
        self.mice_info.draw_count_of_mice(self.screen)

        # for obj in collision_objects:
        #     self.camera.apply(obj)
        # collision_objects.draw(self.screen)
