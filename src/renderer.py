import pygame


class Renderer:
    def __init__(self, board, display):
        self.board = board
        self.display = display

    def render(self):
        self.board.all_sprites.draw(self.display)
        pygame.display.flip()
