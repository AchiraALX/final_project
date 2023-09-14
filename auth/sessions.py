#!/usr/bin/env python3

"""Script to handle the sessions
"""

from db.storage import Storage
from uuid import uuid4


# Generate session token
def _generate_session_token() -> str:
    """Return a new session token
    """

    return str(uuid4())


storage = Storage('test')


class Session:
    """Class to handle session
    """
