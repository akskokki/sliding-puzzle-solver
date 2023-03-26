import pygame
from board import Board
from event_queue import EventQueue
from renderer import Renderer
from clock import Clock
from game_loop import GameLoop


def main():
    size = 4

    screen = pygame.display.set_mode([size*100, size*100])
    pygame.display.set_caption('15 puzzle')

    board = Board(size)
    event_queue = EventQueue()
    renderer = Renderer(board, screen)
    clock = Clock()
    game_loop = GameLoop(board, renderer, event_queue, clock)

    pygame.init()
    game_loop.start()
    pygame.quit()

if __name__ == "__main__":
    main()
