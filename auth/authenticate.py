#!/usr/bin/env python3

"""Give authorization, add cookies
"""

from db.storage import Storage
from workers.workers import get_user_by, update_user
from db.models.user import User
from auth.sessions import Session

from typing import Generator
from bcrypt import hashpw, gensalt, checkpw
from uuid import uuid4


def _generate_hash_password(string_password: str) -> str:
    """Generate hash representation of the password
    """

    encoded = hashpw(string_password.encode('utf-8'), gensalt())

    return encoded.decode('utf-8')


def _match_keys(stored: str, provided: str) -> bool:
    """Check if keys are matching

    Return:
        bool
    """

    if checkpw(
        password=provided.encode('utf-8'),
        hashed_password=stored.encode('utf-8')
    ):
        return True

    return False


class Auth:
    """Authenticate
    """

    def __init__(self, **kwargs: object) -> None:
        self.all = kwargs
        self.username = kwargs.get('username')
        self.session_id = kwargs.get('session_id')
        self.password = kwargs.get('password')
        self.email = kwargs.get('email')
        self.storage = Storage('test')
        self.session = Session()

    def initiated(self) -> Generator:
        """Return a dictionary of the added arguments
        """

        yield self.all

    def create_user(self, **kwargs) -> None | str | Generator:
        """Create user to database
        """

        user = get_user_by(string=kwargs['username'])

        try:
            if user.__next__()['username'] == kwargs['username']:
                yield f"<{kwargs['username']}>: already exists ): ):"

        except TypeError:
            kwargs['password'] = _generate_hash_password(kwargs['password'])
            if self.storage.add_to_database(data=kwargs, model='user'):
                yield f"User {kwargs['username']} created successfully"

            else:
                yield "A fatal error occurred"

    def create_blog(self, **kwargs) -> Generator:
        """Create blog to database
        """

        if self.storage.add_to_database(data=kwargs, model='blog'):
            yield f"Blog {kwargs['title']} created successfully"

        else:
            yield f"Fatal error. Blog not created. ): "

    def login(self, username: str, password: str) -> str | bool | None:
        """Logs a user into a new session
        """

        user = self.storage.new_session.query(
            User).filter_by(username=username).first()
        if user is not None:
            if _match_keys(user.password, password):
                return self.session.create_user_session(username=username)

        return None

    def logout(self, token: str) -> bool:
        """Log user out of the session

        Return:
            bool
        """

        if self.session.destroy_user_session(token=token):
            return True

        return False

    def reset_password(self, username: str) -> bool:
        """Initiates the password reset by adding reset_token to user
        """

        token = str(uuid4())
        user = self.storage.new_session.query(
            User).filter_by(username=username).first()
        if user is not None:
            if update_user({'password_reset_token': token}, id=user.id):
                return True

        return False

    def updated_password(self, token: str, new_pass: str) -> bool:
        """Updates the password and clears the reset token
        """

        user = self.storage.new_session.query(
            User).filter_by(password_reset_token=token).first()

        if user is not None:
            if update_user({'password_reset_token': None, 'password': new_pass}, id=user.id):
                return True

        return False

    def __repr__(self) -> str:
        return "Authenticate yourself"
