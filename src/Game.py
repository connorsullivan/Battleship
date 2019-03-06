
import sys

from Board import Board
from Opponent import Opponent
from Position import Position
from Position import InvalidPosition

# Gets user input and translates it into a position to attack on the opponent's board
# (Board is passed in to show to the user during input)
def get_move_from_user(board):

    # Loop while getting user input
    while True:

        # Show the player's board
        print(board)

        user_input = input('\nSelect a target on your opponent\'s board (example: A5) (\'quit\' to end game): ')

        # Capitalize the input
        user_input = user_input.upper()

        # If the user decides to exit the game
        if user_input == 'QUIT':
            print('\nQuitting game. Good-bye!')
            sys.exit(0)

        # Make sure the length of the input is 2 characters
        if len(user_input) != 2:
            print('\nChoice must be two characters (example: A5)')
            continue

        try:
            return Position(user_input[0], user_input[1])
        except InvalidPosition:
            continue

if __name__ == "__main__":

    print('\nWelcome to Battleship!')

    # Generate a board for both players (0 = user, 1 = cpu)
    player_1_board = Board(0)
    player_2_board = Board(1)

    # Generate an opponent for the player to compete against
    opponent = Opponent()

    # Main game loop
    while True:

        # Get a target position from the user
        target_position = get_move_from_user(player_1_board)

        # Attack the opponent's board at the given position
        player_2_board.attack(target_position)

        # Opponent generates a position to attack
        target_position = opponent.generate_move()

        # Attack the user's board at the given position
        player_1_board.attack(target_position)
