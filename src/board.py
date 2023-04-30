import random
from copy import deepcopy


class Board:
    """
    Handles game logic for the board

    Constants:
        UP, LEFT, RIGHT, DOWN: Tuples that act as unit vectors
            for board piece movement

    Attributes:
        numbers_grid: The board state in a grid
        win_state: A grid of the win state of the board
        blank_coords: Coordinates of the blank tile
        size: Side length of the board 
    """

    UP = (-1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    DOWN = (1, 0)

    DIRS = [UP, LEFT, RIGHT, DOWN]

    def __init__(self, size):
        """
        Class constructor

        Args:
            size: Size of puzzle grid
        """
        self.numbers_grid = []
        self.win_state = []

        self.blank_coords = (size-1, size-1)

        self.size = size

        self._create_board()

    def move(self, direction):
        """
        Moves the blank space in a direction if possible

        Args:
            direction: Direction constant from DIRS

        Returns:
            True: Valid movement
            False: Invalid movement
        """
        blank_y = self.blank_coords[0]
        blank_x = self.blank_coords[1]
        y = blank_y + direction[0]
        x = blank_x + direction[1]
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            return False
        self.numbers_grid[blank_y][blank_x] = self.numbers_grid[y][x]
        self.numbers_grid[y][x] = 0
        self.blank_coords = (y, x)
        return True

    def scramble(self):
        """Scrambles the board by 100 moves"""
        for _ in range(100):
            direction = random.choice(self.DIRS)
            while not self.move(direction):
                direction = random.choice(self.DIRS)

    def check_win(self):
        """
        Checks if the win state has been reached

        Returns:
            True: Game is in solved state
            False: Game is not in solved state
        """
        for y in range(self.size):
            for x in range(self.size):
                if self.numbers_grid[y][x] != self.win_state[y][x]:
                    return False
        return True

    def _create_board(self):
        """Creates the initial board"""
        for y in range(self.size):
            numbers_grid_row = []
            for x in range(self.size):
                number = (y * self.size + x + 1) % (self.size ** 2)
                numbers_grid_row.append(number)
            self.numbers_grid.append(numbers_grid_row)
            self.win_state.append(deepcopy(numbers_grid_row))
