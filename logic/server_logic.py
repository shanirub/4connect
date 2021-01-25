'''
server side logic:
should check incoming requests ($move, $player),
and return: 1. error message if request is illegal OR
            2. win / lose message OR
            3. updated grid
'''

from logic.Board import Board
import logging

class ServerLogic:
    def __init__(self):
        logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)
        b = Board

    def generate_reply(self, request):
        logging.info("recieved request:")
        logging.info(request)


