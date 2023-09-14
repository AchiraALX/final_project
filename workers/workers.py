#!/usr/bin/env python3

"""The workers
"""

from db.storage import Storage
from typing import Generator
import json
from db.models.user import User
from db.models.blog import Blog


def _sum(a: int | float, b: int | float) -> int | float:
    """Add a to b

    Return:
        sum float or integer
    """

    return a + b


def get_user_by(email: str) -> Generator:
    """Get one user
    """

    for user in all_users():
        if user.email == email:
            yield {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }

    yield f"No user with the email specified: {email}"


def all_users() -> Generator:
    """Get all users
    """

    users = Storage('test').new_session.query(User).all()

    for user in users:
        yield user


if __name__ == "__main__":
    storage = Storage('test')
