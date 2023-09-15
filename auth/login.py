#!/usr/bin/env python3

"""Login view handle
"""

from quart import (
    Blueprint,
    render_template,
    Response,
    request,
    make_response
)

from auth.authenticate import Auth
from db.storage import Storage
from db.models.user import User


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

    password = (await request.form).get('password')
    username = (await request.form).get('username')

    if password is not None and username is not None:
        auth = Auth()
        if auth.login(username=username, password=password):
            storage = Storage('test').new_session
            user = storage.query(User).filter_by(username=username).first()
            if user is not None:
                response = await make_response(f"Logged in at: {user.session_token}")
                response.set_cookie('session', user.session_token)

                return response

    return f"Failed to log in {username} with key: {password}"


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


@login.route('/reset-password', strict_slashes=False, methods=['GET'])
async def initiate_reset_password() -> str:
    """Initiates the password reset process
    """

    username = (await request.form).get('username')
    if username is not None:
        auth = Auth()
        if auth.reset_password(username=username):
            return f"Reset password initiated for {username}"

        return f"Failed to initiate password reset for {username}"

    return f"Username must be provided!! ): "


@login.route('/update-password/<token>', strict_slashes=False, methods=['PUT'])
async def update_password(token) -> str:
    """Updates the password with the valid reset token
    """

    password = (await request.form).get('password')

    if password is not None:
        auth = Auth()
        if auth.updated_password(token=token, new_pass=password):
            return f"Pass was updated as successfully"

        return f"Failed to update password"

    return f"Password must be provided!! ): "


@login.route('/logout/<token>', strict_slashes=False, methods=['GET'])
async def logout(token) -> str:
    """Logs a user out
    """

    auth = Auth()
    if auth.logout(token=token):
        return f"Logged out"

    return f"Some issue is preventing logging out."
