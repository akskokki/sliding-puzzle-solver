from board import Board
from ida_star import IDAStar
from logger import Logger

board = Board(4)
logger = Logger()
solver = IDAStar(board, logger, 60)

while True:
    board.reset_board()
    board.scramble()
    board.scramble()
    solution = solver.run()
    elapsed_time = logger.get_elapsed_time()
    with open('performance_log', 'a') as log:
        if solution:
            solution_length = len(solution)
        else:
            solution_length = -1
        log.write(f'{solution_length},{elapsed_time}\n')
