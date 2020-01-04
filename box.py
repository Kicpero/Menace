from random import seed
from random import randint


class Box:
    # beads array:
    # if there is "-1" menace has already took position X
    # if there is "-2" random player has already took position
    # 0 no beads in position

    # default number of beads for each option
    default = 1

    # number of colours in a box, if box run out of one of the colour then decrease the number of colours
    colours = 0

    # chosen position in previous go
    chosen = -1

    # type = 0 for empty board with random play strategy
    # type != 0 for board with elements
    def __init__(self, mode, board):
        self.beads = [0, 0, 0, 0, 0, 0, 0, 0, 0].copy()
        seed(1000)
        if mode == 0:  # at the beginning random strategy
            self.beads[0] = 3
            self.beads[1] = 3
            self.beads[2] = 3
            self.colours = 3
        else:  # creating new box
            for i in range(0, 9):
                if board.get_board()[i] == 1:
                    self.beads[i] = -1
                elif board.get_board()[i] == 2:
                    self.beads[i] = -2
                else:
                    self.beads[i] = self.default
                    self.colours += 1

    # returns the place of MENACE move
    # decreases the number of beads of the position
    # set the chosen value
    def move(self):
        tmp = randint(1, self.colours)
        for i in range(0, 9):
            if self.beads[i] > 0:
                if tmp == 1:
                    self.beads[i] -= 1
                    self.chosen = i
                    if self.beads[i] == 0:
                        self.colours -= 1
                    return i
                else:
                    tmp -= 1
        return -1

    def modify_beads(self, result):
        if result == 1:  # if menace draw put 1 bead
            self.beads[self.chosen] += 1
            if self.beads[self.chosen] == 1:
                self.colours += 1
        elif result == 2:  # if menace won put 3 beads
            self.beads[self.chosen] += 3
            if self.beads[self.chosen] == 3:
                self.colours += 1
        # if menace lost nothing happen
