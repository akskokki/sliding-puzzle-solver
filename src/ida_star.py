from copy import deepcopy
from logger import Logger


class IDAStar:
    """ Implementation of the IDA* solving algorithm with
        Manhattan distance as the heuristic being used

    Constants:
        INFTY: Large number to emulate infinity in the algorithm

    Attributes:
        board: Board being used for game logic
    """
    INFTY = 99999

    def __init__(self, board, logger):
        self.board = board
        self.logger = logger

    def run(self):
        self.logger.reset()
        board_copy = deepcopy(self.board)
        bound = self.h_value(board_copy)
        moves = []
        while True:
            self.logger.set_bound(bound)
            t = self.search(0, board_copy, bound, moves)
            if t is True:
                print(f'Found solution of {len(moves)} moves')
                return moves
            if t == self.INFTY:
                return None
            bound = t

    def search(self, g, board_copy, bound, moves):
        self.logger.add_node()
        f = g + self.h_value(board_copy)
        if f > bound:
            return f
        if board_copy.check_win():
            return True
        minimum = self.INFTY

        for move in board_copy.DIRS:
            if len(moves) > 0 and (-move[0], -move[1]) == moves[-1]:
                continue

            if board_copy.move(move):
                moves.append(move)
                t = self.search(g + 1, board_copy, bound, moves)
                if t is True:
                    return True
                if t < minimum:
                    minimum = t
                board_copy.move((-move[0], -move[1]))
                moves.pop()

        return minimum

    def destination(self, number):
        x = (number - 1) % self.board.size
        y = (number - 1) // self.board.size
        return (x, y)

    def find_manhattan(self, x, y, number):
        (dest_x, dest_y) = self.destination(number)
        distance = abs(dest_x - x) + abs(dest_y - y)
        return distance

    def find_conflicts(self, numbers_grid, x, y, number):
        (dest_x, dest_y) = self.destination(number)
        conflicts = 0
        if y == dest_y:
            for k in range(x + 1, self.board.size - 1):
                other_number = numbers_grid[y][k]
                if other_number == 0:
                    continue
                (dest_x_other, dest_y_other) = self.destination(other_number)
                if dest_y_other == dest_y and dest_x_other <= dest_x:
                    conflicts += 1
        if x == dest_x:
            for k in range(y + 1, self.board.size - 1):
                other_number = numbers_grid[k][x]
                if other_number == 0:
                    continue
                (dest_x_other, dest_y_other) = self.destination(other_number)
                if dest_x_other == dest_x and dest_y_other <= dest_y:
                    conflicts += 1
        return conflicts

    def h_value(self, current_board):
        h = 0
        numbers_grid = current_board.numbers_grid
        for y in range(self.board.size):
            for x in range(self.board.size):
                number = numbers_grid[y][x]
                if number == 0:
                    continue
                h += self.find_manhattan(x, y, number)
                h += 2 * self.find_conflicts(numbers_grid, x, y, number)
        return h
