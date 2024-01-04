import copy

PLAYER = 0
COMPUTER = 1


class MinMax:
    def __init__(self, board):
        self.board = copy.deepcopy(board)
        self.height = len(board)
        self.width = len(board[0])
        pass


    def is_game_over(self):
        for i in range(self.height - 3):
            for j in range(self.width - 3):
                values = [self.board[i + k][j + k] for k in range(4)]
                if values.count(PLAYER) == 4 or values.count(COMPUTER) == 4:
                    return True

        # secondary diag
        for i in range(self.height - 3):
            for j in range(3, self.width):
                values = [self.board[i + k][j - k] for k in range(4)]
                if values.count(PLAYER) == 4 or values.count(COMPUTER) == 4:
                    return True

        # vertical
        for i in range(self.height - 3):
            for j in range(self.width):
                values = [self.board[i + k][j] for k in range(4)]
                if values.count(PLAYER) == 4 or values.count(COMPUTER) == 4:
                    return True

        # horizontal
        for i in range(self.height):
            for j in range(self.width - 3):
                values = [self.board[i][j + k] for k in range(4)]
                if values.count(PLAYER) == 4 or values.count(COMPUTER) == 4:
                    return True

    def evaluate(self, board):
        rez = 0
        # principal diag
        for i in range(self.height - 3):
            for j in range(self.width - 3):
                values = [self.board[i + k][j + k] for k in range(4)]
                if PLAYER in values:
                    if not (COMPUTER in values):
                        rez += values.count(PLAYER)
                else:
                    rez -= values.count(COMPUTER)

        # secondary diag
        for i in range(self.height - 3):
            for j in range(3, self.width):
                values = [self.board[i + k][j - k] for k in range(4)]
                if PLAYER in values:
                    if not (COMPUTER in values):
                        rez += values.count(PLAYER)
                else:
                    rez -= values.count(COMPUTER)

        # vertical
        for i in range(self.height - 3):
            for j in range(self.width):
                values = [self.board[i + k][j] for k in range(4)]
                if PLAYER in values:
                    if not (COMPUTER in values):
                        rez += values.count(PLAYER)
                else:
                    rez -= values.count(COMPUTER)

        # horizontal
        for i in range(self.height):
            for j in range(self.width - 3):
                values = [self.board[i][j + k] for k in range(4)]
                if PLAYER in values:
                    if not (COMPUTER in values):
                        rez += values.count(PLAYER)
                else:
                    rez -= values.count(COMPUTER)
        return rez

    def minmax(self, board, depth, alpha, beta, max_player):
        if depth == 0 or


