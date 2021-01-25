from enum import Enum
import socketio
import uvicorn

sio = socketio.AsyncServer(async_mode='asgi')
app = socketio.ASGIApp(sio)

clients = []

@sio.event
async def connect(sid, environ):
    print("connect ", sid)
    clients.append(sid)
    print("clients: ")
    print(clients)
    await sio.emit("welcome", room=clients[0])

@sio.event
async def chat_message(sid, data):
    print("message ", data)
    await sio.emit('reply', room=sid)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    # create a Socket.IO server

    uvicorn.run("server:app", host="127.0.0.1", port=5000, log_level="trace")
