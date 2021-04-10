'''
client side game_logic:
should only 1. draw the grid 2. read a move from the player
'''

import pygame
import logging
from game_logic.Board import Board

class ClientLogic:
    def __init__(self):
        logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)

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

        pygame.event.set_allowed(None)
        pygame.event.set_allowed([pygame.KEYDOWN])

    def draw_grid(self, grid):
        for i in range(7):
            text = self.myfont.render(str(i), True, pygame.Color("White"), pygame.Color("Black"))
            self.screen.blit(text, (100 * i, 0))
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

    async def read_move(self):
        global move
        pygame.display.update()
        is_quit_or_keydown_event = False

        while not is_quit_or_keydown_event:
            move = pygame.event.wait()
            logging.info("read event: ")
            logging.info(move)
            if move.type == pygame.KEYDOWN or move.type == pygame.QUIT:
                is_quit_or_keydown_event = True

        return move

## testing

# c = ClientLogic()
# c.read_move

