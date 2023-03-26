from sprites.tile import Tile
import pygame
import random


class Board:
    def __init__(self, size):
        self.tiles = pygame.sprite.Group()
        self.tiles_grid = []

        self.all_sprites = pygame.sprite.Group()

        self.cell_size = 100
        self.size = size

        self._create_level()

    def update(self):
        self.tiles.update()

    def click(self, pos):
        for tile in self.tiles:
            if tile.rect.collidepoint(pos):
                tile.move()

    def scramble(self):
        tile = self.tiles_grid[3][2]
        for i in range(1000):
            tile.move()
            tile = random.choice(tile.neighbours)

    def _create_level(self):
        for y in range(self.size):
            tiles_grid_row = []
            for x in range(self.size):
                number = (y * self.size + x + 1) % (self.size ** 2)
                norm_x = x * self.cell_size
                norm_y = y * self.cell_size

                tile = Tile(norm_x, norm_y, number)

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
