import pygame
from .constants import BLACK, WHITE, BG_COLOR, SQ_COLOR, BOARD_SIZE, SQUARE_SIZE, FENCE_SIZE, ROWS, COLS, W_DIFF, H_DIFF
from .pawn import Pawn
from .fence import Fence
from .player import Player


class Board:

    def __init__(self):
        self.board = []
        self.player_count = 2
        self.players = []
        self.turn = 0
        self.create_board()
        self.selected_pawn = None

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

    def set_selected_pawn(self, pawn, row, col):
        if not self.valid_space(row, col):
            print("invalid space")
            return False
        if self.selected_pawn is not None:
            self.selected_pawn = None
            print("deselect")
            return False
        
        pawn = self.get_pawn(row, col)
        if pawn != "":
            if self.valid_turn(pawn):
                self.selected_pawn = pawn
                print("pawn set:", pawn)
                return True

        return False

    def open_space(self, row, col):
        if not self.valid_space(row, col):
            return False
        if self.board[row][col] == self.selected_pawn:
            self.selected_pawn = None
            print("deselect")
            return False

        return True


    def get_player(self):
        return self.players[self.turn]

    def get_pawn(self, row, col):
        return self.board[row][col]

    def valid_turn(self, pawn):
        if pawn.id == self.turn:
            return True
        else:
            print("invalid turn")
            return False

    def valid_space(self, row, col):
        return (0 <= row < ROWS and 0 <= col < COLS)
        
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
            self.board[x][y] = Pawn((x, y), num, player.color)

    def draw_board(self, win):
        win.fill(BG_COLOR)
        pygame.draw.rect(win, BLACK, ((W_DIFF/2 -5), (H_DIFF/2 -5), BOARD_SIZE, BOARD_SIZE))
        pygame.draw.rect(win, WHITE, ((W_DIFF/2), (H_DIFF/2), BOARD_SIZE-10, BOARD_SIZE-10))
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(win, SQ_COLOR, (row*SQUARE_SIZE+(W_DIFF/2), col*SQUARE_SIZE+(H_DIFF/2), SQUARE_SIZE-5, SQUARE_SIZE-5))

        player = self.get_player()
        misc = Fence((4, 5), "g")
        misc.draw_fence(win, player.color) # temp

    def draw(self, win):
        self.draw_board(win)
        for row in range(ROWS):
            for col in range(COLS):
                pawn = self.board[row][col]
                if pawn != "":
                    pawn.draw(win)
