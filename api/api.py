#!/usr/bin/env python3

"""Main API
"""

from quart import Blueprint, render_template


api = Blueprint("api", __name__)


@api.route('/', strict_slashes=False)
async def api_main():
    """API Home
    """

    return await render_template('api.html')
