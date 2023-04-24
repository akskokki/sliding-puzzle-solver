import unittest
import pygame

from board import Board
from game_loop import GameLoop
from ui import UI


class StubClock:
    def tick(self, fps):
        pass

    def get_ticks(self):
        1


class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key


class StubEventQueue:
    def __init__(self, events):
        self._events = events

    def get(self):
        return self._events


class StubRenderer:
    def render(self):
        pass


class StubIDAStar:
    def __init__(self):
        pass


class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.board = Board(4)

    def test_moving_works(self):
        events = [
            StubEvent(pygame.KEYDOWN, pygame.K_LEFT),
            StubEvent(pygame.QUIT, None)
        ]
        self.assertEqual(self.board.numbers_grid[3][3], 0)
        self.assertEqual(self.board.numbers_grid[3][2], 15)

        game_loop = GameLoop(
            self.board, UI(self.board), StubRenderer(
            ), StubEventQueue(events), StubClock(), StubIDAStar()
        )
        game_loop.start()

        self.assertEqual(self.board.numbers_grid[3][3], 15)
        self.assertEqual(self.board.numbers_grid[3][2], 0)

    # def test_clicking_tile_works(self):
    #     events = [
    #         StubEvent(pygame.MOUSEBUTTONDOWN, (250, 350)),
    #         StubEvent(pygame.QUIT, None)
    #     ]
    #     self.assertEqual(self.board.numbers_grid[3][3].number, 0)
    #     self.assertEqual(self.board.numbers_grid[3][2].number, 15)

    #     game_loop = GameLoop(
    #         self.board, StubRenderer(), StubEventQueue(events), StubClock()
    #     )
    #     game_loop.start()

    #     self.assertEqual(self.board.numbers_grid[3][3].number, 15)
    #     self.assertEqual(self.board.numbers_grid[3][2].number, 0)
