#!/usr/bin/env python3

"""Main entry to the app
"""

from quart import (
    Quart,
    render_template,
    Response
)
from views.chat_routes import chat_route
from api.api import api
from auth.login import login

from typing import Tuple

chat = Quart(__name__)

chat.register_blueprint(chat_route, url_prefix='/chat')
chat.register_blueprint(api, url_prefix='/api')
chat.register_blueprint(login, url_prefix='/auth')


@chat.route('/', strict_slashes=False)
async def chat_me() -> str:
    """Main route/ home route
    """

    return await render_template("blog.html")


@chat.errorhandler(500)
async def server_error(error) -> str | int:
    """Internal server error handler
    """
    Response.status_code = 500
    return await render_template("500.html", error=error, title=500)


@chat.errorhandler(404)
async def not_found_error(error) -> str:
    """Page not found error handler
    """
    Response.status_code = 404
    return await render_template("404.html", error=error, title=404)
