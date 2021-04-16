import logging
import threading
import pygame
from pygame.locals import *
from game_logic.config import PYGAME_THREAD_NAME, SOCKETIO_THREAD_NAME
from game_logic.client_pygame import ClientLogic
import zmq


def pygame_thread(context=None):    # t2
    context = context or zmq.Context.instance()
    t1 = context.socket(zmq.PAIR)
    t1.bind("inproc://" + PYGAME_THREAD_NAME)
    logging.info("pygame_thread:    bind succeeded")

    c = ClientLogic()

    pygame.init()
    POLL_SOCKET = USEREVENT + 1
    pygame.time.set_timer(POLL_SOCKET, 100)
    is_gameover = False
    while not is_gameover:
        for event in pygame.event.get():
            if event.type == POLL_SOCKET:   # message from main thread T1
                try:
                    # TODO check messages from main thread:
                    # TODO 1. draw board (c object) __OR__
                    # TODO 2. error message
                    data = t1.recv(zmq.NOBLOCK)
                    t1.send('')
                    print(data)
                except zmq.ZMQError:
                    continue
            elif event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                # only relevant events
                print(event)
                # t1.send(b"")
                t1.send_json({"event_type": event.type})
                # TODO send to main thread (then server) analyse move and react accordingly
            else:
                pass


def socketio_thread(context=None):  # t3
    context = context or zmq.Context.instance()
    t1 = context.socket(zmq.PAIR)
    t1.bind("inproc://" + SOCKETIO_THREAD_NAME)
    logging.info("socketio_thread:    bind succeeded")

    while True:
        x = t1.recv_json()
        print(x)
        t1.send(b"yes from socketio")


if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)
    logging.info("Starting main thread. (T1)")

    context = zmq.Context.instance()

    threads = list()
    logging.info("Main    : create and start pygame_thread")
    t2 = threading.Thread(target=pygame_thread, daemon=True)
    threads.append(t2)

    logging.info("Main    : create and start socketio_thread")
    t3 = threading.Thread(target=socketio_thread, daemon=True)
    threads.append(t3)

    for thread in threads:
        thread.start()

    logging.info("Main    : starting and binding sockets")
    t2_socket = context.socket(zmq.PAIR)
    t2_socket.connect("inproc://" + PYGAME_THREAD_NAME)

    t3_socket = context.socket(zmq.PAIR)
    t3_socket.connect("inproc://" + SOCKETIO_THREAD_NAME)
    logging.info("Main    : binding succeeded")

    should_exit = False

    while not should_exit:
        # TODO: 1. recv t3 socketio
        socketio_message = t3_socket.recv()

        # TODO: 2. send t2 pygame
        t2_socket.send(socketio_message)

        # TODO: 3. recv t2 pygame
        pygame_answer = t2_socket.recv()

        # TODO: 4. send t3 socketio
        t3_socket.send(pygame_answer)

    for thread in threads:
        thread.join()
