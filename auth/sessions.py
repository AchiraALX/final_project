#!/usr/bin/env python3

"""Script to handle the sessions
"""


from db.storage import Storage
from db.models.user import User
from workers.workers import update_user

from uuid import uuid4
import secrets


# Generate session token
def _generate_session_token() -> str:
    """Return a new session token
    """

    return secrets.token_hex(32)


class Session:
    """Class to handle session
    """

    def __init__(self) -> None:
        self.session = Storage('test').new_session

    def create_user_session(self, username: str) -> bool:
        """Create a new login session for the user
        """

        token = _generate_session_token()
        user = self.session.query(User).filter_by(username=username).first()
        if user is not None:
            data = {
                'session_token': token
            }

            update_user(data=data, id=user.id)
            self.session.close()
            return True

        return False

    def destroy_user_session(self, token: str) -> bool:
        """Destroys user in session with obj
        """

        user = self.session.query(User).filter_by(session_token=token).first()
        if user is not None:
            data = {
                'session_token': None
            }

            update_user(data=data, id=user.id)
            self.session.close()
            return True

        return False
