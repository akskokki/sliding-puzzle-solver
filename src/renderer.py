import pygame


class Renderer:
    """ Renders the game into pygame

    Attributes:
        ui: Elements to be rendered
        display: The display to render the elements on
    """

    def __init__(self, ui, display):
        self.ui = ui
        self.display = display

    def render(self):
        self.ui.tiles.draw(self.display)
        pygame.display.flip()
