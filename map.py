from sprites import *


class Map:
    def __init__(self, screen, level):
        self.screen = screen
        self.row_count = len(level)
        self.col_count = len(level[0])
        self.tiles_board = [[None for j in range(self.col_count)] for i in range(self.row_count)]

        for i in range(self.row_count):
            for j in range(self.col_count):
                if level[i][j] == 'W':
                    self.tiles_board[i][j] = Wall(i, j)

    def get_tile_char(self, i, j):
        return self.tiles_board[i][j].get_char()

    def get_tile_object(self, i, j):
        return self.tiles_board[i][j]

    def set_tile(self, i, j, obj):
        self.tiles_board[i][j] = obj
