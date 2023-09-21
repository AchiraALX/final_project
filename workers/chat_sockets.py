#!/usr/bin/env python3

"""All sockets used live here
"""

from quart import websocket, Blueprint, render_template
import asyncio

from workers.workers import ChatBroker

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


@socket.get('/hey')
async def chat_achira():
    return await render_template('chat_achira.html')
