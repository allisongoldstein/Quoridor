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
        self.pawns = []
        self.selected_pawn = None
        self.buttons = []
        self.button_coords = []
        self.selected_button = None
        self.fences = []
        self.h_fences = [["" for _ in range(ROWS)] for _ in range(COLS)]
        self.v_fences = [["" for _ in range(ROWS)] for _ in range(COLS)]
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
        self.update_turn()

        # check for win pos

    def place_fence(self, x, y, orientation):
        if not self.open_fence_space(x, y, orientation):
            print("fence already exists at location")
            return False
        player = self.players[self.turn]
        fence = player.place_fence((x, y), orientation)
        if fence is False:
            return False
        if orientation == "h":
            self.h_fences[x][y] = fence
        elif orientation == "v":
            self.v_fences[x][y] = fence
        print(fence)
        self.fences.append(fence)
        self.update_turn()

    def update_turn(self):
        if self.turn == 0:
            self.turn = 1
        else:
            self.turn = 0
        button = self.get_button_by_id("pawn")
        self.set_selected_button(button)

    def on_board(self, coords):
        x, y = coords
        if BOARD_X_START <= x <= BOARD_X_END and BOARD_Y_START <= y <= BOARD_Y_END:
            return True
        else:
            return False

    def valid_turn(self, pawn):
        if pawn.id == self.turn:
            return True
        else:
            print("invalid turn")
            return False

    def valid_space(self, row, col):
        return (0 <= row < ROWS and 0 <= col < COLS)

    def open_space(self, row, col):
        if not self.valid_space(row, col):
            return False
        if self.board[row][col] == self.selected_pawn:
            self.selected_pawn = None
            return False
        elif self.board[row][col] != "":
            return False

        return True

    def open_fence_space(self, x, y, orientation):
        if orientation == "h":
            if self.h_fences[x][y] != "":
                return False
        elif orientation == "v":
            if self.v_fences[x][y] != "":
                return False
        return True

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
        if button.id == "fence":
            if self.players[self.turn].has_fences is False:
                return False
        self.selected_button = button
        self.set_move_type(button.id)

    def set_move_type(self, type):
        self.move_type = type
        self.selected_pawn = None

    def get_player(self):
        return self.players[self.turn]

    def get_pawn(self, row, col):
        return self.board[row][col]

    def get_button_by_id(self, id):
        for button in self.buttons:
            if button.id == id:
                return button

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
        self.create_fences()

    def create_players(self):
        for num in range(self.player_count):
            player = Player(num)
            x = player.start_coords[0]
            y = player.start_coords[1]
            self.players.append(player)
            pawn = Pawn((x, y), num, player.color)
            self.board[x][y] = pawn
            self.pawns.append(pawn)

    def create_buttons(self):
        ids = ["pawn", "fence"]
        texts = ["MOVE PAWN", "PLACE FENCE"]
        h_offsets = [TOTAL_HEIGHT//2 - (B_GAP+B_HEIGHT), TOTAL_HEIGHT//2 + B_GAP]
        for i in range(len(ids)):
            self.buttons.append(Button(ids[i], texts[i], h_offsets[i]))
            self.button_coords.append([(TOTAL_HEIGHT, TOTAL_HEIGHT+B_WIDTH), (h_offsets[i], h_offsets[i]+B_HEIGHT)])
        self.selected_button = self.buttons[0]
        self.move_type = self.selected_button.id

    def create_fences(self):
        for i in range(ROWS):
            for j in range(COLS):
                if not 0 < i < ROWS-1:
                    self.h_fences[i][j] = "EDGE"
                if not 0 < j < COLS-1:
                    self.v_fences[i][j] = "EDGE"
        
    def draw_board(self, win):
        win.fill(BG_COLOR)
        pygame.draw.rect(win, BLACK, (BOARD_X_START, BOARD_Y_START, BOARD_SIZE, BOARD_SIZE))
        pygame.draw.rect(win, WHITE, (BOARD_X_START+PADDING, BOARD_Y_START+PADDING, BOARD_SIZE-PADDING*2, BOARD_SIZE-PADDING*2))
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(win, SQ_COLOR, (row*SQUARE_SIZE+EDGE, col*SQUARE_SIZE+EDGE, SPACE_SIZE, SPACE_SIZE))
        for player in self.players:
            for i in range((BOARD_SIZE-PADDING*2)//PADDING):
                if (i % 2) == 0:
                    color = player.color
                else:
                    color = WHITE
                pygame.draw.rect(win, color, ((BOARD_X_START+PADDING)+PADDING*i, player.goal_line, PADDING, PADDING))
        
    def draw_buttons(self, win):
        for button in self.buttons:
            if button == self.selected_button:
                button.draw(win, "selected")
            else:
                button.draw(win)

    def draw_fences(self, win):
        for fence in self.fences:
            fence.draw_fence(win)
        
    def draw(self, win):
        self.draw_board(win)
        for pawn in self.pawns:
            if pawn == self.selected_pawn:
                pawn.draw(win, BLACK)
            else:
                pawn.draw(win)
        
        self.draw_fences(win)

        self.draw_buttons(win)
