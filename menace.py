from box import Box
from board import Board


class Menace:
    # Array of boxes
    boxes = {'000000000': Box(0, board=[0, 0, 0, 0, 0, 0, 0, 0, 0])}

    # array of chosen boxes in single game
    chosen = ['000000000', '000000000', '000000000', '000000000']

    # last modified:
    last = -1

    def __init__(self):
        print("I'm the menace - learning machine")

    # returns the position where MENACE wants to move
    # if return = -1 then no more beads
    def move(self, board):
        if self.last == 3:  # if it is last move
            for i in range(0, 9):
                if board.get_board()[i] == 0:
                    position = i
                    return position
        str1 = ''
        for i in range(0, 9):  # creating name of the box
            str1 += str(board.get_board()[i])
        if str1 not in self.boxes:  # if this box doesn't exist create new box
            new_board = Board()
            new_board.copy_board(board)
            self.boxes[str1] = Box(1, new_board)
        self.last += 1
        self.chosen[self.last] = str1
        position = self.boxes[str1].move()
        return position

    # return:
    # True - the box with such positions already exists
    # False - the box with such positions doesn't exist
    def check_box(self, board):
        str1 = ''
        for i in range(0, 9):
            str1 += str(board[i])
        print(str1)
        return str1 in self.boxes

    # send reward
    # loser = 0
    # drawer = 1
    # winner = 2
    def reward(self, result):
        for i in range(0, self.last + 1):
            self.boxes[self.chosen[i]].modify_beads(result)

    def clean(self):
        self.chosen = ['000000000', '000000000', '000000000', '000000000']
        self.last = -1
