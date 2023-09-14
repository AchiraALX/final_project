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
            users_with_query.append({
                'username': user.username,
                'email': user.email
            })

    yield users_with_query


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


def remove_user_self(id: str) -> bool:
    """Delete a user from the database

    Return:
        Generator

    Usage:
        remove_user_self(id) -> id is the user id
    """

    session = Storage('test').new_session
    user = session.query(User).filter_by(id=id).first()

    if user is not None:
        session.delete(user)
        session.commit()

        return True

    return False


def update_user(data: dict, id: str) -> bool:
    """Update user that match the specified key
    """

    session = Storage('test').new_session
    user = session.query(User).filter_by(id=id).first()

    if user is not None:
        for key, val in data.items():
            setattr(user, key, val)
            session.commit()

        return True

    return False


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

    query = query.lower()

    blogs_with_query = []
    for blog in all_blogs():
        if query in blog.title.lower() or query in blog.content.lower():
            blogs_with_query.append({
                'author': blog.author,
                'title': blog.title,
                'content': blog.content
            })

    yield blogs_with_query


def get_blog_by(string: str) -> Generator:
    """Get one blog

    Return:
        Generator

    Usage:
        get_blog_by(string) -> string is the blog title or id
    """

    string = string.lower()

    for blog in all_blogs():
        if string in blog.title.lower() or string in blog.content.lower():
            yield {
                'author': blog.author,
                'title': blog.title,
                'content': blog.content
            }

    yield f"No result for: {string}"


def remove_blog_self(id: str) -> bool:
    """Delete a blog from the database

    Return:
        Generator

    Usage:
        remove_blog_self(id) -> id is the blog id
    """

    session = Storage('test').new_session
    blog = session.query(Blog).filter_by(id=id).first()
    if blog is not None:
        session.delete(blog)
        session.commit()

        return True

    return False


def update_blog(data: dict, id: str) -> bool:
    """Update the blog with the matching key

    Return:
        bool: True if the update went through else False

    Usage:
        update_blog(data, key) -> data is the data to be updated
        and key is the blog id
    """
    session = Storage('test').new_session
    blog = session.query(Blog).filter_by(id=id).first()
    if blog is not None:
        for key, val in data.items():
            setattr(blog, key, val)
            session.commit()

        return True

    return False
