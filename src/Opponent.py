
import random

from Position import Position

class Opponent:

    def __init__(self):

        # Reference of previous moves (so as not to repeat moves)
        self.board = [[0 for c in range(10)] for r in range(10)]

    # Generates a position to attack
    def generate_move(self):

        found_position = False

        while not found_position:

            # Randomly select a position to attack
            selected_row = random.randint(0, 9)
            selected_col = random.randint(0, 9)

            # Check that the position hasn't been attacked yet
            if not self.board[selected_row][selected_col]:

                # Mark this position as used for future moves
                self.board[selected_row][selected_col] = 1

                # Break from the loop
                found_position = True

        chosen_position = Position(selected_col, selected_row)

        return chosen_position
