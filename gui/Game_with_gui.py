from logic.Board import Board
import pygame


class GameWithGui:
    def __init__(self):
        self.SQUARE_SIZE = 100
        self.RADIUS_SIZE = self.SQUARE_SIZE / 2 - 10
        self.b = Board()

        pygame.init()

        height = self.b.NUM_OF_ROWS * self.SQUARE_SIZE
        width = self.b.NUM_OF_COLS * self.SQUARE_SIZE
        size = (width, height)

        self.screen = pygame.display.set_mode(size)
        self.screen.fill('Lavender')
        self.myfont = pygame.font.SysFont("monospace", 75)

        self.draw_grid(self.b.grid)
        pygame.display.update()

    def play(self):
        player = 1  # first player
        has_won_condition = False
        valid_input_condition = False

        while not has_won_condition:

            for event in pygame.event.get():
                self.draw_grid(self.b.grid)
                pygame.display.update()
                if event.type == pygame.QUIT:
                    # Close the program any way you want, or troll users who want to close your program.
                    raise SystemExit
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        print("Player " + str(player) + ": Column 0")
                        if self.b.add_disc(player, 0):
                            has_won_condition = self.b.has_won(player, self.b.current_col, self.b.current_row)
                            player = [2, 1][player - 1]
                    elif event.key == pygame.K_1:
                        print("Player " + str(player) + ": Column 1")
                        if self.b.add_disc(player, 1):
                            has_won_condition = self.b.has_won(player, self.b.current_col, self.b.current_row)
                            player = [2, 1][player - 1]
                    elif event.key == pygame.K_2:
                        print("Player " + str(player) + ": Column 2")
                        if self.b.add_disc(player, 2):
                            has_won_condition = self.b.has_won(player, self.b.current_col, self.b.current_row)
                            player = [2, 1][player - 1]
                    elif event.key == pygame.K_3:
                        print("Player " + str(player) + ": Column 3")
                        if self.b.add_disc(player, 3):
                            has_won_condition = self.b.has_won(player, self.b.current_col, self.b.current_row)
                            player = [2, 1][player - 1]
                    elif event.key == pygame.K_4:
                        print("Player " + str(player) + ": Column 4")
                        if self.b.add_disc(player, 4):
                            has_won_condition = self.b.has_won(player, self.b.current_col, self.b.current_row)
                            player = [2, 1][player - 1]
                    elif event.key == pygame.K_5:
                        print("Player " + str(player) + ": Column 5")
                        if self.b.add_disc(player, 5):
                            has_won_condition = self.b.has_won(player, self.b.current_col, self.b.current_row)
                            player = [2, 1][player - 1]
                    elif event.key == pygame.K_6:
                        print("Player " + str(player) + ": Column 6")
                        if self.b.add_disc(player, 6):
                            has_won_condition = self.b.has_won(player, self.b.current_col, self.b.current_row)
                            player = [2, 1][player - 1]

        # label = self.myfont.render("Player " + str(player) + " wins!!", 1, pygame.Color("Yellow"))
        # self.screen.blit(label, (40, 10))
        pygame.time.wait(5000)


    def draw_grid(self, grid):
        # print(self.b.__repr__())
        for row in range(self.b.NUM_OF_ROWS):
            for col in range(self.b.NUM_OF_COLS):
                pygame.draw.rect(self.screen, pygame.Color('Black'), (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE,
                                 self.SQUARE_SIZE, self.SQUARE_SIZE), 10)

                if grid[row][col] == 2:
                    pygame.draw.circle(self.screen, pygame.Color('Red'),
                                       (col * self.SQUARE_SIZE + 50, row * self.SQUARE_SIZE + 50), self.RADIUS_SIZE)
                elif grid[row][col] == 1:
                    pygame.draw.circle(self.screen, pygame.Color('Blue'),
                                       (col * self.SQUARE_SIZE + 50, row * self.SQUARE_SIZE + 50), self.RADIUS_SIZE)
                # paint circle - white empty, 1 blue, 2 red

        # pygame.display.update()
        # pygame.time.wait(5000)


if __name__ == '__main__':
    game = GameWithGui()
    game.play()