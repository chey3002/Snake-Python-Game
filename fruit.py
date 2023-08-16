import pygame
import random
from pygame.math import Vector2


class Fruit:
    def __init__(self, cell_number):
        self.cell_number = cell_number
        self.randomize()
        self.apple = pygame.image.load('Imagenes/bit.png').convert_alpha()


    def draw(self, screen, cell_size):
        x = self.pos.x*cell_size
        y = self.pos.y*cell_size
        fruit_rect = pygame.Rect(x, y, cell_size, cell_size)
        #pygame.draw.rect(screen, (255, 0, 0), fruit_rect)
        screen.blit(self.apple,fruit_rect)

    def randomize(self):
        self.x = random.randint(0, self.cell_number-1)
        self.y = random.randint(0, self.cell_number-1)
        self.pos = Vector2(self.x, self.y)
