from copy import deepcopy
from sys import argv
import pygame
from minmax import MinMax, is_game_over

BLUE = (50, 98, 168)
BEIGE = (250, 233, 177)
RED = (245, 66, 66)
YELLOW = (242, 245, 66)


def read_input(args):
    """
    Reads command line arguments and validates them

    :param args: Contains parameters for the game session
    :return: All the necessary data for a game session
    """
    size = len(args)
    if size < 4 or size > 5:
        print(
            "Incorrect number of arguments. Correct usage is: 4inaROW.py "
            "<opponent type> <board width>"
            "<board height> [firstPlayer]\nEX: 4inaROW.py computer2 7 5 "
            "human\nEX: 4inaROW.py human 7 5\nOpponent"
            "types are: human/computer1/computer2/computer3 (where 1 2 3 are "
            "difficulties in ascending order)")
        exit(-1)
    opponent_type = args[1]
    if opponent_type not in ["human", "computer1", "computer2", "computer3"]:
        print(
            "Incorrect opponent type. Available types are: "
            "human/computer1/computer2/computer3 (where 1 2 3 are"
            "difficulties in ascending order)")
        exit(-1)
    width = int(args[2])
    height = int(args[3])
    if not isinstance(width, int) or not isinstance(height, int):
        print("Only integers allowed for width and height")
        exit(-1)
    if width < 4 or height < 4:
        print("Height or with cannot be less than 4")
        exit(-1)
    first_player = None
    if opponent_type == "human":
        if size == 5:
            print(
                "First player specification is redundant since the opponent "
                "is human.\n")
    elif size == 5:
        first_player = args[4]
        if first_player not in ["human", "computer"]:
            print("First player types are: 'human'/'computer'")
            exit(-1)
    return opponent_type, width, height, first_player


class FourInARow:
    """
    Class that represents and updates a game session

    Attributes:
        computer (bool): Whether the second players is human or AI
        screen (window): The pygame window
        font (font): Font used in the pygame window
        first_player (str): Who is the first to play in a human vs AI game
        width (int): The width of the window
        height (int): The height of the window
        window_scale (int): The scale of the window
        header (int): The size of the header
        margin (int): The margin between cells
        board (int): The board that represents the current state of the game
        minmax (MinMax): Object that gives the next move of the AI based on
                         difficulty
        window_header (int): the width of the header in pixels
        window_width (int): the width of the window in pixels
        window_height (int): the height of the window in pixels
    """

    def __init__(self, opponent_type: str, width: int, height: int,
                 first_player: str):
        """
        Initialize a Four in a Row session

        :param opponent_type: Whether the second players is human or AI
        :param width: The width of the board in cells
        :param height: The height of the board in cells
        :param first_player: Who is the first to play in a human vs AI game
        """
        self.computer = False
        self.screen = None
        self.font = None
        self.first_player = None
        self.width = width
        self.height = height
        self.window_scale = 100
        self.header = 1
        self.margin = 10
        self.board = [[None for _ in range(width)] for _ in range(height)]
        if opponent_type.startswith("computer"):
            self.computer = True
            self.minmax = MinMax(self.board, opponent_type[-1])
            if first_player == "computer":
                self.first_player = "computer"
        self.window_header = self.header * self.window_scale
        self.window_width = self.width * self.window_scale
        self.window_height = (self.height * self.window_scale
                              + self.window_header)
        self.initial_setup()

    def initial_setup(self):
        """
        Initializes the window and the board for the game session
        """
        pygame.init()
        pygame.display.set_caption("4 in a row")
        self.font = pygame.font.SysFont("Comic Sans MS", 36)
        self.screen = pygame.display.set_mode((self.window_width,
                                               self.window_height))
        self.screen.fill(BLUE)
        pygame.draw.rect(self.screen, BEIGE,
                         (0, 0, self.window_width, self.window_header))
        for i in range(self.width):
            for j in range(self.header, self.height + self.header):
                pygame.draw.circle(self.screen, BEIGE, (i
                                                        * self.window_scale
                                                        + self.window_scale
                                                        // 2,
                                                        j
                                                        * self.window_scale
                                                        + self.window_scale
                                                        // 2),
                                   self.window_scale
                                   / 2
                                   - self.margin)
        pygame.display.update()

    def move(self, x, opp):
        """
        Performs the next move in the game

        :param x: The column where the next piece is placed
        :param opp: Which player performs the move
        """
        y = None
        for i in range(self.height - 1, -1, -1):
            if self.board[i][x] is None:
                y = i
                break
        if y is None:
            return -1
        self.board[y][x] = opp
        color = YELLOW if opp == 0 else RED
        pygame.draw.circle(self.screen, color, (
            x * self.window_scale + self.window_scale // 2,
            y * self.window_scale + self.window_scale // 2 +
            self.window_header),
                           self.window_scale / 2 - self.margin)
        pygame.display.update()

    def update_turn_text(self, opp):
        """
        Computes the text in the header to specify who's turn is now

        :param opp: The next player to move
        """
        color = YELLOW if opp == 0 else RED
        if self.computer:
            if opp == 0:
                display_text = "Your Turn"
            else:
                display_text = "Computer's Turn"
        else:
            display_text = f"Player{opp + 1}'s Turn"
        self.display_text(display_text, color)
        pygame.display.update()

    def display_text(self, display_text, color):
        """
        Updates the text in the header to specify who's turn is now

        :param display_text: The text that contains the player to move
        :param color: The color of the player
        """
        pygame.draw.rect(self.screen, BEIGE, (0,
                                              0,
                                              self.window_width,
                                              self.window_header))
        text = self.font.render(display_text, True, color, (10, 10, 10))
        textRect = text.get_rect()
        textRect.center = (self.window_width // 2, self.window_header // 2)
        self.screen.blit(text, textRect)
        pygame.display.update()

    def check_game_over(self, turn):
        """
        Checks if the game is over. If so, it displays a message

        :param turn: The next player to move
        :return: True is the game is over, False otherwise
        """
        if is_game_over(self.board):
            if turn:
                if self.computer:
                    self.display_text("You win!!!", YELLOW)
                else:
                    self.display_text("Player 1 wins!!!", YELLOW)
            else:
                if self.computer:
                    self.display_text("Computer wins!!!", RED)
                else:
                    self.display_text("Player 2 wins!!!", RED)
            return True
        return False

    def run(self):
        """
        Simulates the game, checking for moves
        """
        over = False
        running = True
        turn = 0
        self.update_turn_text(turn)
        if self.first_player == "computer":
            turn = 1
            self.update_turn_text(turn)
            self.minmax.board = deepcopy(self.board)
            best_pc = self.minmax.get_best_move()
            self.move(best_pc, turn)
            turn = 1 - turn
            self.update_turn_text(turn)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and not over:
                    if event.button == 1:
                        if (self.move(event.pos[0] // self.window_scale, turn)
                                != -1):
                            turn = 1 - turn
                            if self.check_game_over(turn):
                                over = True
                                break
                            self.update_turn_text(turn)
                            if self.computer:
                                self.minmax.board = deepcopy(self.board)
                                best_pc = self.minmax.get_best_move()
                                self.move(best_pc, turn)
                                turn = 1 - turn
                                if self.check_game_over(turn):
                                    over = True
                                    break
                                self.update_turn_text(turn)
                pygame.event.clear()
        pygame.display.update()


if __name__ == '__main__':
    opponent, w, h, first = read_input(argv)
    instance = FourInARow(opponent, w, h, first)
    instance.run()
