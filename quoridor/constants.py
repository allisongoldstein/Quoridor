import pygame

WIDTH, HEIGHT = 600, 600
BOARD_SIZE = 500
ROWS, COLS = 9, 9
W_DIFF = WIDTH - BOARD_SIZE
H_DIFF = HEIGHT - BOARD_SIZE
SQUARE_SIZE = BOARD_SIZE//COLS
FENCE_SIZE = SQUARE_SIZE//COLS * 2
FENCE_SHORT = SQUARE_SIZE//COLS - 1
FENCE_LONG = SQUARE_SIZE-(FENCE_SHORT)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BG_COLOR = (224, 224, 224)
SQ_COLOR = (200, 189, 235)


START_COORDS = [(0, 4), (8, 4)]
P_COLORS = [(0, 255, 0), (255, 0, 255)]
