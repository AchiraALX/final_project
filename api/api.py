#!/usr/bin/env python3

"""Main API
"""

from quart import Blueprint, render_template, request
from workers.workers import (
    get_user_by,
    users_with_matching_query,
    remove_user_self,
    remove_blog_self
)

from typing import Generator


api = Blueprint("api", __name__)


@api.route('/', strict_slashes=False, methods=['GET'])
async def api_main():
    """API Home
    """

    return await render_template('api.html')


@api.route('/user/<username>', strict_slashes=False, methods=['GET'])
@api.route('/user', strict_slashes=False, methods=['GET'])
async def get_user() -> dict[str, str] | str | Generator:
    """Get my users
    """

    string = (await request.form).get('query')

    user = get_user_by(string=str(string))

    return user.__next__()


@api.route('/users/<query>', strict_slashes=False, methods=['GET'], defaults={'query': None})
async def user_matching_query(query) -> list:
    """Gets user that match the query

    Route:
        /users/<query> where query = username or email
    """

    if query is None:
        query = (await request.form).get('query')

    users = users_with_matching_query(query=str(query)).__next__()

    return users


# Update Blog
@api.route('blog-update/<key>', strict_slashes=False, methods=['PUT'])
async def blog_update(key: str) -> str:
    """Update the blog that matches key

    Return:
        str
    """

    if not key:
        return f"Key should be specified"

    return f"Blog updated with key: {key}"


@api.route('/user-update/<key>', strict_slashes=False, methods=['PUT'])
async def user_update(key: str) -> str:
    """Update the user that matches key

    Return:
        str
    """

    if not key:
        return f"Parameter 'key: str' should be specified."

    return f"User with key: {key} was updated as successfully"


@api.route('/destroy_profile', strict_slashes=False, methods=['DELETE'])
@api.route(
    'destroy_profile/<username>/<password>',
    defaults={'password': None},
    strict_slashes=False,
    methods=['DELETE']
)
async def destroy_profile(username: str, password) -> str:
    """Delete the user's profile
    """

    if password is not None:
        user = get_user_by(string=username).__next__()
        if user['password'] == password:
            return remove_user_self(id=user['id']).__next__()
        return "Password is incorrect"
    return "Password is required"
