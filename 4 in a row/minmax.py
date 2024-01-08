import copy
import sys

PLAYER = 0
COMPUTER = 1
DEPTHS = [0, 3, 6]
WEIGHTS = [0, 3, 30, 75, 170]


def is_game_over(board):
    """
    Checks if the game is over. If so, it displays a message

    :param board: The current state of the board
    :return: True is the game is over, False otherwise
    """
    height = len(board)
    width = len(board[0])
    for i in range(height - 3):
        for j in range(width - 3):
            values = [board[i + k][j + k] for k in range(4)]
            if values.count(PLAYER) == 4 or values.count(COMPUTER) == 4:
                return True

    # secondary diag
    for i in range(height - 3):
        for j in range(3, width):
            values = [board[i + k][j - k] for k in range(4)]
            if values.count(PLAYER) == 4 or values.count(COMPUTER) == 4:
                return True

    # vertical
    for i in range(height - 3):
        for j in range(width):
            values = [board[i + k][j] for k in range(4)]
            if values.count(PLAYER) == 4 or values.count(COMPUTER) == 4:
                return True

    # horizontal
    for i in range(height):
        for j in range(width - 3):
            values = [board[i][j + k] for k in range(4)]
            if values.count(PLAYER) == 4 or values.count(COMPUTER) == 4:
                return True
    return False


class MinMax:
    """
    Class that gives the next move of the AI based on the difficulty

    Attributes:
        _board (list[list[int]]): The current state of the game
        _height (int): The height of the board in cells
        _width (int): The width of the board in cells
        _depth (int): The depth of the minmax algorithm
    """

    def __init__(self, board, level):
        """
        Initializes all the parameters necessary for computing next moves

        :param board: The current state of the game
        :param level: The difficulty. Higher level means higher difficulty
        """
        self._board = copy.deepcopy(board)
        self._height = len(board)
        self._width = len(board[0])
        self._depth = DEPTHS[int(level) - 1]
        pass

    def evaluate(self, board):
        """
        Computes how good a state of the game is for the AI

        :param board: The current state of the game
        :returns rez: higher means better position
        """
        rez = 0
        # principal diag
        for i in range(self._height - 3):
            for j in range(self._width - 3):
                values = [board[i + k][j + k] for k in range(4)]
                if PLAYER in values:
                    if not (COMPUTER in values):
                        rez -= WEIGHTS[values.count(PLAYER)]
                else:
                    rez += WEIGHTS[values.count(COMPUTER)]

        # secondary diag
        for i in range(self._height - 3):
            for j in range(3, self._width):
                values = [board[i + k][j - k] for k in range(4)]
                if PLAYER in values:
                    if not (COMPUTER in values):
                        rez -= WEIGHTS[values.count(PLAYER)]
                else:
                    rez += WEIGHTS[values.count(COMPUTER)]

        # vertical
        for i in range(self._height - 3):
            for j in range(self._width):
                values = [board[i + k][j] for k in range(4)]
                if PLAYER in values:
                    if not (COMPUTER in values):
                        rez -= WEIGHTS[values.count(PLAYER)]
                else:
                    rez += WEIGHTS[values.count(COMPUTER)]

        # horizontal
        for i in range(self._height):
            for j in range(self._width - 3):
                values = [board[i][j + k] for k in range(4)]
                if PLAYER in values:
                    if not (COMPUTER in values):
                        rez -= WEIGHTS[values.count(PLAYER)]
                else:
                    rez += WEIGHTS[values.count(COMPUTER)]
        return rez

    def get_next_moves(self, board, turn):
        """
        Computes how good a state of the game is for the AI

        :param board: The current state of the game
        :param turn: The next player to move
        :returns boards: A list that contains all te next possible states of
                         the game, sorted from the best for the AI to the worst
        """
        boards = []
        for j in range(self._width):
            for i in range(self._height - 1, -1, -1):
                if board[i][j] is None:
                    new_board = copy.deepcopy(board)
                    new_board[i][j] = turn
                    boards.append((new_board, j))
                    break
        return sorted(boards, key=lambda x: self.evaluate(x[0]))

    def get_best_move(self):
        """
        Computes the move chosen by the AI

        :returns best_move_index: The index of the column the AI will place its
                                  next piece
        """
        best_move_index = -1
        best_move_score = -sys.maxsize
        for move, index in self.get_next_moves(self._board, COMPUTER):
            move_score = self.minmax(move,
                                     self._depth,
                                     -sys.maxsize,
                                     sys.maxsize,
                                     False)
            if move_score > best_move_score:
                best_move_index = index
                best_move_score = move_score
        return best_move_index

    def minmax(self, board, depth, alpha, beta, max_player):
        """
        MinMax algorith to compute the next move for the AI

        :param board: The current state of the game
        :param depth: The depth of the algorithm
        :param alpha: Threshold for the best move for the maximizer
        :param beta: Threshold for the best move for the minimizer
        :param max_player: If the current player wants to maximize or minimize
                           the score of the next move

        :returns best_move: The best score that a player can get from the
                            current position based on the depth
        """
        if depth == 0 or is_game_over(board):
            return self.evaluate(board)

        if max_player:
            max_eval = -sys.maxsize
            for move, _ in self.get_next_moves(board, COMPUTER):
                current_eval = self.minmax(move,
                                           depth - 1,
                                           alpha,
                                           beta,
                                           False)
                max_eval = max(max_eval, current_eval)
                alpha = max(alpha, current_eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = sys.maxsize
            for move, _ in self.get_next_moves(board, PLAYER):
                current_eval = self.minmax(move,
                                           depth - 1,
                                           alpha,
                                           beta,
                                           True)
                min_eval = min(min_eval, current_eval)
                beta = min(beta, current_eval)
                if beta <= alpha:
                    break
            return min_eval
