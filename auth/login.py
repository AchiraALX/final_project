#!/usr/bin/env python3

"""Login view handle
"""

from quart import Blueprint, render_template


login = Blueprint('login', __name__)


@login.route('/', strict_slashes=False)
async def login_main():
    """Return login main page
    """

    return await render_template('login.html')


@login.route('/register', strict_slashes=False)
async def sign_up():
    """Return the main sign up page
    """

    return await render_template('sign_up.html')
