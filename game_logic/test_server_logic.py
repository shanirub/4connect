import asyncio

from game_logic.server_logic import ServerLogic
from game_logic.config import ServerOpCodes, ClientOpCodes
import pygame
import pytest


@pytest.mark.asyncio
async def test_generate_reply():
    s = ServerLogic()
    player_id = 1
    request = {'op':pygame.QUIT}
    reply = await s.generate_reply(player_id, request)
    assert reply == ServerOpCodes.GAME_ENDED

    request = {'op':ClientOpCodes.MOVE, 'key':46}
    reply = await s.generate_reply(player_id, request)
    assert reply == ServerOpCodes.ILLEGAL_INPUT

    request = {'op':ClientOpCodes.MOVE, 'key':56}
    reply = await s.generate_reply(player_id, request)
    assert reply == ServerOpCodes.ILLEGAL_INPUT

    request = {'op':ClientOpCodes.MOVE, 'key':50}
    reply = await s.generate_reply(player_id, request)
    assert reply == ServerOpCodes.LEGAL_MOVE

