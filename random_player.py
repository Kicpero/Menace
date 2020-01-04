from random import randint
from random import seed


class PlayerRandom:
    def __init__(self):
        print("I'm a random player!")
        seed(1000)

    def move(self, board):
        pos = self.check_winner_move(board)
        if pos >= 0:  # if there is a winning position choose that
            return pos
        else:  # if there is a no winning position randomize
            while pos < 0:
                tmp = randint(0, 8)
                if board[tmp] == 0:
                    pos = tmp
            if pos == -1:
                raise ValueError("ERROR in randomization")
            return pos

    def check_winner_move(self, board):
        for i in range(0, 3):
            # check winning position in a row
            if board[3 * i] + board[3 * i + 1] + board[3 * i + 2] == 4:
                if board[3 * i] == 0:
                    return 3 * i
                elif board[3 * i + 1] == 0:
                    return 3 * i + 1
                elif board[3 * i + 2] == 0:
                    return 3 * i + 2
        for i in range(0, 3):
            # check winning position in a column
            if board[i] + board[i + 3] + board[i + 6] == 4:
                if board[i] == 0:
                    return i
                elif board[i + 3] == 0:
                    return i + 3
                elif board[i + 6] == 0:
                    return i + 6
        # check winning position in a right cross
        if board[0] + board[4] + board[8]:
            if board[0] == 0:
                return 0
            elif board[4] == 0:
                return 4
            elif board[8] == 0:
                return 8
        # check winning position in a left cross
        if board[2] + board[4] + board[5]:
            if board[2] == 0:
                return 2
            elif board[4] == 0:
                return 4
            elif board[5] == 0:
                return 5
        return -1
