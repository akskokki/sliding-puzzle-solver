import pygame
from board import Board
from utilities.event_queue import EventQueue
from utilities.renderer import Renderer
from utilities.clock import Clock
from game_loop import GameLoop
from ida_star import IDAStar
from ui import UI
from logger import Logger


def main():
    size = 4
    solver_timeout = 20

    screen = pygame.display.set_mode([size*100, size*100])
    pygame.display.set_caption('15 puzzle')

    board = Board(size)
    ui = UI(board)
    logger = Logger()
    solver = IDAStar(board, logger, solver_timeout)
    event_queue = EventQueue()
    renderer = Renderer(ui, screen)
    clock = Clock()
    game_loop = GameLoop(board, ui, renderer, event_queue, clock, solver)

    pygame.init()
    game_loop.start()
    pygame.quit()


if __name__ == "__main__":
    main()
