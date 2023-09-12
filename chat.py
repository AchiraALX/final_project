#!/usr/bin/env python3

"""Chat entry
"""

import asyncio
from app.main import chat
from hypercorn.config import Config
from hypercorn.asyncio import serve

config = Config()
config.use_reloader = True
config.workers = 1
config.quic_bind = ['0:8000']

if __name__ == "__main__":
    asyncio.run(
        serve(chat, config)
    )
