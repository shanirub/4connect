'''
i thought keeping track of all the constants in one config file would look more professional
'''
from enum import Enum


class ClientOpCodes(Enum):
    QUIT = 1
    KEYDOWN = 2
    MOVE = 3


class ServerOpCodes(Enum):
    ILLEGAL_INPUT = 1
    USER_WON = 2
    USER_LOST = 3
    UPDATE_GRID = 4
    GAME_ENDED = 5  # game ended before anyone won
    COL_FULL = 6
    WAITING_FOR_MOVE = 7
    LEGAL_MOVE = 8
    WAITING_FOR_SECONDE_PLAYER = 9

