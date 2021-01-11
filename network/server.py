from enum import Enum
import socketio
import uvicorn


class OpCode(Enum):
    PLAY = 0
    WIN = 1
    LOSS = 2


def find_op_code():
    pass


def initiate_game():
    pass


sio = socketio.AsyncServer(async_mode='asgi')
app = socketio.ASGIApp(sio)

if __name__ == '__main__':
    # create a Socket.IO server

    uvicorn.run("server:app", host="127.0.0.1", port=5000, log_level="trace")
