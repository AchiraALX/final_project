#!/usr/bin/env python3

"""Main API
"""

from quart import Blueprint, render_template, request
from workers.workers import (
    get_user_by,
    get_blog_by,
    users_with_matching_query,
    blogs_with_matching_query,
    remove_user_self,
    remove_blog_self,
    update_user,
    update_blog,
    all_blogs,
    get_blog_by_id
)
from auth.authenticate import Auth

from typing import Generator


api = Blueprint("api", __name__)


@api.route('/', strict_slashes=False, methods=['GET'])
async def api_main():
    """API Home
    """

    return await render_template('api.html', title='API')


@api.route('/user/<username>', strict_slashes=False, methods=['GET'])
@api.route('/user', strict_slashes=False, methods=['GET'])
async def get_user() -> dict[str, str] | str | Generator:
    """Get my users
    """

    string = (await request.form).get('query')

    user = get_user_by(string=str(string))

    return user.__next__()


@api.route('/users', strict_slashes=False, methods=['GET'])
@api.route('/users/<query>', strict_slashes=False, methods=['GET'])
async def user_matching_query(query: str = '') -> str:
    """Gets user that match the query

    Route:
        /users/<query> where query = username or email
    """

    if not query:
        query = (await request.form).get('query').__str__()

    users = users_with_matching_query(query=str(query)).__next__()

    return users


@api.route('/user-update/<key>', strict_slashes=False, methods=['PUT'])
async def user_update(key: str) -> str:
    """Update the user that matches key

    Return:
        str
    """

    username = (await request.form).get('username')
    email = (await request.form).get('email')
    password = (await request.form).get('password')

    data = {
        'username': username,
        'email': email,
        'password': password,
    }

    if not key:
        return f"Parameter 'key: str' should be specified."

    user = update_user(data=data, id=key)
    if user:
        return f"<< {username} >> was updated as successfully"

    return f"An error occurred while updating"


# Destroy  a user
@api.route('/destroy-user/<id>', strict_slashes=False, methods=['DELETE'])
async def destroy_profile(id: str = '') -> str:
    """Delete the user's profile
    """

    if not id or id.strip() == '':
        return f"the parameter id is required"

    if remove_user_self(id=id):
        return f"Deleted user with id << {id} >> as successfully."

    return f"Unable to resolve the deletion of: {id}"


# ----------------------------------------------------------------------------
#
# ---------------------------- Blog Routes -----------------------------------
#
# -----------------------------------------------------------------------------

# Get all blogs
@api.route('/all-blogs', strict_slashes=False, methods=['GET'])
async def get_all_blogs() -> list:
    """Retrieve all blogs
    """

    return [{
        'id': blog.id,
        'author': blog.author,
        'title': blog.title,
        'content': blog.content
    } for blog in all_blogs()]


# Create a blog
@api.route('/add-blog', strict_slashes=False, methods=['POST'])
async def add_blog():
    """Add a blog to a database
    """

    auth = Auth()

    title = (await request.form).get('title')
    content = (await request.form).get('content')
    author = (await request.form).get('author')

    details = {
        'title': title,
        'content': content,
        'author': author
    }

    return auth.create_blog(**details)


# Get a blog
@api.route('/blog', strict_slashes=False, methods=['GET'])
@api.route('/blog/<query>', strict_slashes=False, methods=['GET'])
async def get_blog(query: str = '') -> dict:
    """Retrieve a blog that matches the id provided
    """

    if not query:
        query = (await request.form).get('query').__str__()

    return get_blog_by(string=query).__next__()


# Ge blog by id
@api.get('/blogged/<id>')
async def get_one_blog(id: str):
    '''Retrieve one blog by id'''

    try:
        blog = get_blog_by_id(string_id=id).__next__()

    except StopIteration:
        return 'Max iteration reached'

    return blog


@api.get('/author')
async def get_author():
    '''Get user via the sess'''

    session_cookie = request.cookies.get('session')

    if not session_cookie or session_cookie is None:
        return {
            'cookie': None
        }

    else:
        return {
            'cookie': session_cookie
        }


# Get blogs with matching query
@api.route('/blogs', strict_slashes=False, methods=['GET'])
@api.route('/blogs/<query>', strict_slashes=False, methods=['GET'])
async def match_blogs(query: str = ''):
    """Get all blogs that match query
    """

    if not query:
        query = (await request.form).get('query').__str__()

    blogs = blogs_with_matching_query(query=query)

    return next(blogs)


# Update Blog
@api.route('/blog-update/<key>', strict_slashes=False, methods=['PUT'])
async def blog_update(key: str) -> str:
    """Update the blog that matches key

    Return:
        str
    """

    title = (await request.form).get('title')
    content = (await request.form).get('content')

    data = {
        'title': title,
        'content': content
    }

    if not key:
        return f"Key should be specified"

    update = update_blog(data=data, id=key)
    if update:
        return f"<< {title} >> was updated as successfully"

    return f"Something went wrong: Title: {title}. --> Content: {content}, {key}"

# Destroy a blog


@api.route('/destroy-blog/<id>', strict_slashes=False, methods=['DELETE'])
async def destroy_blog(id: str) -> str:
    """Deletes a a blog that matches the id provided

    Return:
        str
    """

    if remove_blog_self(id=id):
        return f"Deleted << {id} >> as successfully."

    return f"An error occurred while deleting: {id}"
