#!/usr/bin/env python3

"""Script to handle the sessions
"""

from workers.workers import update_user
from db.models.user import User

from uuid import uuid4


# Generate session token
def _generate_session_token() -> str:
    """Return a new session token
    """

    return str(uuid4())


class Session:
    """Class to handle session
    """

    @staticmethod
    def create_user_session(obj: User):
        """Create a new login session for the user
        """

        token = _generate_session_token()
        data = {
            'session_token': token
        }

        update_user(data=data, id=obj.id)

    @staticmethod
    def destroy_user_session(obj: User):
        """Destroys user in session with obj
        """

        data = {
            'session_token': None
        }
        update_user(data=data, id=obj.id)
