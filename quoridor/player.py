from .constants import *
from .fence import Fence

class Player():

    def __init__(self, number):
        self.number = number
        self.start_coords = START_COORDS[number]
        self.color = P_COLORS[number]
        self.has_fences = True
        self.remaining_fences = 10
        if self.number == 0:
            self.goal_line = BOARD_Y_START
        else:
            self.goal_line = BOARD_Y_END-PADDING

    def place_fence(self, win, fence):
        fence.draw_fence(win, self.color)
