import pygame
from .constants import *


class Fence():

    def __init__(self, coords, orientation, color):
        self.row = coords[0]
        self.col = coords[1]
        self.orientation = orientation
        self.color = color
        print(self)

    def draw_fence(self, win):
        if self.orientation == "h":
            x = (self.col + 1) * SQUARE_SIZE
            y = (self.row + 1) * SQUARE_SIZE - 5
            width, height = FENCE_LONG, FENCE_SHORT
        else:
            x = (self.col + 1) * SQUARE_SIZE - 5
            y = (self.row + 1) * SQUARE_SIZE
            width, height = FENCE_SHORT, FENCE_LONG
        pygame.draw.rect(win, self.color, (x, y, width, height))

    def __repr__(self):
        return str(self.row) + ", " + str(self.col) + ", " + str(self.orientation)
    