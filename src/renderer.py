import pygame


class Renderer:
    def __init__(self, ui, display):
        self.ui = ui
        self.display = display

    def render(self):
        self.ui.tiles.draw(self.display)
        pygame.display.flip()
