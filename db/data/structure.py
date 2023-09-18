#!/usr/bin/env python3

"""Structure for message
"""


class Message:
    """Class representation for messages in the database
    """

    def __init__(
        self,
        datetime,
        sender,
        receiver,
        text,
        attachments=None,
        feedback=None,
        **kwargs
    ) -> None:
        self.datetime = datetime
        self.sender = sender
        self.receiver = receiver
        self.text = text
        self.attachments = attachments or []
        self.feedback = feedback

    def to_dict(self) -> dict:
        """Return the dict representation of message"""

        return self.__dict__

    def __repr__(self) -> str:
        return "Message representation"

    def __str__(self) -> str:
        return f"Message from {self.sender}, to {self.receiver}"\
            f"at {self.datetime}:\n{self.text}"


class Metadata:
    """Metadata for message"""

    def __init__(self, database, collection, directory) -> None:
        self.database = database
        self.collection = collection
        self.directory = directory

    def to_dict(self) -> dict:
        """return the dictionary representation of metadata"""
        return self.__dict__

    def __str__(self) -> str:
        return "Convert to a dict"
