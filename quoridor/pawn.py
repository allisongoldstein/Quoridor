import pygame
from constants import SQUARE_SIZE, WHITE, BLACK

class Pawn():
    PADDING = 10
    OUTLINE = 2

    def __init__(self, coordinates):
        self.row = coordinates[0]
        self.col = coordinates[1]

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def draw(self, win):        # temporary
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, WHITE, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, BLACK, (self.x, self.y), radius)
        
    def __repr__(self):
        return str(self.row, self.col)
