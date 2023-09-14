#!/usr/bin/env python3

"""Give authorization, add cookies
"""

from db.storage import Storage
from workers.workers import get_user_by

from typing import Generator


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

    def __repr__(self) -> str:
        return "Authenticate yourself"
