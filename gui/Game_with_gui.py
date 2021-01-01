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
        myfont = pygame.font.SysFont("monospace", 75)

        self.draw_grid(self.b.grid)
        pygame.display.update()

    def play(self):
        pass

    def draw_grid(self, grid):
        print(self.b.__repr__())
        for row in range(self.b.NUM_OF_ROWS):
            for col in range(self.b.NUM_OF_COLS):
                # paint box
                # pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.rect(self.screen, pygame.Color('Black'), (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE,
                                 self.SQUARE_SIZE, self.SQUARE_SIZE), 10)

                # if grid[row][col] == 0:
                pygame.draw.circle(self.screen, pygame.Color('Red'),
                                       (col * self.SQUARE_SIZE + 50, row * self.SQUARE_SIZE + 50), self.RADIUS_SIZE)
                # paint circle - white empty, 1 blue, 2 red

        pygame.display.update()
        pygame.time.wait(5000)

    def _announce_win(self):
        pass


if __name__ == '__main__':
    game = GameWithGui()
    game.play()