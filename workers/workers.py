#!/usr/bin/env python3

"""The workers
"""

from db.storage import Storage
from db.graph_queries import Query
from graphene import Schema
from typing import Generator
from custom.exceptions.exceptions import GraphQueryError

schema = Schema(query=Query)


def _sum(a: int | float, b: int | float) -> int | float:
    """Add a to b

    Return:
        sum float or integer
    """

    return a + b


def get_users():
    """Retrieve users from the database
    """

    yield {
        'users': [
            {
                'name': 'John Doe',
                'email': 'ed127720@student.mu.ac.ke'
            },
            {
                'name': 'Jane',
                'email': 'acitrajacobs@gmail.com'
            },
            {
                'name': 'Jack',
                'email': 'jack@gmail.com'
            },
            {
                'name': 'Jill',
                'email': 'biden@gmail.com'
            }
        ]
    }


# Execute the graphql query
def graphql(query) -> Generator:
    """Execute the graphql query
    """

    result = schema.execute(query)
    if result.errors:
        raise GraphQueryError

    yield result.data.__dict__


if __name__ == "__main__":
    storage = Storage('test')
