from pawn import Pawn

class Player():

    def __init__(self, number):
        self.player_number = number
        if self.player_number == 1:
            self.pawn = Pawn((4, 0))
            self.pawn_id = "P1"
        else:
            self.pawn = Pawn((4, 8))
            self.pawn_id = "P2"
