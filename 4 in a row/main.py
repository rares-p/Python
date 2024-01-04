import sys
import time

import pygame

BLUE = (50, 98, 168)
BEIGE = (250, 233, 177)
RED = (245, 66, 66)
YELLOW = (242, 245, 66)


def read_input(args):
    size = len(args)
    if size < 4 or size > 5:
        print("Incorrect number of arguments. Correct usage is: 4inaROW.py <opponent type> <board width> "
              "<board height> [firstPlayer]\nEX: 4inaROW.py computer 7 5 human\nEX: 4inaROW.py human 7 5\nOpponent "
              "types are: human/computer1/computer2/computer3 (where 1 2 3 are difficulties in ascending order)")
        exit(-1)
    opponent_type = args[1]
    if opponent_type not in ["human", "computer1", "computer2", "computer3"]:
        print("Incorrect opponent type. Available types are: human/computer1/computer2/computer3 (where 1 2 3 are "
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
            print("First player specification is redundant since the opponent is human.\n")
    elif size == 5:
        first_player = args[4]
        if first_player not in ["human", "computer"]:
            print("First player types are: 'human'/'computer'")
            exit(-1)

    return opponent_type, width, height, first_player


class FourInARow:
    def __init__(self, opponent_type: str, width: int, height: int, first_player: str):
        self.opponent_type = opponent_type
        self.screen = None
        self.font = None
        self.first_player = None
        self.second_player = None
        self.width = width
        self.height = height
        self.window_scale = 100
        self.header = 1
        self.margin = 10
        self.board = [[None for _ in range(width)] for _ in range(height)]
        self.window_header = self.header * self.window_scale
        self.window_width = self.width * self.window_scale
        self.window_height = self.height * self.window_scale + self.window_header
        if opponent_type.startswith("computer"):
            if first_player == "human":
                self.first_player = "Your"  # TODO: DE VAZUT DACA SA RAMANA ASA
                self.second_player = "Computer's"
            else:
                self.first_player = ""
        self.initial_setup()

    def initial_setup(self):
        pygame.init()
        pygame.display.set_caption("4 in a row")
        self.font = pygame.font.SysFont("Comic Sans MS", 36)
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.screen.fill(BLUE)
        pygame.draw.rect(self.screen, BEIGE, (0, 0, self.window_width, self.window_header))
        for i in range(self.width):
            for j in range(self.header, self.height + self.header):
                pygame.draw.circle(self.screen, BEIGE, (i * self.window_scale + self.window_scale // 2, j *
                                                        self.window_scale + self.window_scale // 2),
                                   self.window_scale / 2 - self.margin)
        pygame.display.update()
        self.run()

    def move(self, x, opp):
        print(self.board)
        y = None
        for i in range(self.height - 1, -1, -1):
            if self.board[i][x] is None:
                y = i
                break
        if y is None:
            return -1
        print(y)
        self.board[y][x] = opp
        print(self.board)
        color = YELLOW if opp == 0 else RED
        pygame.draw.circle(self.screen, color, (
            x * self.window_scale + self.window_scale // 2,
            y * self.window_scale + self.window_scale // 2 + self.window_header),
                           self.window_scale / 2 - self.margin)

    def update_turn_text(self, opp):
        display_text = None
        color = YELLOW if opp == 0 else RED
        pygame.draw.rect(self.screen, BEIGE, (0, 0, self.window_width, self.window_header))
        if self.opponent_type.startswith("computer"):
            if opp == 0:
                display_text = "Your Turn"
            else:
                display_text = "Computer's Turn"
        else:
            display_text = f"Player{opp + 1}'s Turn"
        text = self.font.render(display_text, True, color, (10, 10, 10))
        textRect = text.get_rect()
        textRect.center = (self.window_width // 2 + self.margin, self.window_header // 2)
        self.screen.blit(text, textRect)
        pygame.display.update()

    def run(self):
        running = True
        turn = 0
        self.update_turn_text(turn)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Mouse clicked at:", event.pos)
                        if self.move(event.pos[0] // self.window_scale, turn) != -1:
                            turn = 1 - turn
                            self.update_turn_text(turn)
                            print(self.board)

        pygame.display.update()


if __name__ == '__main__':
    opponent, w, h, first = read_input(sys.argv)
    instance = FourInARow(opponent, w, h, first)
