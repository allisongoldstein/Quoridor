import pygame
from .constants import *

class Pawn():

    def __init__(self, coords, id, color):
        self.row = coords[0]
        self.col = coords[1]
        self.x = 0
        self.y = 0
        self.calc_pos()
        self.id = id
        self.color = color

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2 + EDGE - PADDING//2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2 + EDGE - PADDING//2

    def draw(self, win, border_color=WHITE):        # temporary
        radius = SQUARE_SIZE//2 - PAWN_PADDING
        pygame.draw.circle(win, border_color, (self.x, self.y), radius + PAWN_OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        
    def __repr__(self):
        return "(" + str(self.row) + "," + str(self.col) + ")"
