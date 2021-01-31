import pygame
import socketio
import asyncio
import aiohttp
from logic.client_logic import ClientLogic
import logging
from logic.config import ClientOpCodes

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)
loop = asyncio.get_event_loop()
sio = socketio.AsyncClient(logger=True, engineio_logger=True)
c = ClientLogic()


@sio.event
async def connect():
    print('connection established')




@sio.event
def my_message(data):
    print('message received with ', data)

    pygame.event.wait()
    event = pygame.event.get()[0]
    if event.type == pygame.QUIT:
        raise SystemExit
    else:
        sio.emit('my response', {'response': event})


@sio.event
async def disconnect():
    print('disconnected from server')


async def start_client():

    # waiting for connection
    await sio.connect('http://localhost:5000')

    # waiting for my turn
    move = await c.read_move()
    logging.info("move assigned")

    request = {}

    # waiting for legal input
    if move.type == pygame.QUIT:
        request['op'] = ClientOpCodes.QUIT.value
    elif move.type == pygame.KEYDOWN:
        request['op'] = ClientOpCodes.KEYDOWN.value
        request['key'] = move.key

    await sio.sleep(1.0)
    await sio.emit('move', request)
    await sio.sleep(1.0)
    logging.info(str(move))

    await sio.sleep(5.0)

if __name__ == '__main__':
    loop.run_until_complete(start_client())



