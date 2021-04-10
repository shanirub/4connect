'''
Server module - should run only once on the server

handles networking
game_logic in server_logic.py
'''


from enum import Enum
import socketio
import uvicorn
import logging
from game_logic.server_logic import ServerLogic
from game_logic.config import ClientOpCodes, ServerOpCodes

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
    # starting a game when there are two players
    if len(clients) == 2:
        await sio.emit(ServerOpCodes.WAITING_FOR_MOVE, to=clients[0])
    elif len(clients) == 1:
        await sio.emit(ServerOpCodes.WAITING_FOR_SECONDE_PLAYER, to=clients[0])

@sio.on(ClientOpCodes.MOVE)
async def move(sid, data):
    logging.info("new MOVE event recieved: sid: " + str(sid) + "data: ")
    logging.info(data)

    player_id = clients.index(sid) + 1
    logging.info("player id: " + str(player_id))

    reply = await sl.generate_reply(player_id, data)
    logging.info("reply from game_logic module")
    logging.info(str(reply))

    await sio.emit(reply, to=sid)
    await sio.sleep(5.0)

    # updating grid for the two players
    await update_grid()

    # alerting the other player that's his turn
    if reply['op'] == ServerOpCodes.LEGAL_MOVE:
        if clients.index(sid) == 0:
            await sio.emit(ServerOpCodes.WAITING_FOR_MOVE, to=clients[1])
        else:
            await sio.emit(ServerOpCodes.WAITING_FOR_MOVE, to=clients[0])


@sio.event
def disconnect(sid):
    print('disconnect ', sid)

async def update_grid():
    reply = {'op': ServerOpCodes.UPDATE_GRID, 'grid':sl.b.grid}
    await sio.emit(reply, to=clients[0])
    await sio.emit(reply, to=clients[1])

if __name__ == '__main__':
    # create a Socket.IO server
    logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)
    uvicorn.run("server:app", host="127.0.0.1", port=5000, log_level="trace")
