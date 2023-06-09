from copy import deepcopy


class IDAStar:
    """
    Implementation of the IDA* solving algorithm for the puzzle with
    Walking distance (Manhattan with linear conflict resolution)
    as the heuristic being used

    Constants:
        INFTY: Large number to emulate infinity in the algorithm

    Attributes:
        board: Board being used for game logic
        logger: Logger object to report the search progress to terminal
        timeout: Time (seconds) until solver times out
    """
    INFTY = 99999

    def __init__(self, board, logger, timeout=-1):
        """
        Class constructor

        Args:
            board: Board object
            logger: Logger object
            timeout: Time (seconds) until solver times out
        """
        self.board = board
        self.logger = logger
        self.timeout = timeout

    def run(self):
        """
        Starts the solving algorithm

        Returns:
            moves (List): List of moves to reach solution
            None: Solution not found
        """
        print(f'\nStarting configuration: {self.board.numbers_grid}')
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
            if t is False:
                print(f'No solution found in {self.timeout} seconds')
                return None
            if t == self.INFTY:
                return None
            bound = t

    def search(self, g, board_copy, bound, moves):
        """
        Recursive part of search algorithm

        Args:
            g: Distance from starting node
            board_copy: Copy of the board created for the search
            bound: Current bound of the IDA* search
            moves: Current list of moves

        Returns:
            f or minimum (int): Value of f exceeds bound
            True: Win state has been reached
            False: Solver timed out
        """
        elapsed_time = self.logger.add_node()
        if self.timeout > 0 and elapsed_time > self.timeout:
            return False
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
                if t is False:
                    return False
                if t < minimum:
                    minimum = t
                board_copy.move((-move[0], -move[1]))
                moves.pop()

        return minimum

    def destination(self, number):
        """
        Finds the win-state destination of a specific tile on the board

        Args:
            number: Number of the tile

        Returns:
            (x, y) (tuple): Destination coordinates
        """
        x = (number - 1) % self.board.size
        y = (number - 1) // self.board.size
        return (x, y)

    def find_manhattan(self, x, y, number):
        """
        Finds Manhattan distance of tile from specific coordinates to
        the win state

        Args:
            x, y: Coordinates of the tile
            number: Number of the tile

        Returns:
            distance (int): Manhattan distance calculated
        """
        (dest_x, dest_y) = self.destination(number)
        distance = abs(dest_x - x) + abs(dest_y - y)
        return distance

    def find_conflicts(self, numbers_grid, x, y, number):
        """
        Finds the amount of linear conflicts to the right and
        below a specific tile on the board

        Args:
            numbers_grid: 2D array representation of the board
            x, y: Coordinates of the tile
            number: Number of the tile

        Returns:
            conflicts (int): Total conflicts to the right or below this tile
        """
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
        """
        Total heuristic value of a specific board state
        (Manhattan distance + Linear conflicts)

        Args:
            current_board: Board object to calculate the heuristic for

        Returns:
            h (int): Total heuristic value of this board state
        """
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
