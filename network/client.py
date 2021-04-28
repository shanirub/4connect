import asyncio
import logging
import threading
import pygame
import socketio
from pygame.locals import *
from game_logic.config import PYGAME_THREAD_NAME, SOCKETIO_THREAD_NAME, ClientOpCodes
from game_logic.client_pygame import ClientLogic
import zmq
from network.threadsocketio import SocketioHandlers


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
                    logging.info("pygame_thread:    POLL_SOCKET event recorded from T1")
                    logging.info(event)
                    data = t1.recv(zmq.NOBLOCK)
                    t1.send('')
                    print(data)
                except zmq.ZMQError:
                    continue
            elif event.type == pygame.QUIT:
                logging.info("pygame_thread:    QUIT event recorded")
                request = {'op': ClientOpCodes.QUIT}
                logging.info("pygame_thread:    sending request to t1")
                logging.info(request)
                t1.send_json(request)
            elif event.type == pygame.KEYDOWN:
                logging.info("pygame_thread:    KEYDOWN event recorded")
                logging.info(event)
                request = {'op': ClientOpCodes.MOVE, 'key': event.key}
                logging.info("pygame_thread:    sending request to t1")
                logging.info(request)
                t1.send_json(request)
            else:
                logging.error("pygame_thread:   unexpected event!")
                logging.error(event)


def socketio_thread(context=None):  # t3
    # connection with main thread (t1)
    context = context or zmq.Context.instance()
    t1 = context.socket(zmq.PAIR)
    return_code = t1.bind("inproc://" + SOCKETIO_THREAD_NAME)
    print(return_code)
    logging.info("socketio_thread:    bind succeeded")

    # connection with server (socketio)
    loop = asyncio.new_event_loop()
    sio = socketio.AsyncClient(logger=True, engineio_logger=True)
    # TODO do i need this '/chat' thing
    # sio.register_namespace(SocketioHandlers('/chat'))
    my_handler = SocketioHandlers(t1)
    sio.register_namespace(my_handler)

    async def start_client():
        try:
            data = t1.recv(zmq.NOBLOCK)
            t1.send(b'')
            print(data)
        except zmq.ZMQError:
            print("")

        # waiting for connection
        await sio.connect('http://localhost:5000')
        await sio.wait()

    loop.run_until_complete(start_client())

    #    t1.send(b"yes from socketio")


if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)
    logging.info("Starting main thread. (T1)")

    context = zmq.Context.instance()


    threads = list()
    # logging.info("Main    : create and start pygame_thread")
    # t2 = threading.Thread(target=pygame_thread, daemon=True)
    # threads.append(t2)

    logging.info("Main    : create and start socketio_thread")
    # thread_socketio_object = ThreadSocketIO()

    t3 = threading.Thread(target=socketio_thread, daemon=True)
    #     t3 = threading.Thread(target=ThreadSocketIO, daemon=True)
    threads.append(t3)

    for thread in threads:
        thread.start()

    logging.info("Main    : starting and binding sockets")
    # t2_socket = context.socket(zmq.PAIR)
    # t2_socket.connect("inproc://" + PYGAME_THREAD_NAME)

    t3_socket = context.socket(zmq.PAIR)
    t3_socket.connect("inproc://" + SOCKETIO_THREAD_NAME)
    logging.info("Main    : binding succeeded")

    # TODO TODO TODO!!!!!
    # TODO check threads connection t1(main) <--> t3(socket_io) as class!!!
    p = t3_socket.send(b'')
    print(p)
    reply = t3_socket.recv()
    print(reply)
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
