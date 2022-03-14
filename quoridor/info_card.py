import pygame
import pygame.freetype
from .constants import *


class Info_Card():

    def __init__(self, id, text, color, c_side, h_offset):
        self.id = id
        self.text = text
        self.color = color
        self.c_side = c_side
        self.c_offset = C_WIDTH
        self.h_offset = h_offset

    def draw(self, win, selected=False):
        if selected:
            BORDER = BLACK
        else:
            BORDER = B_COLOR
        pygame.draw.rect(win, BORDER, (B_X_OFFSET, self.h_offset, B_WIDTH, B_HEIGHT))
        self.surface = pygame.draw.rect(win, WHITE, (B_X_OFFSET+B_PADDING, self.h_offset+B_PADDING, B_WIDTH-B_PADDING*2, B_HEIGHT-B_PADDING*2))
        self.add_text(win)
        
    def add_text(self, win):
        FONT = pygame.font.SysFont('Georgia', 18)
        text = FONT.render(self.text, True, BLACK)
        text_rect = text.get_rect(center=self.surface.center)
        win.blit(text, text_rect)

    def __repr__(self):
        return str(self.id) + " " + str(self.h_offset)


