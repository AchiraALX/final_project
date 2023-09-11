#!/usr/bin/env python3

"""Main entry to the app
"""

from quart import Quart

chat = Quart(__name__)


@chat.route('/', strict_slashes=False)
async def chat_me():
    """Main route/ home route
    """

    return "My chat is alive."
