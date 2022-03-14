from .constants import *
from .fence import Fence

class Player():

    def __init__(self, id):
        self.id = id
        self.start_coords = START_COORDS[id]
        self.color = P_COLORS[id]
        self.has_fences = True
        self.remaining_fences = 10
        if self.id == 0:
            self.goal_line = BOARD_Y_START
        else:
            self.goal_line = BOARD_Y_END-PADDING

    def place_fence(self, row, col, orientation):
        if self.has_fences:
            fence1 = Fence(row, col, orientation, self.color)
            fence2 = Fence(row, col, orientation, self.color)
            self.remaining_fences -= 1
            if self.remaining_fences == 0:
                self.has_fences = False
            return fence1, fence2
        return False