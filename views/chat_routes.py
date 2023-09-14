#!/usr/bin/env python3

"""Main routes forth chat
"""

from quart import Blueprint, render_template, request

from workers.workers import all_users, get_user_by
from custom.exceptions.exceptions import StringEmptyError
from custom.queries.graph_queries import min_user

from db.storage import Storage
from db.models.user import User

from typing import Generator

chat_route = Blueprint("chat_route", __name__)


@chat_route.route('/', strict_slashes=False)
async def chat_route_main():
    """Main route for the chats
    """

    return await render_template("chat.html")


@chat_route.route('/user', strict_slashes=False, methods=['POST'])
async def my_users() -> dict[str, str] | str | Generator:
    """Get my users
    """

    email = (await request.form).get('email')

    user = get_user_by(email=str(email))

    return user.__next__()


@chat_route.route('/users', strict_slashes=False, methods=['GET'])
async def all_my_users():
    """Browse all users from the database
    """

    users = all_users()

    return [{
        'id': user.id,
        'username': user.username,
        'email': user.email
    } for user in users]
