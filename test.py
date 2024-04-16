import pygame
import sys

# Инициализация Pygame
pygame.init()

# Устанавливаем размеры окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Collision Detection with Animated and Static Sprites")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Класс для создания анимированных спрайтов
class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet_data):
        super().__init__()
        self.sprite_sheet = pygame.image.load(sprite_sheet_data['filename']).convert_alpha()
        self.image = self.sprite_sheet.subsurface(pygame.Rect(sprite_sheet_data['frames'][0]))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 200
        self.frame_index = 0
        self.animation_frames = sprite_sheet_data['frames']
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        # Обновляем анимацию
        self.frame_index += 0
        if self.frame_index >= len(self.animation_frames):
            self.frame_index = 0
        self.image = self.sprite_sheet.subsurface(pygame.Rect(self.animation_frames[self.frame_index]))
        self.mask = pygame.mask.from_surface(self.image)

    def move(self, dx, dy):
        # Двигаем спрайт
        self.rect.x += dx
        self.rect.y += dy


# Класс для создания статических спрайтов
class StaticSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)


# Функция для загрузки данных анимации из файла
def load_sprite_sheet(filename, frame_width, frame_height):
    sprite_sheet = pygame.image.load(filename).convert_alpha()
    frames = []
    for y in range(0, sprite_sheet.get_height(), frame_height):
        for x in range(0, sprite_sheet.get_width(), frame_width):
            frames.append((x, y, frame_width, frame_height))
    return {'filename': filename, 'frames': frames}


# Создаем анимированный спрайт
sprite_sheet_data = load_sprite_sheet('images/sprites.png', 100, 100)
animated_sprite = AnimatedSprite(sprite_sheet_data)

# Создаем статический спрайт
static_sprite = StaticSprite('images/block.png', 300, 100)
static_sprite_2 = StaticSprite('images/block.png', 300, 140)

# Группа спрайтов
all_sprites = pygame.sprite.Group()
all_sprites.add(static_sprite, animated_sprite, static_sprite_2)

# Управление FPS
clock = pygame.time.Clock()
FPS = 60

# Скорость перемещения спрайта
SPEED = 5

# Главный игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление движением анимированного спрайта
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        animated_sprite.move(-SPEED, 0)
    if keys[pygame.K_RIGHT]:
        animated_sprite.move(SPEED, 0)
    if keys[pygame.K_UP]:
        animated_sprite.move(0, -SPEED)
    if keys[pygame.K_DOWN]:
        animated_sprite.move(0, SPEED)

    # Обновляем анимированный спрайт
    animated_sprite.update()

    # Проверяем коллизию по маске спрайтов
    if pygame.sprite.collide_mask(animated_sprite, static_sprite):
        print("Collision Occurred!")

    # Очищаем экран
    screen.fill(BLACK)

    # Рисуем спрайты на экране
    all_sprites.draw(screen)

    pygame.display.flip()

    # Ограничение FPS
    clock.tick(FPS)

# Выход из игры
pygame.quit()
sys.exit()