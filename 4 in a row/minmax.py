import copy
import sys

PLAYER = 0
COMPUTER = 1
DEPTHS = [1, 3, 6]


class MinMax:
    def __init__(self, board, level):
        self.board = copy.deepcopy(board)
        self.height = len(board)
        self.width = len(board[0])
        self.depth = DEPTHS[int(level) - 1]
        pass

    def is_game_over(self, board):
        for i in range(self.height - 3):
            for j in range(self.width - 3):
                values = [board[i + k][j + k] for k in range(4)]
                if values.count(PLAYER) == 4 or values.count(COMPUTER) == 4:
                    return True

        # secondary diag
        for i in range(self.height - 3):
            for j in range(3, self.width):
                values = [board[i + k][j - k] for k in range(4)]
                if values.count(PLAYER) == 4 or values.count(COMPUTER) == 4:
                    return True

        # vertical
        for i in range(self.height - 3):
            for j in range(self.width):
                values = [board[i + k][j] for k in range(4)]
                if values.count(PLAYER) == 4 or values.count(COMPUTER) == 4:
                    return True

        # horizontal
        for i in range(self.height):
            for j in range(self.width - 3):
                values = [board[i][j + k] for k in range(4)]
                if values.count(PLAYER) == 4 or values.count(COMPUTER) == 4:
                    return True

    def evaluate(self, board):
        rez = 0
        # principal diag
        for i in range(self.height - 3):
            for j in range(self.width - 3):
                values = [board[i + k][j + k] for k in range(4)]
                if PLAYER in values:
                    if not (COMPUTER in values):
                        rez -= values.count(PLAYER) ** 3
                else:
                    rez += values.count(COMPUTER) ** 3

        # secondary diag
        for i in range(self.height - 3):
            for j in range(3, self.width):
                values = [board[i + k][j - k] for k in range(4)]
                if PLAYER in values:
                    if not (COMPUTER in values):
                        rez -= values.count(PLAYER) ** 3
                else:
                    rez += values.count(COMPUTER) ** 3

        # vertical
        for i in range(self.height - 3):
            for j in range(self.width):
                values = [board[i + k][j] for k in range(4)]
                if PLAYER in values:
                    if not (COMPUTER in values):
                        rez -= values.count(PLAYER) ** 3
                else:
                    rez += values.count(COMPUTER) ** 3

        # horizontal
        for i in range(self.height):
            for j in range(self.width - 3):
                values = [board[i][j + k] for k in range(4)]
                if PLAYER in values:
                    if not (COMPUTER in values):
                        rez -= values.count(PLAYER) ** 3
                else:
                    rez += values.count(COMPUTER) ** 3
        return rez

    def get_next_moves(self, board, turn):
        boards = []
        for j in range(self.width):
            for i in range(self.height - 1, -1, -1):
                if board[i][j] is None:
                    new_board = copy.deepcopy(board)
                    new_board[i][j] = turn
                    boards.append((new_board, j))
                    break
        return boards

    def get_best_move(self):
        best_move_index = -1
        best_move_score = -sys.maxsize
        for move, index in self.get_next_moves(self.board, COMPUTER):
            move_score = self.minmax(move, self.depth, -sys.maxsize, sys.maxsize, False)
            if move_score > best_move_score:
                best_move_index = index
                best_move_score = move_score
        return best_move_index

    def minmax(self, board, depth, alpha, beta, max_player):
        if depth == 0 or self.is_game_over(board):
            return self.evaluate(board)

        if max_player:
            max_eval = -sys.maxsize
            for move, _ in self.get_next_moves(board, COMPUTER):
                current_eval = self.minmax(move, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, current_eval)
                alpha = max(alpha, current_eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = sys.maxsize
            for move, _ in self.get_next_moves(board, PLAYER):
                current_eval = self.minmax(move, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, current_eval)
                beta = min(beta, current_eval)
                if beta <= alpha:
                    break
            return min_eval
