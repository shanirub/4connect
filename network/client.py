import logging
import threading
from time import sleep

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
            if event.type == POLL_SOCKET:
                try:
                    # TODO check messages from main thread
                    data = t1.recv(zmq.NOBLOCK)
                    t1.send('')
                    print(data)
                except zmq.ZMQError:
                    continue
            elif event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                print(event)
                # TODO send to c object to analyse move and react accordingly
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

    # for i in range(10):
    #     logging.info("sending n to t3")
    #     sleep(2)
    #     t3_socket.send_json({"n":i})
    #     x = t3_socket.recv()
    #     print(x)
    #
    #     logging.info("sending n to t2")
    #     t2_socket.send_json({"n":i})
    #     x = t2_socket.recv()
    #     print(x)
    while True:
        pass

    for thread in threads:
        thread.join()
