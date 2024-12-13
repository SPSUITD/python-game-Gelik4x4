from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from sprites import Mouse
from tiles import Background


class Camera:
    def __init__(self, target):
        self.dx = 0
        self.dy = 0
        self.target = target  # target is Cat

    def apply(self, obj):
        """
        Применить сдвиг к объекту
        """
        if not isinstance(obj, Background):
            obj.rect.x += self.dx
            obj.rect.y += self.dy
        else:
            obj.rect.x += self.dx // 5
            obj.rect.y += self.dy // 4
        # Если объект сдвига мышь, то также сдвигаем отклонение
        if isinstance(obj, Mouse):
            obj.maximum_x += self.dx
            obj.minimum_x += self.dx

    def update(self):
        """
        Определить сдвиг относительно объекта Cat
        """
        if self.target:
            self.dx = -(self.target.rect.x + self.target.rect.w / 2 - SCREEN_WIDTH / 2)
            # Определяем, находится ли персонаж ближе к верхней или нижней границе экрана
            if self.target.rect.y + self.target.rect.h / 2 < SCREEN_HEIGHT / 4:  # Ближе к верхней границе
                self.dy = -(self.target.rect.y + self.target.rect.h / 2 - SCREEN_HEIGHT / 4)
            elif self.target.rect.y + self.target.rect.h / 2 > SCREEN_HEIGHT * 3 / 4:  # Ближе к нижней границе
                self.dy = -(self.target.rect.y + self.target.rect.h / 2 - SCREEN_HEIGHT * 3 / 4)
            else:
                self.dy = 0
