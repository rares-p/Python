import sys


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
    width = args[2]
    height = args[3]
    if not isinstance(width, int) or not isinstance(height, int):
        print("Only integers allowed for width and height")
        exit(-1)
    if width < 4 or height < 4:
        print("Height or with cannot be less than 4")
        exit(-1)
    first_player = None
    if opponent_type == "human" and size == 5:
        print("First player specification is redundant since the opponent is human.\n")
    elif size == 5:
        first_player = args[4]

    return opponent_type, width, height, first_player


if __name__ == '__main__':
    data = read_input(sys.argv)
