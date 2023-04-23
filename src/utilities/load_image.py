import os
import pygame

directory = os.path.dirname(__file__)


def load_image(file):
    return pygame.image.load(
        os.path.join(directory, 'assets', file)
    )
