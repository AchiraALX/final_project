#!/usr/bin/env python3

"""Main entry to the app
"""

from quart import (
    Quart,
    render_template,
    Response,
    request,
    redirect,
    url_for,
    g
)
from views.chat_routes import chat_route
from api.api import api
from auth.login import login
from workers.chat_sockets import socket
from quart_cors import cors
from secrets import token_hex
from workers.workers import get_user_by_session


chat = Quart(__name__)
chat = cors(chat, allow_origin='*')
chat.secret_key = str(token_hex(32))


chat.register_blueprint(chat_route, url_prefix='/chat')
chat.register_blueprint(api, url_prefix='/api')
chat.register_blueprint(login, url_prefix='/auth')
chat.register_blueprint(socket, url_prefix='/tunnel')

response = Response()

global is_authenticated
global user

user = None
is_authenticated = None


@chat.after_request
async def add_custom_headers(response: Response):
    """Adds custom headers
    """

    global is_authenticated
    global user

    response.headers['method'] = str(request.method)
    if is_authenticated:
        response.headers['name'] = 'Authenticate'

    return response


@chat.before_request
async def auth():
    """Authenticate using cookies
    """

    global is_authenticated

    session_token = request.cookies.get('session-token')

    if session_token is not None and not session_token:
        print(session_token)
        user = get_user_by_session(
            session_id=session_token
        ).__next__()
        response.headers['Client'] = user['username']
        is_authenticated = True

    else:
        user = None

    request_uri = request.url

    if 'chat' in request_uri and session_token is None:
        print('Chat in requested resource')
        return await render_template('login.html')


@chat.route('/', strict_slashes=False)
async def chat_me() -> str:
    """Main route/ home route
    """

    global is_authenticated
    if is_authenticated:

        return await render_template("blog.html")
    else:
        return await render_template('login.html')


@chat.errorhandler(500)
async def server_error(error) -> tuple[str, int]:
    """Internal server error handler
    """

    return f"{error}", 500


@chat.errorhandler(404)
async def not_found_error(error) -> str:
    """Page not found error handler
    """

    return await render_template("404.html", error=error, title=404)


@chat.errorhandler(405)
async def method_not_allowed(error) -> tuple[str, int]:
    """Not allowed method handling
    """

    return f"{error}", 405
