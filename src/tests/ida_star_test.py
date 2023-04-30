import unittest
from ida_star import IDAStar
from board import Board


class MockLogger:
    """Mock Logger that always returns 5 seconds as elapsed time"""

    def reset(self):
        pass

    def add_node(self):
        return 5

    def set_bound(self, new_bound):
        return 5


class TestIDAStar(unittest.TestCase):
    def setUp(self):
        self.board = Board(4)
        self.ida_star = IDAStar(self.board, MockLogger())

    def test_solved_state_has_h_value_zero(self):
        numbers_grid = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]
        ]
        self.board.numbers_grid = numbers_grid

        h_value = self.ida_star.h_value(self.board)
        self.assertEqual(h_value, 0)

    def test_manhattan_distance_works(self):
        manhattan_value = self.ida_star.find_manhattan(1, 3, 1)
        self.assertEqual(manhattan_value, 4)

    def test_conflicts_works(self):
        numbers_grid = [
            [3, 1, 4, 2],
            [7, 6, 5, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]
        ]
        conflicts_value_3 = self.ida_star.find_conflicts(numbers_grid, 0, 0, 3)
        self.assertEqual(conflicts_value_3, 1)
        conflicts_value_7 = self.ida_star.find_conflicts(numbers_grid, 0, 1, 7)
        self.assertEqual(conflicts_value_7, 2)

    def test_solved_state_returns_0_move_solution(self):
        numbers_grid = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]
        ]
        self.board.numbers_grid = numbers_grid

        moves = self.ida_star.run()
        self.assertEqual(len(moves), 0)

    def test_simple_solution_is_found(self):
        numbers_grid = [
            [1, 2, 7, 3],
            [5, 0, 6, 4],
            [9, 10, 11, 8],
            [13, 14, 15, 12]
        ]
        self.board.numbers_grid = numbers_grid
        self.board.blank_coords = (1, 1)

        moves = self.ida_star.run()
        self.assertEqual(len(moves), 6)

    def test_timeout_works(self):
        numbers_grid = [
            [1, 2, 7, 3],
            [5, 0, 6, 4],
            [9, 10, 11, 8],
            [13, 14, 15, 12]
        ]
        self.board.numbers_grid = numbers_grid
        self.board.blank_coords = (1, 1)

        self.ida_star = IDAStar(self.board, MockLogger(), 4)

        moves = self.ida_star.run()
        self.assertEqual(moves, None)
