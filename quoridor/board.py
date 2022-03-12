from numpy import spacing
import pygame
from .constants import *
from .pawn import Pawn
from .fence import Fence
from .player import Player
from .button import Button


class Board:

    def __init__(self):
        self.board = []
        self.player_count = 2
        self.players = []
        self.turn = 0
        self.buttons = []
        self.button_coords = []
        self.selected_pawn = None
        self.selected_button = None
        self.move_type = None
        self.create_board()

    def move_pawn(self, row, col):
        # checks
        pawn = self.selected_pawn

        if not self.open_space(row, col) or not pawn.valid_move(row, col):
            self.selected_pawn = None
            print("invalid move")
            return False
        self.board[pawn.row][pawn.col], self.board[row][col] = self.board[row][col], self.board[pawn.row][pawn.col]
        pawn.move(row, col)

        self.selected_pawn = None
        if self.turn == 0:
            self.turn = 1
        else:
            self.turn = 0

        # check for win pos

    def valid_turn(self, pawn):
        if pawn.id == self.turn:
            return True
        else:
            print("invalid turn")
            return False

    def on_board(self, coords):
        x, y = coords
        if BOARD_X_START <= x <= BOARD_X_END and BOARD_Y_START <= y <= BOARD_Y_END:
            return True
        else:
            return False

    def valid_space(self, row, col):
        return (0 <= row < ROWS and 0 <= col < COLS)

    def set_selected_pawn(self, row, col):
        if self.move_type != "pawn":
            return False
        if self.selected_pawn is not None:
            self.selected_pawn = None
            return False
        
        pawn = self.get_pawn(row, col)
        if pawn != "":
            if self.valid_turn(pawn):
                self.selected_pawn = pawn
                return True

        return False

    def set_selected_button(self, button):
        self.selected_button = button
        self.set_move_type(button.id)

    def set_move_type(self, type):
        self.move_type = type
        self.selected_pawn = None

    def open_space(self, row, col):
        if not self.valid_space(row, col):
            return False
        if self.board[row][col] == self.selected_pawn:
            self.selected_pawn = None
            return False
        elif self.board[row][col] != "":
            return False

        return True

    def get_player(self):
        return self.players[self.turn]

    def get_pawn(self, row, col):
        return self.board[row][col]

    def is_button(self, pos):
        for i in range(len(self.buttons)):
            button = self.button_coords[i]
            if pos[0] in range(button[0][0], button[0][1]) and pos[1] in range(button[1][0], button[1][1]):
                return self.buttons[i]
        return False
        
    def create_board(self):
        for _ in range(ROWS):
            row = []
            for _ in range(COLS):
                row.append("")
            self.board.append(row)
        self.create_players()
        self.create_buttons()

    def create_players(self):
        for num in range(self.player_count):
            player = Player(num)
            x = player.start_coords[0]
            y = player.start_coords[1]
            self.players.append(player)
            self.board[x][y] = Pawn((x, y), num, player.color)

    def create_buttons(self):
        ids = ["pawn", "fence"]
        texts = ["MOVE PAWN", "PLACE FENCE"]
        h_offsets = [TOTAL_HEIGHT//3, TOTAL_HEIGHT//3 + 60]
        for i in range(len(ids)):
            self.buttons.append(Button(ids[i], texts[i], h_offsets[i]))
            self.button_coords.append([(TOTAL_HEIGHT, TOTAL_HEIGHT+B_WIDTH), (h_offsets[i], h_offsets[i]+B_HEIGHT)])
        self.selected_button = self.buttons[0]
        self.move_type = self.selected_button.id
        
    def draw_board(self, win):
        win.fill(BG_COLOR)
        pygame.draw.rect(win, BLACK, (BOARD_X_START, BOARD_Y_START, BOARD_SIZE, BOARD_SIZE))
        pygame.draw.rect(win, WHITE, (BOARD_X_START+PADDING, BOARD_Y_START+PADDING, BOARD_SIZE-10, BOARD_SIZE-10))
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(win, SQ_COLOR, (row*SQUARE_SIZE+EDGE, col*SQUARE_SIZE+EDGE, SPACE_SIZE, SPACE_SIZE))

    def draw_buttons(self, win):
        for button in self.buttons:
            if button == self.selected_button:
                button.draw(win, "selected")
            else:
                button.draw(win)
        
    def draw(self, win):
        self.draw_board(win)
        for row in range(ROWS):
            for col in range(COLS):
                pawn = self.board[row][col]
                if pawn != "":
                    if pawn == self.selected_pawn:
                        pawn.draw(win, BLACK)
                    else:
                        pawn.draw(win)
        
        # draw fences

        self.draw_buttons(win)
