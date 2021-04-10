'''
Game class for testing

2 local players on one computer, text mode

'''
from game_logic.Board import Board

class Game():
    def __init__(self):
        pass

    def play(self):
        b = Board()
        player = None  # first player
        has_won_condition = False
        valid_input_condition = False

        while not has_won_condition:

            if player is None or player == 2:
                player = 1
            else:
                player = 2

            print("Current grid:")
            print(b.__repr__())

            while not valid_input_condition:
                play = input(" Player " + str(player) + ": Please enter column number (0 - 6).")
                if play.isdigit():
                    play = int(play)
                    if 0 <= play <= 6:
                        if b.add_disc(player, play):
                            has_won_condition = b.has_won(player, b.current_col, b.current_row)
                            valid_input_condition = True
                        else:
                            print("Full column, try another column.")
                    else:
                        print("Column not in range.")
                else:
                    print("Column must be a number.")

            valid_input_condition = False

        self._announce_win(player)

    def _announce_win(self, player):
        print("The winner is player " + str(player) + "!")

    def _ask_for_play(self, player):
        pass


if __name__ == '__main__':
    g = Game()
    g.play()

