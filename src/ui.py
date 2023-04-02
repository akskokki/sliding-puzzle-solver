import pygame
from sprites.tile import Tile


class UI:
    def __init__(self, board):
        self.board = board
        self.tiles = pygame.sprite.Group()
        self.tiles_grid = []
        self.create_tiles(board)

    def update(self):
        for tile in self.tiles:
            tile.number = self.board.numbers_grid[tile.y][tile.x]
        self.tiles.update()

    # def click(self, pos):
    #     for tile in self.tiles:
    #         if tile.rect.collidepoint(pos):

    def create_tiles(self, board):
        for y in range(self.board.size):
            tiles_grid_row = []
            for x in range(self.board.size):
                number = self.board.numbers_grid[y][x]
                tile = Tile(x, y, number)
                self.tiles.add(tile)
                tiles_grid_row.append(tile)
            self.tiles_grid.append(tiles_grid_row)
