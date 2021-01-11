import socketio
import asyncio
import aiohttp

loop = asyncio.get_event_loop()
sio = socketio.AsyncClient(logger=True, engineio_logger=True)


@sio.event
async def connect():
    print('connection established')


@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})


@sio.event
async def disconnect():
    print('disconnected from server')


async def start_server():
    await sio.connect('http://localhost:5000')
    await sio.wait()

if __name__ == '__main__':
    loop.run_until_complete(start_server())


