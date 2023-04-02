class IDAStar:
    """ Implementation of the IDA* solving algorithm with
        Manhattan distance as the heuristic being used

    Constants:
        INFTY: Large number to emulate infinity in the algorithm

    Attributes:
        board: Board being used for game logic
    """
    INFTY = 99999

    def __init__(self, board):
        self.board = board

    def run(self):
        bound = self.h_value(self.board)
        path = [self.board]
        moves = []
        while True:
            t = self.search(path, 0, bound, moves)
            if t is True:
                print(f'found solution of {len(moves)} moves')
                return moves
            elif t == self.INFTY:
                return None
            bound = t

    def search(self, path, g, bound, moves):
        node = path[-1]
        f = g + self.h_value(node)
        if f > bound:
            return f
        if node.check_win():
            return True
        min = self.INFTY

        for move in node.DIRS:
            if len(moves) > 0 and (-move[0], -move[1]) == moves[-1]:
                continue

            new_node = node.simulate_move(move)
            if new_node and not new_node in path:
                path.append(new_node)
                moves.append(move)
                t = self.search(path, g + 1, bound, moves)
                if t == True:
                    return True
                if t < min:
                    min = t
                path.pop()
                moves.pop()

        return min

    def h_value(self, current_board):
        h = 0
        numbers_grid = current_board.numbers_grid
        for y in range(current_board.size):
            for x in range(current_board.size):
                number = numbers_grid[y][x]
                if number != 0:
                    h += abs((number - 1) // current_board.size - y)
                    h += abs((number - 1) % current_board.size - x)
        return h
