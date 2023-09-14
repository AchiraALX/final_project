#!/usr/bin/env python3

"""Give authorization, add cookies
"""

from db.storage import Storage


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

    def initiated(self) -> dict:
        """Return a dictionary of the added arguments
        """

        return self.all

    def create_user(self, **kwargs) -> None | str | object:
        """Create user to database
        """

        details = {
            'username': kwargs.get('username')
        }

        user = self.storage.get_object(filter_id=details, model='user')
        try:
            return self.storage.add_to_database(data=kwargs, model='user')

        except Exception:
            return user

    def __repr__(self) -> str:
        return "Authenticate yourself"
