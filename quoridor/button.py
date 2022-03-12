import pygame
import pygame.freetype
from .constants import *


class Button():

    def __init__(self, id, text, h_offset):
        self.id = id
        self.text = text
        self.h_offset = h_offset
        self.surface = None
        
    def draw(self, win, selected=False):
        if selected:
            BORDER = BLACK
        else:
            BORDER = B_COLOR
        pygame.draw.rect(win, BORDER, (TOTAL_HEIGHT, self.h_offset, B_WIDTH, B_HEIGHT))
        self.surface = pygame.draw.rect(win, WHITE, (TOTAL_HEIGHT+B_PADDING, self.h_offset+B_PADDING, B_WIDTH-B_PADDING*2, B_HEIGHT-B_PADDING*2))
        self.add_text(win)
        
    def add_text(self, win):
        FONT = pygame.font.SysFont('Georgia', 18)
        text = FONT.render(self.text, True, BLACK)
        text_rect = text.get_rect(center=self.surface.center)
        win.blit(text, text_rect)


    def __repr__(self):
        return str(self.id) + " " + str(self.h_offset)