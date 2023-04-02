import pygame


class Clock:
    """ Implements basic functions of pygame Clock
    """

    def __init__(self):
        self.clock = pygame.time.Clock()

    def tick(self, fps):
        self.clock.tick(fps)
