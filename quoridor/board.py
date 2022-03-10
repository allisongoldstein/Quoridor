import pygame
from .constants import BLACK, WHITE, BG_COLOR, SQ_COLOR, BOARD_SIZE, SQUARE_SIZE, ROWS, COLS, W_DIFF, H_DIFF
from .player import Player
from .pawn import Pawn


class Board:

    def __init__(self):
        self.board = []
        self.player_count = 2
        self.players = []
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
        for num in range(self.player_count):
            player = Player(num)
            x = player.start_coords[0]
            y = player.start_coords[1]
            self.players.append(player)
            self.board[x][y] = Pawn((x, y), num+1)

    def draw(self, win):
        self.draw_board(win)
        for row in range(ROWS):
            for col in range(COLS):
                pawn = self.board[row][col]
                if pawn != "":
                    pawn.draw(win)
