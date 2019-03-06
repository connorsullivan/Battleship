
import random
import sys
import time

from Battleship import Battleship

class Board:

    def __init__(self, player):

        # The owner of this board
        self.player = player

        # The game board (2D list, 10x10)
        self.board = [[0 for c in range(10)] for r in range(10)]

        # A copy of the game board that shows positions that have already been attacked
        self.board_attacked = [[0 for c in range(10)] for r in range(10)]

        # The battleships on the board
        self.ships = []

        # Add battleships to the board
        # (the int parameter is the size of the battleship)
        self.add_ship(4)
        self.add_ship(3)
        self.add_ship(3)
        self.add_ship(2)
        self.add_ship(2)
        self.add_ship(2)
        self.add_ship(1)
        self.add_ship(1)
        self.add_ship(1)
        self.add_ship(1)

    def __repr__(self):

        repr = '\nHere is your board:\n'

        repr += '\n  A B C D E F G H I J\n'

        for row in range(10):
            repr += '{} '.format(row)

            for col in range(10):

                if self.board[row][col] == 0:
                    repr += '~'
                else:
                    repr += 'x'

                if col < 9:
                    repr += ' '

            if row < 9:
                repr += '\n'

        return repr

    # Add a battleship to the board
    def add_ship(self, size):

        # Create the battleship
        ship = Battleship(size)

        # Set the limits on where the ship can be safely placed
        min_row = size - 1
        min_col = size - 1
        max_row = 10 - size
        max_col = 10 - size

        placed_ship = False

        # Try to place the ship
        while not placed_ship:

            # Generate a random coordinate as a starting point
            selected_row = random.randint(min_row, max_row)
            selected_col = random.randint(min_col, max_col)

            curr_row, curr_col = selected_row, selected_col

            # Pick a random direction to insert the ship
            # (1 = North, 2 = South, 3 = East, 4 = West)
            direction = random.randint(1, 4)

            placed_ship = True

            # First, check the path of the ship to see if anything is blocking it
            for i in range(0, size):

                # Check if the current cell is occupied
                if not self.check_space(curr_row, curr_col):
                    placed_ship = False
                    break

                # North
                if direction == 1:
                    curr_row -= 1

                # South
                elif direction == 2:
                    curr_row += 1

                # East
                elif direction == 3:
                    curr_col += 1

                # West
                else:
                    curr_col -= 1

            # Then, place the ship if nothing is blocking its path
            if placed_ship:

                curr_row, curr_col = selected_row, selected_col

                for i in range(0, size):

                    # Mark this cell as taken
                    self.board[curr_row][curr_col] = 1

                    # Add this cell to the ship's location array
                    ship.add_cell(curr_row, curr_col)

                    # North
                    if direction == 1:
                        curr_row -= 1

                    # South
                    elif direction == 2:
                        curr_row += 1

                    # East
                    elif direction == 3:
                        curr_col += 1

                    # West
                    else:
                        curr_col -= 1

                # Add this ship to the board
                self.ships.append(ship)

    # Remove a battleship from the board
    def rem_ship(self, ship):
        self.ships = [x for x in self.ships if x != ship]

    # Check if a board cell (and its immediate neighbors) are occupied
    def check_space(self, row, col):

        # Check the cell and its immediate neighbors (8)
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                try:

                    # If any cell is occupied, return False
                    if self.board[r][c] == 1:
                        return False

                except IndexError:
                    pass

        # If no cells are occupied, return True
        return True

    # Launch an attack against one of this board's positions
    def attack(self, position):

        # Check the owner of the board
        if self.player == 0:
            print('\nYour opponent launches an attack on position {}!'.format(position))
        else:
            print('\nYou launch an attack on position {}!'.format(position))

        # Sleep for a few seconds to add some realism to the game
        time.sleep(3)

        # Check if the cell has already been attacked
        if self.board_attacked[position.row][position.col]:
            print('\nThat position has already been attacked!')

        # If the cell contains a ship
        elif self.board[position.row][position.col]:

            print('\nHit!')

            # Check to see which ship was hit
            for ship in self.ships:

                # If the current ship was the one hit
                if ship.rem_cell(position.row, position.col):

                    # If the ship was destroyed
                    if ship.is_destroyed():

                        # Remove the ship from the board
                        self.rem_ship(ship)

                        # If there are no more ships on the board (game over condition)
                        if not self.ships:

                            # Decide who won/lost the game
                            if self.player == 0:
                                print('\nGame over! All of your battleships have been destroyed :(')
                            else:
                                print('\nVictory! You have destroyed all of your opponent\'s battleships!')

                            # Exit the program
                            sys.exit(0)

                        # If there are still other ships on the board
                        else:

                            print('\nBattleship sunk!', end=' ')

                            if self.player == 0:
                                print('You have {} ship(s) remaining on the board.'.format(len(self.ships)))
                            else:
                                print('Your opponent has {} ship(s) remaining on the board.'.format(len(self.ships)))

                    # Break from the ship iteration loop
                    break

            # Mark the cell as empty
            self.board[position.row][position.col] = 0

        # If the cell doesn't contain a ship
        else:
            print('\nMiss!')

        # Mark the cell as being attacked (even if it was already marked)
        self.board_attacked[position.row][position.col] = 1

        # Sleep for a few seconds to add some realism to the game
        time.sleep(3)
