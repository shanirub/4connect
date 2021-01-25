from enum import Enum

class ClientOpCodes(Enum):
    NEW_EVENT = 1

class ServerOpCodes(Enum):
    ILLEGAL_INPUT = 1
    USER_WON = 2
    USER_LOST = 3
    UPDATE_GRID = 4