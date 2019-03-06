
# Thrown if the constructor arguments are invalid
class InvalidPosition(Exception):
    pass

class Position:

    def __init__(self, col, row):

        # Validate the column argument
        if type(col) is int:
            if col < 0 or col > 9:
                print('\nColumn must be either INT (0-9) or STR (A-J).')
                raise InvalidPosition()

        # If the column is provided by the user
        elif type(col) is str:
            if col not in 'ABCDEFGHIJ':
                print('\nThe first character must be a letter A-J.')
                raise InvalidPosition()

            # Translate the column into an INT
            if col == 'A':
                col = 0
            elif col == 'B':
                col = 1
            elif col == 'C':
                col = 2
            elif col == 'D':
                col = 3
            elif col == 'E':
                col = 4
            elif col == 'F':
                col = 5
            elif col == 'G':
                col = 6
            elif col == 'H':
                col = 7
            elif col == 'I':
                col = 8
            else:
                col = 9

        # Validate the row argument
        if type(row) is int:
            if row < 0 or row > 9:
                print('\nRow must be INT (0-9).')
                raise InvalidPosition()

        # If the row is provided by the user
        elif type(row) is str:
            if row not in '0123456789':
                print('\nThe second character must be a number 0-9.')
                raise InvalidPosition()

            # Case the row into an INT
            row = int(row)

        # Once the col/row are validated, set them
        self.col = col
        self.row = row

    def __repr__(self):

        if self.col == 0:
            return 'A' + str(self.row)
        elif self.col == 1:
            return 'B' + str(self.row)
        elif self.col == 2:
            return 'C' + str(self.row)
        elif self.col == 3:
            return 'D' + str(self.row)
        elif self.col == 4:
            return 'E' + str(self.row)
        elif self.col == 5:
            return 'F' + str(self.row)
        elif self.col == 6:
            return 'G' + str(self.row)
        elif self.col == 7:
            return 'H' + str(self.row)
        elif self.col == 8:
            return 'I' + str(self.row)
        else:
            return 'J' + str(self.row)
