
class Battleship:

    # Create a new Battleship object
    def __init__(self, size):
        self.size = size
        self.cells = []

    # Add a cell to this ship's list of cells
    def add_cell(self, row, col):
        self.cells.append([row, col])

    # Remove a cell from this ship's list of cells
    def rem_cell(self, row, col):

        target_cell = [row, col]

        # Remove the target cell if it exists
        for cell in self.cells:
            if cell == target_cell:
                self.cells = [c for c in self.cells if c != target_cell]

                # Return True if the target cell was found and removed
                return True

        # Return False if the target cell was not found
        return False

    # Check if a ship is destroyed
    def is_destroyed(self):

        # Return True if the ship has no remaining cells, otherwise return False
        return not bool(self.cells)
