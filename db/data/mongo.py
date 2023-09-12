#!/usr/bin/env python3

"""NoSQL database handler
"""

from pymongo import MongoClient


class Mongo:
    """mongo handler
    """

    def __init__(self) -> None:
        self.connection = MongoClient()

    def __repr__(self) -> str:
        return "I am the NoSQL client handler"
