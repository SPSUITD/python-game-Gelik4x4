import pygame
import sys

# Константы
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PLAYER_SIZE = (50, 50)
PLATFORM_SIZE = (200, 20)
WALL_SIZE = (20, 100)
GRAVITY = 0.5
JUMP_STRENGTH = -10
MOVE_SPEED = 5

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Инициализация Pygame
pygame.init()

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jump and Move")

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(PLAYER_SIZE)
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.topleft = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - PLAYER_SIZE[1])
        self.velocity_y = 0
        self.on_ground = False

    def update(self, platforms, walls):
        keys = pygame.key.get_pressed()

        # Движение влево и вправо
        if keys[pygame.K_LEFT]:
            self.rect.x -= MOVE_SPEED
            self.check_collision(walls, -MOVE_SPEED, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.x += MOVE_SPEED
            self.check_collision(walls, MOVE_SPEED, 0)

        # Гравитация
        if not self.on_ground:
            self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        # Проверка коллизий с платформами
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_y > 0:  # Падение вниз
                    self.rect.bottom = platform.rect.top
                    self.velocity_y = 0
                    self.on_ground = True
                elif self.velocity_y < 0:  # Прыжок вверх
                    self.rect.top = platform.rect.bottom
                    self.velocity_y = 0


    def jump(self):
        if self.on_ground:
            self.velocity_y = JUMP_STRENGTH
            self.on_ground = False

    def check_collision(self, walls, dx, dy):
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:  # Движение вправо; удар слева стены
                    self.rect.right = wall.rect.left
                if dx < 0:  # Движение влево; удар справа стены
                    self.rect.left = wall.rect.right
                if dy > 0:  # Движение вниз; удар сверху стены
                    self.rect.bottom = wall.rect.top
                    self.on_ground = True
                    self.velocity_y = 0
                if dy < 0:  # Движение вверх; удар снизу стены
                    self.rect.top = wall.rect.bottom
                    self.velocity_y = 0

# Класс платформы
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface(PLATFORM_SIZE)
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(topleft=(x, y))

# Класс стены
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface(WALL_SIZE)
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(topleft=(x, y))

# Создание игрока
player = Player()

# Создание платформ
platforms = pygame.sprite.Group()
platforms.add(Platform(200, 500))
platforms.add(Platform(400, 400))
platforms.add(Platform(100, 300))

# Создание стен
walls = pygame.sprite.Group()
walls.add(Wall(150, 450))
walls.add(Wall(350, 350))
walls.add(Wall(250, 250))

# Группа всех спрайтов
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(platforms)
all_sprites.add(walls)

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

    # Обновление спрайтов
    player.update(platforms, walls)
    platforms.update()
    walls.update()

    # Очистка экрана
    screen.fill(WHITE)

    # Отрисовка спрайтов
    all_sprites.draw(screen)

    # Обновление экрана
    pygame.display.flip()

    # Задержка для ограничения кадров
    pygame.time.Clock().tick(60)

# Завершение Pygame
pygame.quit()
sys.exit()
