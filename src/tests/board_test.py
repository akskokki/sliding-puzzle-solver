import unittest
from board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(4)

    def test_correct_starting_board(self):
        numbers_grid_correct = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]
        ]
        self.assertEqual(numbers_grid_correct, self.board.numbers_grid)

    def test_moving_works(self):
        numbers_grid_correct = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 0, 11],
            [13, 14, 15, 12]
        ]
        self.board.move(Board.UP)
        self.board.move(Board.LEFT)
        self.assertEqual(numbers_grid_correct, self.board.numbers_grid)

    def test_check_win_returns_correct_values(self):
        self.assertEqual(True, self.board.check_win())
        self.board.move(Board.UP)
        self.assertEqual(False, self.board.check_win())
