#!/usr/bin/env python3


"""Graphene type for the project
"""

from db.storage import Storage
from db.models.user import User
from db.models.blog import Blog
from db.models.business import Business
from graphene import (
    ObjectType,
    String,
    List
)
from typing import Generator

storage = Storage('test')


class BusinessType(ObjectType):
    """Business model graphene object type
    """

    id = String()
    name = String()
    region = String()
    owner = String()
    blogs = List(String)


class BlogType(ObjectType):
    """Blog model graphene object type
    """

    id = String()
    title = String()
    content = String()
    author = String()


class UserType(ObjectType):
    """user model graphene object type
    """

    id = String()
    username = String()
    email = String()


class Query(ObjectType):
    """Queries
    """

    users = List(UserType)
    blogs = List(BlogType)
    business = List(BusinessType)

    def resolve_users(self, info) -> Generator:
        """List of users
        """

        yield storage.new_session.query(User).all()

    def resolve_blogs(self, info) -> Generator:
        """List of blogs
        """

        yield storage.new_session.query(Blog).all()

    def resolve_business(self, info) -> Generator:
        """List for businesses
        """

        yield storage.new_session.query(Business).all()

    def __repr__(self) -> str:
        return "Resolvers"
