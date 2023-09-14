#!/usr/bin/env python3

"""Main entry to the app
"""

from quart import (
    Quart,
    render_template,
    Response,
    request
)
from views.chat_routes import chat_route
from api.api import api
from auth.login import login

chat = Quart(__name__)

chat.register_blueprint(chat_route, url_prefix='/chat')
chat.register_blueprint(api, url_prefix='/api')
chat.register_blueprint(login, url_prefix='/auth')

response = Response()


@chat.after_request
async def add_custom_headers(response: Response):
    """Adds custom headers
    """

    response.headers["X-Name"] = 'Achira'
    response.headers['method'] = str(request.method)

    return response


@chat.route('/', strict_slashes=False)
async def chat_me() -> str:
    """Main route/ home route
    """

    return await render_template("blog.html")


@chat.errorhandler(500)
async def server_error(error) -> str | int:
    """Internal server error handler
    """

    return await render_template("500.html", error=error, title=500)


@chat.errorhandler(404)
async def not_found_error(error) -> str:
    """Page not found error handler
    """

    return await render_template("404.html", error=error, title=404)


@chat.errorhandler(405)
async def method_not_allowed(error):
    """Not allowed method handling
    """

    return {'res': 'Not really god at this stuff'}
