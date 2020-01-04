from board import Board
from menace import Menace
from random_player import PlayerRandom


class Game:
    p1 = 9  # menace starts game
    p2 = 8  # random player is second
    board = Board()  # board initialization
    menace = Menace()  # menace initialization
    player_random = PlayerRandom()  # player initialization

    def play(self):
        self.prepare_game()
        while self.p1 > 0:
            score = self.move()  # returning 0, 1 or -1
            if score == 0:
                if self.p1 < self.p2:
                    print("Player 1 wins")
                    self.menace.reward(2)
                    return 1
                else:
                    print("Player 2 wins")
                    self.menace.reward(0)
                    return 2
            elif score == -1:
                print("It's a draw")
                self.menace.reward(1)
                return 0

    # values of P1 are 1's
    # values of P2 are 2's
    # return score:
    # 0 - player 1 or player 2 win
    # 1 - no winner yet
    # -1 - draw
    def move(self):
        if self.p1 > self.p2:
            self.p1 -= 2
            pos = self.menace.move(self.board)  # menace move
            if pos == -1:
                return -1
            self.board.set_value_pos(pos, 1)  # place a one
        else:
            self.p2 -= 2
            pos = self.player_random.move(self.board.get_board())  # player move
            if pos == -1:
                return -1
            self.board.set_value_pos(pos, 2)  # place a two

        # self.board.print_board()
        return self.board.check_winner(pos)  # check if sb won

    def prepare_game(self):
        self.board.clean()
        self.p1 = 9
        self.p2 = 8
        self.menace.clean()
