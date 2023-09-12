#!/usr/bin/env python3

"""Main API
"""

from quart import Blueprint, render_template
from workers.workers import get_users


api = Blueprint("api", __name__)


@api.route('/', strict_slashes=False, methods=['GET'])
async def api_main():
    """API Home
    """

    return await render_template('api.html')


@api.route('/get_users')
async def get_users_():
    """Retrieve users from the database
    """

    return get_users().__next__()
