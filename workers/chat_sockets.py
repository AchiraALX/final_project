#!/usr/bin/env python3

"""All sockets used live here
"""

from quart import websocket, Blueprint

socket = Blueprint('socket', __name__)
