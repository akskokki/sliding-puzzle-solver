import pygame
from load_image import load_image


class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, number):
        super().__init__()
        self.number = number
        self.x = x
        self.y = y

        self.images = self._load_images()

        self.image = self.images[number]
        self.rect = self.image.get_rect()
        self.rect.x = x * self.rect.width
        self.rect.y = y * self.rect.height

    def update(self):
        self.image = self.images[self.number]

    def _load_images(self):
        images = {}
        for i in range(16):
            images[i] = load_image(f'tile{i}.png')
        return images
