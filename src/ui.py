import pygame
from sprites.tile import Tile


class UI:
    """
    Handles the Pygame Sprites in the UI

    Attributes:
        board: Board for game logic
        tiles: Pygame Group of tile sprites
        tiles_grid: Tile sprites assembled in a grid
    """

    def __init__(self, board):
        """
        Class constructor

        Args:
            board: Board object used for the current game
        """
        self.board = board
        self.tiles = pygame.sprite.Group()
        self.tiles_grid = []
        self.create_tiles()

    def update(self):
        """Performs pygame updates for all tiles"""
        for tile in self.tiles:
            tile.number = self.board.numbers_grid[tile.y][tile.x]
        self.tiles.update()

    # def click(self, pos):
    #     for tile in self.tiles:
    #         if tile.rect.collidepoint(pos):

    def create_tiles(self):
        """Creates the initial tiles based on the values of the board"""
        for y in range(self.board.size):
            tiles_grid_row = []
            for x in range(self.board.size):
                number = self.board.numbers_grid[y][x]
                tile = Tile(x, y, number)
                self.tiles.add(tile)
                tiles_grid_row.append(tile)
            self.tiles_grid.append(tiles_grid_row)
