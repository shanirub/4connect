class Board():
    def __init__(self):
        # grid init
        self.NUM_OF_ROWS = 6
        self.NUM_OF_COLS = 7
        self.grid = [[0] * self.NUM_OF_COLS for _ in range(self.NUM_OF_ROWS)]

    def add_disc(self, player, col):
        """
        Adds a new disc to the grid.
        Parameters
        ----------
        player : int
            the player adding the disc
        col : int
            the column, to which the disc is added

        Returns
        -------
        True
            when adding was successful. False otherwise.
        """
        if not self.is_col_full(col):
            i = 5
            while (i >= 0) and (self.grid[i][col] != 0):
                i -= 1

            self.grid[i][col] = player
            return True
        else:
            return False

    def is_col_full(self, col):
        """
        Checking to see if a column in the grid is full
        Parameters
        ----------
        col : int
            the column to check

        Returns
        -------
        True
            when the column is full
        """
        return self.grid[0][col] != 0

    def has_won(self, player, current_col, current_row):
        # check for last added disc
        return self._check_vertical(self, player, current_col, current_row)

    def _check_horizontal(self, player, current_col, current_row):
        tmp = self.grid[current_row]
        return tmp[:current_col] == [player] * 3 or tmp[current_col:] == [player] * 4

    def _check_vertical(self, player, current_col, current_row):
        if current_row >= 2:  # no point in checking, when there are less than 4 discs in the column
            tmp = [row[current_col] for row in self.grid]
            return tmp[current_row:current_row + 4] == [player] * 4

        return False

    def _check_diagonal_right(self, player, current_col, current_row):  # diagonal right down, left up
        sublist_right_down = [self.grid[current_row + i][current_col + i]
                              for i in range(min(self.NUM_OF_COLS - current_col, self.NUM_OF_ROWS - current_row))]
        sublist_left_up = [self.grid[current_row - i][current_col - i]
                           for i in range(min(current_col + 1, current_row + 1))]

        # sublist_left_up reverse, take out last element (to avoid duplicates)
        sublist_left_up.reverse()
        sublist_left_up.pop()
        # join both sublists and save them as a string
        tmpstr = ''.join(str(x) for x in [sublist_left_up + sublist_right_down])
        # search for the winning sequence in the string
        if tmpstr.find(str(player) * 4) == -1:
            return False
        else:
            return True

    def _check_diagonal_left(self):
        pass
