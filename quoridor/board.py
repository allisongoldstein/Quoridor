from numpy import spacing
import pygame
from .constants import *
from .pawn import Pawn
from .fence import Fence
from .player import Player
from .info_card import Info_Card


class Board:

    def __init__(self):
        self.board = []

        self.player_count = 2
        self.players = []
        self.turn = 0

        self.pawns = []
        self.selected_pawn = None

        self.fences = []
        self.h_fences = [["" for _ in range(ROWS+1)] for _ in range(COLS+1)]
        self.v_fences = [["" for _ in range(ROWS+1)] for _ in range(COLS+1)]
        
        self.buttons = []
        self.button_coords = []
        self.selected_button = None
        
        self.info_cards = []

        self.move_type = None
        self.game_status = "unfinished"
        self.create_board()

    def move_pawn(self, row, col):
        pawn = self.selected_pawn

        if not self.open_space(row, col) or not self.valid_move(pawn, row, col):
            self.selected_pawn = None
            print("invalid move")
            return False

        self.board[pawn.row][pawn.col], self.board[row][col] = self.board[row][col], self.board[pawn.row][pawn.col]
        pawn.move(row, col)
        self.selected_pawn = None

        self.win_check(pawn)

        if self.game_status == "unfinished":
            self.update_turn()

    def valid_move(self, pawn, row, col):
        if 0 <= row < ROWS and 0 <= col < COLS:
            x_dif = abs(row - pawn.row)
            y_dif = abs(col - pawn.col)
            if x_dif == 2 and y_dif == 0:
                middle_row = min(pawn.row, row) + 1
                if self.board[middle_row][col] == "":
                    return False
                return self.fence_check(pawn.row, pawn.col, row, col, checks=2)
            if x_dif <= 1 and y_dif <= 1:
                if (x_dif + y_dif) > 0:
                    return self.fence_check(pawn.row, pawn.col, row, col)
        return False

    def place_fence(self, x, y, orientation):
        if self.has_fence(x, y, orientation):
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
        self.fences.append(fence)
        self.update_turn()

    def fence_check(self, row, col, new_row, new_col, checks=1):
        if checks == 2:
            orientation = "h"
            start_x = max(row, new_row)
            if self.has_fence(start_x, col, orientation) or self.has_fence(start_x-1, col, orientation):
                print("watch out for the fence")
                return False
        else:
            if new_row == row:
                orientation = "v"
            elif new_col == col:
                orientation = "h"
            else:
                print("implement diagonal move checks later")
                return

            if orientation == "h":
                f_x = max(row, new_row)
                if self.has_fence(f_x, col, orientation):
                    print("yep, that's a horizontal fence @ ", f_x, col)
                    return False
                else:
                    print("no fence detected")
            elif orientation == "v":
                f_y = max(col, new_col)
                if self.has_fence(row, f_y, orientation):
                    print("yep, that's a vertical fence @ ", row, f_y)
                    return False
                else:
                    print("no fence detected")

        return True

    def update_turn(self):
        if self.turn == 0:
            self.turn = 1
        else:
            self.turn = 0
        button = self.get_button_by_id("pawn")
        self.set_selected_button(button)

    def win_check(self, pawn):
        if self.turn == 0:
            check = 1
        else:
            check = 0
        if pawn.row == START_COORDS[check][0]:
            print("player", self.turn, "wins")
            self.game_status = "finished"
            return True

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

    def has_fence(self, x, y, orientation):
        if orientation == "h":
            if self.h_fences[x][y] != "":
                return True
        elif orientation == "v":
            if self.v_fences[x][y] != "":
                return True
        return False

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
                print("player has no fences")
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
        self.create_fences()
        self.create_info_cards()

    def create_players(self):
        for num in range(self.player_count):
            player = Player(num)
            x = player.start_coords[0]
            y = player.start_coords[1]
            self.players.append(player)
            pawn = Pawn((x, y), num, player.color)
            self.board[x][y] = pawn
            self.pawns.append(pawn)

    def create_fences(self):
        for i in range(ROWS+1):
            for j in range(COLS+1):
                if not 0 < i < ROWS:
                    self.h_fences[i][j] = "EDGE"
                if not 0 < j < COLS:
                    self.v_fences[i][j] = "EDGE"

    def create_info_cards(self):
        ids = ["p1_fences", "p2_fences", "turn", "pawn", "fence"]
        is_button = [False, False, False, True, True]
        text = ["FENCES LEFT: 10", "FENCES: 10", "CURRENT TURN: 1", "MOVE PAWN", "PLACE FENCE"]
        color = [self.players[0].color, self.players[1].color, self.players[0].color, "x", "x"]
        c_side = ["l", "l,", "r", "x", "x"]
        h_offsets = [EDGE+10, TOTAL_HEIGHT-(EDGE+B_HEIGHT+10), TOTAL_HEIGHT//3.5, TOTAL_HEIGHT//2 - (B_GAP+B_HEIGHT), TOTAL_HEIGHT//2 + B_GAP]
        for i in range(len(ids)):
            info_card = Info_Card(ids[i], text[i], color[i], c_side[i], h_offsets[i])
            self.info_cards.append(info_card)
            if is_button[i] is True:
                self.buttons.append(info_card)
                self.button_coords.append([(B_X_OFFSET, B_X_OFFSET+B_WIDTH), (h_offsets[i], h_offsets[i]+B_HEIGHT)])
        self.selected_button = self.buttons[0]
        self.move_type = self.selected_button.id
  
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

    def draw_fences(self, win):
        for fence in self.fences:
            fence.draw_fence(win)

    def draw_info_cards(self, win):
        for card in self.info_cards:
            if self.selected_button == card:
                card.draw(win, selected=True)
            else:
                card.draw(win)
        
    def draw(self, win):
        self.draw_board(win)
        for pawn in self.pawns:
            if pawn == self.selected_pawn:
                pawn.draw(win, BLACK)
            else:
                pawn.draw(win)
        
        self.draw_fences(win)
        self.draw_info_cards(win)
