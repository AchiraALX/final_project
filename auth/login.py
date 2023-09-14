#!/usr/bin/env python3

"""Login view handle
"""

from quart import (
    Blueprint,
    render_template,
    Response,
    g,
    request,
)
from uuid import uuid4

from auth.authenticate import Auth


login = Blueprint('login', __name__)


@login.after_request
async def login_headers(response: Response) -> Response:
    """Modify headers for the login routes
    """

    response.headers['Login-Status'] = 'Logged in'

    return response


@login.route('/', strict_slashes=False, methods=['POST'])
async def logged_in():
    """Return if user logged in
    """

    password = (await request.form)['password']
    username = (await request.form).get('username')

    if str(username).lower() == "Achira".lower():
        if str(password).lower() == 'password'.lower():
            return {
                'status': 'success',
                'message': 'Logged in as successfully',
                'rest_token': str(uuid4()),
                'session_token': str(uuid4())
            }

    return {'info': 'failed'}


@login.route('/login', strict_slashes=False, methods=['GET'])
async def login_main():
    """Return login main page
    """

    return await render_template('login.html')


@login.route('/register', strict_slashes=False, methods=['GET', 'POST'])
async def sign_up() -> str | object | None:
    """Return the main sign up page
    """

    auth = Auth()

    if request.method == 'POST':
        username = (await request.form).get('username')
        email = (await request.form).get('email')
        password = (await request.form).get('password')

        return auth.create_user(
            username=username,
            email=email,
            password=password
        )

    return await render_template('sign_up.html')
