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
            print(f'new bound: {bound}')

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
