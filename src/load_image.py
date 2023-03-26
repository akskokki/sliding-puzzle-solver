import pygame
import os

dir = os.path.dirname(__file__)


def load_image(file):
    return pygame.image.load(
        os.path.join(dir, 'assets', file)
    )
