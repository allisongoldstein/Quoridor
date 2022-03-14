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

    def draw(self, win, selected=False, count=None):
        if selected:
            BORDER = BLACK
        else:
            BORDER = B_COLOR

        pygame.draw.rect(win, BORDER, (B_X_OFFSET, self.h_offset, B_WIDTH, B_HEIGHT))
        self.surface = pygame.draw.rect(win, WHITE, (B_X_OFFSET+B_PADDING, self.h_offset+B_PADDING, B_WIDTH-B_PADDING*2, B_HEIGHT-B_PADDING*2))
        
        if self.c_side is not None:
            if self.c_side == "l":
                pygame.draw.rect(win, self.color, (B_X_OFFSET+PADDING*2, self.h_offset+6, C_WIDTH, C_WIDTH))
            else:
                pygame.draw.rect(win, self.color, (B_X_OFFSET+B_WIDTH-(C_WIDTH+8), self.h_offset+6, C_WIDTH, C_WIDTH))

        self.add_text(win, count)
        
    def add_text(self, win, count):
        if count is not None:
            cur_text = self.text + str(count)
        else:
            cur_text = self.text
        FONT = pygame.font.SysFont('Georgia', 18)
        text = FONT.render(cur_text, True, BLACK)
        if self.c_side is None:
            text_rect = text.get_rect(center=self.surface.center)
        else:
            x, y = self.surface.center 
            if self.c_side == "l":
                text_rect = text.get_rect(center=(x+C_WIDTH-8, y))
            else:
                text_rect = text.get_rect(center=(x-C_WIDTH+8, y))
        
        win.blit(text, text_rect)

    def __repr__(self):
        return str(self.id) + " " + str(self.h_offset)


