from cgitb import reset
import enum
from pygame import Vector2
import pygame


class Snake:
    def __init__(self):
        self.body = [Vector2(10, 10), Vector2(9, 10), Vector2(8, 10)]
        self.direction = Vector2(0, 0)
        self.last_direction = Vector2(1, 0)
        # snake sprites
        self.snake_body = pygame.image.load('sprites/body.png')
        self.snake_head = pygame.image.load('sprites/head.png')
        # Sonido cunado come
        self.sonido_comer = pygame.mixer.Sound('Musica/comer.mp3')

    def juego_sonido_comer(self):
        self.sonido_comer.play()

    def draw_snake(self, screen, cell_size):
        for index, block in enumerate(self.body):
            x = block.x*cell_size
            y = block.y*cell_size
            block_rect = pygame.Rect(x, y, cell_size, cell_size)
            if index == 0:
                if self.direction == Vector2(0, 0):
                    self.draw_head(screen, block_rect, self.last_direction)
                else:
                    self.draw_head(screen, block_rect, self.direction)
            else:
                screen.blit(self.snake_body, block_rect)

    def move_snake(self):
        if self.direction != Vector2(0, 0):
            body = self.body[:-1]
            body.insert(0, body[0]+self.direction)
            self.body = body[:]

    def grow(self):
        self.body.append(self.body[-1]+self.direction)

    def reset(self):
        self.body = [Vector2(10, 10), Vector2(9, 10), Vector2(8, 10)]
        self.direction = Vector2(0, 0)
        self.last_direction = Vector2(1, 0)

    def draw_head(self, screen, block_rect, direction):
        if direction == Vector2(1, 0):
            screen.blit(self.snake_head, block_rect)
        elif direction == Vector2(-1, 0):
            screen.blit(pygame.transform.rotate(
                self.snake_head, 180), block_rect)
        elif direction == Vector2(0, 1):
            screen.blit(pygame.transform.rotate(
                self.snake_head, 270), block_rect)
        elif direction == Vector2(0, -1):
            screen.blit(pygame.transform.rotate(
                self.snake_head, 90), block_rect)

    def pause(self):
        self.last_direction = self.direction
        self.direction = Vector2(0, 0)
