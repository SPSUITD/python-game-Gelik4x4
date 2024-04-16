from sprites import *


class Map:
    def __init__(self, screen, level):
        self.screen = screen
        sprites_back.add(StaticSprite('rock2_b.png', 0, 200))
        sprites_middle.add(StaticSprite('rock2_m.png', 0, 200))
        sprites_collade.add(StaticSprite('rock2_collade.png', 0, 200))
        sprites_back.add(StaticSprite('rock3_b.png', 899, 300))
        sprites_middle.add(StaticSprite('rock3_m.png', 899, 300))
        sprites_front.add(StaticSprite('rock3_f.png', 899, 300))
        sprites_back.add(StaticSprite('rock4_b.png', 899 + 300, 400))
        sprites_middle.add(StaticSprite('rock4_m.png', 899 + 300, 400))
        sprites_front.add(StaticSprite('rock4_f.png', 899 + 300, 400))
        sprites_back.add(StaticSprite('house_b.png', 899 + 300 + 200, 200))
        sprites_middle.add(StaticSprite('house_m.png', 899 + 300 + 200, 200))
        sprites_front.add(StaticSprite('house_f.png', 899 + 300 + 200, 200))
