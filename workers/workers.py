#!/usr/bin/env python3

"""The workers
"""

from db.storage import Storage
from db.models.user import User
from db.models.blog import Blog

from typing import Generator
from sqlalchemy.exc import NoResultFound


def _sum(a: int | float, b: int | float) -> int | float:
    """Add a to b

    Return:
        sum float or integer
    """

    return a + b


# ----------------------------------------------------------------------------
#
# ------------------- These are user workers ---------------------------------
#
# ----------------------------------------------------------------------------


def all_users() -> Generator:
    """Get all users

    Return:
        Generator

    Usage:
        all_users()
    """

    users = Storage('test').new_session.query(User).all()

    for user in users:
        yield user


def users_with_matching_query(query: str) -> Generator:
    """Gets user whose email or username match the query

    Return:
        Generator

    Usage:
        users_with_matching_query(query) -> query is the email or username
    """

    users_with_query = []
    for user in all_users():
        if user.email == query or user.username == query:
            users_with_query.append(user)

    for user in users_with_query:
        yield user


def get_user_by(string: str) -> Generator:
    """Get one user that matches string

    Return:
        Generator

    Usage:
        get_user_by(string) -> string is the email or username
    """

    for user in all_users():
        if user.email == string or user.username == string:
            yield {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }

    yield f"No user with the email specified parameter: {string}"


def remove_user_self(id: str) -> Generator:
    """Delete a user from the database

    Return:
        Generator

    Usage:
        remove_user_self(id) -> id is the user id
    """

    for user in all_users():
        if user.id == id or user.username == id:
            Storage('test').new_session.delete(user)
            Storage('test').new_session.commit()
            yield f"User with id: {id} deleted successfully"

    yield f"No user with the id specified parameter: {id}"


def update_user(data: dict, key: str) -> Generator:
    """Update user that match the specified key
    """

    for user in all_users():
        if user.id == key or user.username == key:
            for key, value in data.items():
                setattr(user, key, value)
                Storage('test').new_session.commit()

                yield f"Updated user with username: {user.username}"

    yield f"No user with the specified key parameter: {key}"


# ----------------------------------------------------------------------------
#
# ------------------- These are blog workers ---------------------------------
#
# ----------------------------------------------------------------------------


def all_blogs() -> Generator:
    """Get all blogs

    Return:
        Generator

    Usage:
        all_blogs()
    """

    blogs = Storage('test').new_session.query(Blog).all()

    for blog in blogs:
        yield blog


def blogs_with_matching_query(query: str) -> Generator:
    """Get all blogs the match the query

    Return:
        Generator

    Usage:
        blogs_with_matching_query(query) -> query is the blog title or id
    """

    blogs_with_query = []
    for blog in all_blogs():
        if blog.title == query or blog.id == query:
            blogs_with_query.append(blog)

    for blog in blogs_with_query:
        yield blog


def get_blog_by(string: str) -> Generator:
    """Get one blog

    Return:
        Generator

    Usage:
        get_blog_by(string) -> string is the blog title or id
    """

    for blog in all_blogs():
        if blog.title == string or blog.id == string:
            yield {
                'id': blog.id,
                'title': blog.title,
                'content': blog.content
            }

    yield f"No blog with the title specified parameter: {string}"


def remove_blog_self(id: str) -> Generator:
    """Delete a blog from the database

    Return:
        Generator

    Usage:
        remove_blog_self(id) -> id is the blog id
    """

    for blog in all_blogs():
        if blog.id == id or blog.title == id:
            Storage('test').new_session.delete(blog)
            Storage('test').new_session.commit()
            yield f"Blog with id: {id} deleted successfully"

    yield f"No blog with the id specified parameter: {id}"


def blog_update(data: dict, key: str) -> bool:
    """Update the blog with the matching key

    Return:
        bool: True if the update went through else False

    Usage:
        blog_update(data, key) -> data is the data to be updated
        and key is the blog id
    """

    for blog in all_blogs():
        if blog.id == key:
            blog.title = data['title']
            blog.content = data['content']
            Storage('test').new_session.commit()
            return True

    return False
