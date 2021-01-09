import socketio

sio = socketio.AsyncClient()


@sio.event
def connect():
    print('connection established')


@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})


@sio.event
def disconnect():
    print('disconnected from server')


async def con():
    await sio.connect('http://localhost:5000')

if __name__ == '__main__':
    con()
