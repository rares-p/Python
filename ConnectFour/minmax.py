import copy


class MinMax:
    def __init__(self, board):
        self.board = copy.deepcopy(board)
        self.height = len(board)
        self.width = len(board[0])
        pass

    def evaluate(self, board):
        rez = 0
        # principal diag
        for i in range(self.height - 4):
            for j in range(self.width - 4):
                values = [self.board[i + k][self.board[j + k]] for k in range(4)]


if __name__ == "__main__":
    print("DA")
