import pygame
from .constants import *


class Fence():

    def __init__(self, coords, orientation):
        self.row = coords[0]
        self.col = coords[1]
        self.orientation = orientation

    def draw_fence(self, win, color):
        x = self.row * SQUARE_SIZE - 10
        y = self.col * SQUARE_SIZE - 5
        if self.orientation == "h":
            width, height = FENCE_LONG, FENCE_SHORT
        else:
            width, height = FENCE_SHORT, FENCE_LONG
        pygame.draw.rect(win, color, (x, y, width, height))
    