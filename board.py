class Board:
    board = [0] * 9  # inicialize board as array
    free_spaces = 9  # remaining free spaces

    def copy_board(self, board):
        self.board = board.get_board().copy()

    def get_value_xy(self, x, y):
        x = int(x)
        y = int(y)
        if x > 3 or x < 1 or y < 1 or y > 3:
            raise ValueError("Such position does not exist on the board!")
        return self.board[x + 3 * (y - 1) - 1]
        # |y\x|1|2|3|
        # |1  |o o o
        # |2  |o o o
        # |3  |o o o

    def get_value_pos(self, pos):
        if pos > 8 or pos < 0:
            raise ValueError("ERROR: Such position does not exist on the board!")
        return self.board[pos]

    def set_value_xy(self, x, y, value):
        x = int(x)
        y = int(y)
        if x > 3 or x < 1 or y < 1 or y > 3:
            raise ValueError("ERROR: Such position does not exist on the board!")
        if value not in [0, 1, 2]:
            raise ValueError("ERROR: Wrong value on the board!")
        self.board[x + 3 * (y - 1) - 1] = value
        self.free_spaces -= 1

    def set_value_pos(self, position, value):
        position = int(position)
        if position > 8 or position < 0:
            raise ValueError("ERROR: Such position does not exist on the board!")
        if value not in [0, 1, 2]:
            raise ValueError("ERROR: Wrong value on the board!")
        self.board[position] = value
        self.free_spaces -= 1

    def check_winner_xy(self, x, y):
        # x - x position of last move
        # y - y position of last move
        # returns 1 if player won
        # returns 0 if player lost
        x = int(x)
        y = int(y)
        if self.board[3 * (y - 1)] == self.board[3 * (y - 1) + 1] == self.board[3 * (y - 1) + 2]:  # horizontal
            return 0
        if self.board[x - 1] == self.board[x + 2] == self.board[x + 5]:  # vertical
            return 0
        if (x == 1 and y == 1) or (x == 2 and y == 2) or (x == 3 and y == 3):  # right cross
            if self.board[0] == self.board[4] == self.board[8]:
                return 0
        if (x == 1 and y == 3) or (x == 3 and y == 1) or (x == 2 and y == 2):  # left cross
            if self.board[2] == self.board[4] == self.board[6]:
                return 0
        return 1

    def check_winner(self, pos):
        pos = int(pos)
        if pos < 3:  # checking first row
            if self.board[0] == self.board[1] == self.board[2]:
                return 0
        elif pos < 6:  # checking second row
            if self.board[4] == self.board[3] == self.board[5]:
                return 0
        else:  # checking third row
            if self.board[6] == self.board[7] == self.board[8]:
                return 0
        if pos in [0, 3, 6]:  # checking first column
            if self.board[0] == self.board[3] == self.board[6]:
                return 0
        elif pos in [1, 4, 7]:  # checking second column
            if self.board[1] == self.board[4] == self.board[7]:
                return 0
        if pos in [2, 5, 8]:  # checking third column
            if self.board[2] == self.board[5] == self.board[8]:
                return 0
        if pos in [0, 4, 8]:  # checking right cross
            if self.board[0] == self.board[4] == self.board[8]:
                return 0
        if pos in [2, 4, 6]:  # checking left cross
            if self.board[2] == self.board[4] == self.board[6]:
                return 0
        if self.free_spaces == 0:
            return -1
        return 1

    def print_board(self):
        for i in range(0, 3):
            print(self.board[3 * i:3 * i + 3])
        print("\n")

    def get_board(self):
        return self.board

    def clean(self):
        for i in range(0, 9):
            self.board[i] = 0
        self.free_spaces = 9
