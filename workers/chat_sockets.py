#!/usr/bin/env python3

"""All sockets used live here
"""

from quart import websocket, Blueprint, render_template, request
import asyncio

from workers.workers import ChatBroker
from workers.workers import get_user_by_session

chat_broker = ChatBroker()

socket = Blueprint('socket', __name__)

connected_clients = set()


async def _receive() -> None:
    while True:
        message = await websocket.receive()
        await chat_broker.put_message(message)


@socket.websocket('/')
async def chat():
    connected_clients.add(websocket)
    try:
        while True:
            message = await websocket.receive()
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)

    except Exception as e:
        raise e

    finally:
        connected_clients.remove(websocket)


@socket.websocket('/achira')
async def put_toa_achira() -> None:
    """Put message to achira
    """

    task = asyncio.ensure_future(_receive())
    try:
        async for message in chat_broker.subscribe():
            await websocket.send(message)

    finally:
        task.cancel()
        await task


@socket.get('/chat')
async def chat_home():
    session_cookie = request.cookies.get('session-token')

    if session_cookie is None and not session_cookie:
        return await render_template('login.html')

    else:
        try:
            user = get_user_by_session(session_id=session_cookie).__next__()

        except StopIteration:
            user = None

    return await render_template('chat_achira.html', user=user)
