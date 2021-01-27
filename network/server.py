from enum import Enum
import socketio
import uvicorn
import logging
from logic.server_logic import ServerLogic
from logic.config import ClientOpCodes

sio = socketio.AsyncServer(async_mode='asgi')
app = socketio.ASGIApp(sio)
sl = ServerLogic()

clients = []

@sio.event
async def connect(sid, environ):
    print("connect ", sid)
    clients.append(sid)
    print("clients: ")
    print(clients)
    await sio.emit("welcome", room=clients[0])

@sio.event
async def request(sid, data):
    # function's name = first argument in emit by client.py
    # sid = client id
    # data = event's data
    logging.info("new event recieved: sid")
    logging.info(sid)
    logging.info("data")
    logging.info(data)
    player_id = clients.index(sid) + 1
    logging.info("player id: " + str(player_id))
    reply = await sl.generate_reply(player_id, data)
    logging.info("reply from logic module")
    logging.info(reply)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    # create a Socket.IO server
    logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)
    uvicorn.run("server:app", host="127.0.0.1", port=5000, log_level="trace")
