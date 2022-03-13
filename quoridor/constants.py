import pygame

TOTAL_WIDTH, TOTAL_HEIGHT = 810, 610
BOARD_SIZE = 500
PADDING = 5
EDGE = (TOTAL_HEIGHT - BOARD_SIZE)//2
BOARD_X_START = EDGE - PADDING
BOARD_Y_START = EDGE- PADDING
BOARD_X_END = BOARD_X_START + BOARD_SIZE
BOARD_Y_END = BOARD_X_START + BOARD_SIZE
ROWS, COLS = 9, 9
SQUARE_SIZE = BOARD_SIZE//COLS
SPACE_SIZE = SQUARE_SIZE - 5

FENCE_SIZE = SQUARE_SIZE//COLS * 2
FENCE_SHORT = SQUARE_SIZE//COLS - 1
FENCE_LONG = SQUARE_SIZE-(FENCE_SHORT)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BG_COLOR = (224, 224, 224)
SQ_COLOR = (202, 223, 237) #199, 233, 255 #(200, 189, 235)
B_COLOR = (128, 128, 128)

START_COORDS = [(0, 4), (8, 4)]
P_COLORS = [(27, 191, 43), (88, 31, 209)]
SQ_RANGES = [(SPACE_SIZE*(i+1)+i*5, SPACE_SIZE*(i+2)+i*5) for i in range(ROWS)]

PAWN_PADDING = 10
PAWN_OUTLINE = 2

B_WIDTH = 140
B_HEIGHT = 30
B_GAP = 20
B_PADDING = 3

F_RANGES = [(SPACE_SIZE*(i+1)+(i*5), SPACE_SIZE*(i+1)+(i+1)*5) for i in range(ROWS+1)]

# 610-750
# 205-235