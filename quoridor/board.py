import pygame
from .constants import BG_COLOR, BOARD_SIZE, BLACK, WHITE, SQ_COLOR, ROWS, COLS, W_DIFF, H_DIFF, SQUARE_SIZE

class Board:

    def __init__(self):
        self.board = []
        self.create_board()
        self.selected_space = None

    def draw_board(self, win):
        win.fill(BG_COLOR)
        pygame.draw.rect(win, BLACK, ((W_DIFF/2 -5), (H_DIFF/2 -5), BOARD_SIZE, BOARD_SIZE))
        pygame.draw.rect(win, WHITE, ((W_DIFF/2), (H_DIFF/2), BOARD_SIZE-10, BOARD_SIZE-10))
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(win, SQ_COLOR, (row*SQUARE_SIZE+(W_DIFF/2), col*SQUARE_SIZE+(H_DIFF/2), SQUARE_SIZE-5, SQUARE_SIZE-5))
        
    def create_board(self):
        for _ in range(ROWS):
            row = []
            for _ in range(COLS):
                row.append("")
            self.board.append(row)

    def draw_pawns(self, win):
        pass
