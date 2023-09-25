#!/usr/bin/env python3

"""Login view handle
"""

from datetime import datetime, timedelta
from quart import (
    Blueprint,
    render_template,
    request,
    flash,
    redirect,
    url_for,
    make_response
)

from auth.authenticate import Auth

from typing import Union


login = Blueprint('login', __name__)


@login.route('/', strict_slashes=False, methods=['POST', 'GET'])
async def logged_in():
    """Return if user logged in
    """

    if request.method == 'POST':
        password = (await request.form).get('password')
        username = (await request.form).get('username')

        if password is not None and username is not None:
            auth = Auth()
            token = auth.login(username=username, password=password)
            if token is not None:
                expiration_time = datetime.utcnow() + timedelta(hours=48)
                response = await make_response(
                    redirect(url_for('socket.chat_home')))

                response.set_cookie('session-token', token,
                                    expires=expiration_time)

                return response

        await flash(f"username: {username} and password: {password} does not match")
        return redirect(url_for('login.login_main'))

    else:
        return await render_template('login.html')


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
        confirm_password = (await request.form).get('confirm-password')

        print(username, email, password, confirm_password)

        if confirm_password != password:
            await flash('Passwords not matching')
            return redirect(url_for('login.sign_up'))

        _ = auth.create_user(
            username=username,
            email=email,
            password=password
        )

        if _ is not None:
            await flash("User created, you can login")
            return redirect(url_for('login.login_main'))

        else:
            await flash("Error occurred while adding user")

    return await render_template('sign_up.html')


@login.route('/reset-password', strict_slashes=False, methods=['GET', 'POST'])
async def initiate_reset_password() -> str:
    """Initiates the password reset process
    """

    if request.method == 'POST':
        username = (await request.form).get('username')
        if username is not None:
            auth = Auth()
            if auth.reset_password(username=username):
                await flash(
                    'Process initiated. Follow instruction on the registered'
                    'email associated with the username you provided')

                return await render_template('update.html')

            await flash('Enter a valid username!')
            return await render_template('reset_password.html')

        return f"Username must be provided!! ): "

    return await render_template('reset_password.html')


@login.route('/update-password', strict_slashes=False, methods=['PUT'])
@login.route('/update-password/<token>', strict_slashes=False, methods=['PUT'])
async def update_password(token):
    """Updates the password with the valid reset token
    """

    password = (await request.form).get('password')
    confirm_password = (await request.form).get('confirm-password')

    if password is None or confirm_password is None:
        try:
            password = request.args.get('password')
            confirm_password = request.args.get('confirm-password')

        except Exception as e:
            await flash('Provide valid values for passwords')
            return redirect(request.url)

    if password is not None and confirm_password is not None and password == confirm_password:
        auth = Auth()
        if auth.updated_password(token=token, new_pass=password):
            return f"Pass was updated as successfully"

        return f"Failed to update password"

    return f"Password must be provided!! ): "


@login.route('/logout', strict_slashes=False, methods=['GET'])
@login.route('/logout/<token>', strict_slashes=False, methods=['GET'])
async def logout(token):
    """Logs a user out
    """

    auth = Auth()
    if not token:
        try:
            token = request.cookies.get('session-token').__str__

        except Exception:
            await flash('Invalid token')

    log = auth.logout(token=str(token))
    if log is not None:
        response = await make_response(render_template('blog.html'))
        response.delete_cookie('session-token')

        return response

    else:
        return request.referrer
