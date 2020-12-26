class Board():
    def __init__(self):
        # grid init
        NUM_OF_ROWS = 6
        NUM_OF_COLS = 7
        self.grid = [[0] * NUM_OF_COLS for _ in range(NUM_OF_ROWS)]

    def add_disc(self, player, col):
        if not self.is_col_full(col):
            i = 5
            while (i >= 0) and (self.grid[i][col] != 0):
                i -= 1

            self.grid[i][col] = player
            return True
        else:
            return False

    def is_col_full(self, col):
        return self.grid[0][col] != 0

    def has_won(self, player, col, row):
        # check for last added disc
        return False

    def _check_horizontal(self):
        pass

    def _check_vertical(self, player, col, row):
        if col > 2:
            return self.grid[row][col - 1] == player and self.grid[row][col - 2] == player and self.grid[row][col - 3] == player

        return False

    def _check_diagonal_right(self):
        pass

    def _check_diagonal_left(self):
        pass
