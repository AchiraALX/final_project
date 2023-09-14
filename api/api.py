#!/usr/bin/env python3

"""Main API
"""

from quart import Blueprint, render_template, request
from workers.workers import all_users
from custom.queries.graph_queries import min_user


api = Blueprint("api", __name__)


@api.route('/', strict_slashes=False, methods=['GET'])
async def api_main():
    """API Home
    """

    return await render_template('api.html')


@api.route('/get_users', strict_slashes=False, methods=['GET'])
async def get_users_():
    """Retrieve users from the database
    """

    return all_users(min_user).__next__()
