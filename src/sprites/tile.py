from load_image import load_image
import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, number):
        super().__init__()
        self.number = number

        self.images = self._load_images()

        self.image = self.images[number]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.neighbours = []

    def update(self):
        self.image = self.images[self.number]

    def add_neighbour(self, new_neighbour):
        self.neighbours.append(new_neighbour)
        new_neighbour.neighbours.append(self)

    def move(self):
        for neighbour in self.neighbours:
            if neighbour.number == 0:
                neighbour.number = self.number
                self.number = 0
                break

    def _load_images(self):
        images = {}
        for i in range(16):
            images[i] = load_image(f'tile{i}.png')
        return images
