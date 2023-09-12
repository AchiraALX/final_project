#!/usr/bin/env python3

"""Main routes forth chat
"""

from quart import Blueprint, render_template

chat_route = Blueprint("chat_route", __name__)


@chat_route.route('/', strict_slashes=False)
async def chat_route_main():
    """Main route for the chats
    """

    return await render_template("chat.html")
