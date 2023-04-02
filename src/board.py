import random
import pygame
from sprites.tile import Tile


class Board:
    UP = (-1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    DOWN = (1, 0)

    DIRS = [UP, LEFT, RIGHT, DOWN]

    def __init__(self, size):
        self.tiles = pygame.sprite.Group()
        self.tiles_grid = []
        self.blank_coords = (size-1, size-1)

        self.all_sprites = pygame.sprite.Group()

        self.cell_size = 100
        self.size = size

        self._create_board()

    def update(self):
        self.tiles.update()

    def move(self, dir):
        y = self.blank_coords[0] + dir[0]
        x = self.blank_coords[1] + dir[1]
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            return
        self.tiles_grid[y][x].move()
        self.blank_coords = (y, x)

    def click(self, pos):
        for tile in self.tiles:
            if tile.rect.collidepoint(pos):
                if tile.move():
                    self.blank_coords = (tile.y, tile.x)

    def scramble(self):
        for _ in range(1000):
            dir = random.choice(self.DIRS)
            self.move(dir)

    def _create_board(self):
        for y in range(self.size):
            tiles_grid_row = []
            for x in range(self.size):
                number = (y * self.size + x + 1) % (self.size ** 2)

                tile = Tile(x, y, number)

                self.tiles.add(tile)
                tiles_grid_row.append(tile)
            self.tiles_grid.append(tiles_grid_row)

        for y in range(self.size):
            for x in range(self.size):
                tile = self.tiles_grid[y][x]
                if y > 0:
                    tile.add_neighbour(self.tiles_grid[y-1][x])
                if x > 0:
                    tile.add_neighbour(self.tiles_grid[y][x-1])

        self.all_sprites.add(self.tiles)
