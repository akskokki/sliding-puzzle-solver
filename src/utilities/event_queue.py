import pygame


class EventQueue:
    """ Simply gets the next event from the pygame events
    """

    def get(self):
        return pygame.event.get()
