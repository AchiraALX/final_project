#!/usr/bin/env python3

"""Main server
"""

import asyncio
from app.main import chat
from hypercorn import Config
from hypercorn.asyncio import serve

hypercorn_config = {
    "bind": ["0:8000"],
    "workers": 1,
    "use_reloader": True,
    "accesslog": "-"
}


if __name__ == "__main__":
    asyncio.run(
        serve(chat, Config(**hypercorn_config))
    )
