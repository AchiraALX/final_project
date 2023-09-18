#!/usr/bin/env python3

"""NoSQL database handler
"""

from pymongo import MongoClient

from db.data.structure import Message


class Mongo:
    """mongo handler
    """

    def __init__(self, database, collection) -> None:
        self.client = MongoClient('mongodb://0:27017'),

        self.database = self.client[database]
        self.collection = self.database[collection]

    def save(self, **kwargs) -> dict | None:
        """Save data into the database
        """

        primary = {
            'datetime': kwargs.get('datetime'),
            'sender': kwargs.get('sender'),
            'receiver': kwargs.get('receiver'),
            'text': kwargs.get('text')
        }

        secondary = {
            'attachments': kwargs.get('attachments'),
            'feedback': Message
        }

        for key, val in primary.items():
            if val is None:
                return {'error': f"Some argument missing: {key}"}

        message = Message(
            datetime=primary['datetime'],
            sender=primary['sender'],
            receiver=primary['receiver'],
            text=primary['text'],
            **secondary
        )

        return self.collection.insert_one(message.__dict__)

    def query(self, **kwargs) -> dict:
        """query database with the specified parameters
        """

        self.collection.find(**kwargs)

    def destroy(self, id: str) -> None:
        """deletes object from database
        """

    def refurbish(self, **kwargs):
        """Updates a document in the database
        """

    def __repr__(self) -> str:
        return "I am the NoSQL client handler"
