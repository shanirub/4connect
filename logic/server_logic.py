'''
server side logic:
should check incoming requests ($move, $player),
and return: 1. error message if request is illegal OR
            2. win / lose message OR
            3. updated grid

ints instead of constants no no no
'''

from logic.Board import Board
from logic.config import ServerOpCodes
import logging
import pygame



class ServerLogic:
    def __init__(self):
        logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)
        self.b = Board()

    async def generate_reply(self, player_id, request_data):
        logging.info("recieved request_data:")
        logging.info(request_data)
        logging.info("from player id:")
        logging.info(player_id)


        reply = {}

        if not request_data['op'] == pygame.QUIT:
            if self._is_valid_keydown(request_data):
                disc_added = self.b.add_disc(player_id, request_data['key'] - 48)
                if disc_added:
                    if self.b.has_won(player_id, self.b.current_col, self.b.current_row):
                        reply['op'] = ServerOpCodes.USER_WON
                    else:
                        reply['op'] = ServerOpCodes.UPDATE_GRID
                        # reply['grid'] = self.b.grid
                else:
                    reply['op'] = ServerOpCodes.COL_FULL
            else:
                reply['op'] = ServerOpCodes.ILLEGAL_INPUT
        else:
            reply['op'] = ServerOpCodes.GAME_ENDED

        return reply

    def _is_valid_keydown(self, request_data):
        return 48 <= request_data['key'] <= 54


