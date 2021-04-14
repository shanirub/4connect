'''
client_socketio.py

handling the thread responsible for the socketio
'''

import pygame
import socketio
import asyncio
import aiohttp
# from game_logic.client_pygame import ClientLogic
import logging
from game_logic.config import ClientOpCodes, ServerOpCodes
import zmq
from game_logic.config import SOCKETIO_THREAD_NAME

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)


# Prepare context and sockets
# connection with thread 1 (main thread)
context = zmq.Context()
t1 = context.socket(zmq.PAIR)
t1.connect("inproc://" + SOCKETIO_THREAD_NAME)

# connection with server (socketio)
loop = asyncio.get_event_loop()
sio = socketio.AsyncClient(logger=True, engineio_logger=True)
# c = ClientLogic()


async def reading_new_move():
    move = await c.read_move()
    logging.info("move assigned: " + str(move))

    request = {}

    if move.type == pygame.QUIT:
        request['op'] = ClientOpCodes.QUIT.value
    elif move.type == pygame.KEYDOWN:
        request['op'] = ClientOpCodes.KEYDOWN.value
        request['key'] = move.key

    return request

@sio.event
async def connect():
    print('connection established')


@sio.on(ServerOpCodes.WAITING_FOR_MOVE)
async def reading_and_sending_move(sid, data):
    request = reading_new_move()
    await sio.emit('move', request)
    await sio.sleep(1.0)


@sio.on(ServerOpCodes.LEGAL_MOVE)
async def move_was_accepted(sid, data):
    logging.info('move was accepted')

@sio.on(ServerOpCodes.UPDATE_GRID)
async def update_grid(sid, data):
    c.b.grid = data['grid']
    c.b.draw_grid(data['grid'])


@sio.on(ServerOpCodes.USER_WON)
async def inform_win():
    print("you have won")
    await sio.disconnect()
    raise SystemExit

@sio.on(ServerOpCodes.COL_FULL)
async def inform_col_full():
    print("requested column is full. try another column")
    request = reading_new_move()
    await sio.emit('move', request)
    await sio.sleep(1.0)


@sio.on(ServerOpCodes.ILLEGAL_INPUT)
async def inform_illegal_input():
    print("illegal input. remember: only 0 - 6 or closing the window. please try again")
    request = reading_new_move()
    await sio.emit('move', request)
    await sio.sleep(1.0)

@sio.on(ServerOpCodes.GAME_ENDED)
async def inform_game_ended():
    print("game ended without a win")
    raise SystemExit


@sio.on(ServerOpCodes.USER_LOST)
async def inform_loss():
    print("you have lost")
    await sio.disconnect()
    raise SystemExit


@sio.event
async def disconnect():
    print('disconnected from server')


async def start_client():
    try:
        data = t1.recv(zmq.NOBLOCK)
        t1.send('')
        print(data)
    except zmq.ZMQError:
        print("")

    # waiting for connection
    await sio.connect('http://localhost:5000')
    await sio.wait()


if __name__ == '__main__':
    loop.run_until_complete(start_client())



