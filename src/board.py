import random
from copy import deepcopy


class Board:
    """ Handles game logic for the board

    Constants:
        UP, LEFT, RIGHT, DOWN: Tuples that act as unit vectors
            for board piece movement

    Attributes:
        numbers_grid: The board state in a grid
        blank_coords: Coordinates of the blank tile
        size: Side length of the board 
    """

    UP = (-1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    DOWN = (1, 0)

    DIRS = [UP, LEFT, RIGHT, DOWN]

    def __init__(self, size):
        self.numbers_grid = []
        self.blank_coords = (size-1, size-1)

        self.size = size

        self._create_board()

    def move(self, dir):
        blank_y = self.blank_coords[0]
        blank_x = self.blank_coords[1]
        y = blank_y + dir[0]
        x = blank_x + dir[1]
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            return False
        self.numbers_grid[blank_y][blank_x] = self.numbers_grid[y][x]
        self.numbers_grid[y][x] = 0
        self.blank_coords = (y, x)
        return True

    def scramble(self):
        for _ in range(100):
            dir = random.choice(self.DIRS)
            self.move(dir)

    def check_win(self):
        for y in range(self.size):
            for x in range(self.size):
                number = (y * self.size + x + 1) % (self.size ** 2)
                if self.numbers_grid[y][x] != number:
                    return False
        return True

    def simulate_move(self, dir):
        sim_board = deepcopy(self)
        if sim_board.move(dir):
            return sim_board
        return None

    def _create_board(self):
        for y in range(self.size):
            numbers_grid_row = []
            for x in range(self.size):
                number = (y * self.size + x + 1) % (self.size ** 2)
                numbers_grid_row.append(number)
            self.numbers_grid.append(numbers_grid_row)
