from sprites import *


class Map:
    def __init__(self, screen, level):
        self.screen = screen
        self.row_count = len(level)
        self.col_count = len(level[0])
        self.tiles_board = [[None for j in range(self.col_count)] for i in range(self.row_count)]
        self.objects_board = [[None for j in range(self.col_count)] for i in range(self.row_count)]
        self.cat = None

        for i in range(self.row_count):
            for j in range(self.col_count):
                if level[i][j] == 'W':
                    self.tiles_board[i][j] = Wall(i, j)

        for i in range(self.row_count):
            for j in range(self.col_count):
                if level[i][j] == 'C':
                    self.cat = Cat(i, j)
                    self.objects_board[i][j] = self.cat

    def get_object_char(self, i, j):
        return self.objects_board[i][j].get_char()

    def get_object(self, i, j):
        return self.objects_board[i][j]

    def set_object(self, i, j, obj):
        self.objects_board[i][j] = obj

    def get_tile_char(self, i, j):
        return self.tiles_board[i][j].get_char()

    def get_tile_object(self, i, j):
        return self.tiles_board[i][j]

    def set_tile(self, i, j, obj):
        self.tiles_board[i][j] = obj

    def get_cat(self):
        return self.cat
