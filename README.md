# 4connect
4 connect game

### Architecture

![image](https://github.com/shanirub/4connect/blob/client_zmq_threads/arch_4connect.png)

Server runs on one thread.

Client uses three threads: *pygame* thread for gui and interaction with the player, *socketio* thread responsible for communicating with server and *main* thread that talks to both *pygame* and *socketio* threads.

There is no direct connection between *pygame* and *socketio* threads.

A message from the server to the player take 3 steps (1,2,3 in diagram) and 3 more steps for the response (4,5,6 in diagram).

Inter-thread connections are handled with `pyzmq` library using **PAIR** sockets.

The connection between the server and the client is handled with `python-socketio` library.

All connection are async.

### Contents
`game_logic` Module includes the following scripts:
- `Board.py` Entire game logic.
- `Game.py` Game implementation - runs locally and in text mode.
- `server_logic.py` and `client_pygame.py` includes the addional logic for the network game (including gui) implementation.
- `config.py` includes all constants in use.

`gui\Game_with_gui.py` Game implementation - runs locally with gui.

`network` includes two scripts:
- `server.py` Server script, to be run once.
- `client.py` Client script, to be run twice (once for each player).




![Python application](https://github.com/shanirub/4connect/workflows/Python%20application/badge.svg)
