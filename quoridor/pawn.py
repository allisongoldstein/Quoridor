import pygame
from .constants import SQUARE_SIZE, WHITE, BLACK, W_DIFF, H_DIFF

class Pawn():
    PADDING = 10
    OUTLINE = 2

    def __init__(self, coordinates, id):
        self.row = None
        self.col = None
        self.set_coordinates(coordinates[0], coordinates[1])
        self.id = "P" + str(id)

        self.x = 0
        self.y = 0

    def set_coordinates(self, x, y):
        self.row = x
        self.col = y

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2 + W_DIFF/2 -5/2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2 + H_DIFF/2 -5/2

    def draw(self, win):        # temporary
        self.calc_pos()
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, WHITE, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, BLACK, (self.x, self.y), radius)
        
    def __repr__(self):
        return str(self.row, self.col)
