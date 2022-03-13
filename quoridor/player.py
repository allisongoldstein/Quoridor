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

    def place_fence(self, coords, orientation):
        if self.has_fences:
            fence = Fence(coords, orientation, self.color)
            self.remaining_fences -= 1
            if self.remaining_fences == 0:
                self.has_fences = False
            return fence
        print("player has no fences")
        return False