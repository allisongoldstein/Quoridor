class Player():

    def __init__(self, number):
        self.player_number = number
        if self.player_number == 1:
            self.start_coords = (0, 4)
        else:
            self.start_coords = (8, 4)
