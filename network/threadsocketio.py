import logging

import socketio
from decorators.basic import timing

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)

class SocketioHandlers(socketio.AsyncClientNamespace):
    @timing
    def __init__(self, t1):
        super().__init__()
        print("handler object initiated")
        self.t1 = t1

    @timing
    def on_connect(self):
        print('connection established')

    def on_disconnect(self):
        print('disconnected from server')

    # one method to handle all ServerOpCodes events and pass them to main thread t1
    async def on_message(self, data):
        logging.info("recieved message")
        logging.info(data)
        self.t1.send(data)
        # await sio.emit('move', request)

    # async def on_my_event(self, data):
    #    await self.emit('my_response', data)