import pygame
import socketio
import asyncio
import aiohttp
from logic.client_logic import ClientLogic

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
        # Close the program any way you want, or troll users who want to close your program.
        raise SystemExit
    else:
        sio.emit('my response', {'response': event})


@sio.event
async def disconnect():
    print('disconnected from server')


async def start_server():
    await sio.connect('http://localhost:5000')
    # 1. wait for opcode from server
    # 2. print something
    # 3. wait for input - only one move
    # 4. send move to server
    # 5. goto 1
    await sio.wait()


async def my_background_task(my_argument):
    # do some background work here!
    c.read_move()


if __name__ == '__main__':
    loop.run_until_complete(start_server())
    sio.start_background_task(my_background_task)



