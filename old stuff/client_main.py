'''
client_main.py

main thread, used to connect the other two threads (for pygame and socketio)
'''
import logging

from game_logic.config import PYGAME_THREAD_NAME, SOCKETIO_THREAD_NAME
import zmq

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)

context = zmq.Context()
t2 = context.socket(zmq.PAIR)
t2.bind("inproc://" + PYGAME_THREAD_NAME)

t3 = context.socket(zmq.PAIR)
t3.bind("inproc://" + SOCKETIO_THREAD_NAME)

for n in range(100):
    t3.send_string("Counter: " + str(n))
    logging.info("counter: " + n)
    t3.recv()
