#!/usr/bin/env python3

"""The Structure database storage
"""

from db.models.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from db.models.blog import Blog
from db.models.business import Business
from db.models.user import User
from sqlalchemy.exc import NoResultFound
from custom.exceptions.exceptions import StringEmptyError


class Storage:
    """Structure database storage
    """

    available_models = {
        'user': User,
        'blog': Blog,
        'business': Business
    }

    def __init__(self, database: str) -> None:
        self.__engine = create_engine(f"sqlite:///db/{database}.sqlite3")

        # Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)

        self.__session = Session(bind=self.__engine)

    @property
    def new_session(self):
        """Return new session"""

        return self.__session

    def add_to_database(self, data: dict, model: str) -> Blog | User | Business | None:
        """Add data to a database
        """
        match model:
            case 'blog':
                obj = Blog(**data)
            case 'user':
                obj = User(**data)
            case 'business':
                obj = Business(**data)
            case _:
                obj = None

        session = self.new_session
        if obj is not None:
            session.add(obj)
            session.commit()

        return obj

    def update_object(self, obj: Blog | User) -> Blog | User:
        """Update object in the db
        """

        session = self.new_session
        session.add(obj)
        session.flush()
        session.commit()

        return obj

    def __repr__(self) -> str:
        return f"(<Database engine at: {self.__engine}>)"


if __name__ == "__main__":
    storage = Storage('test')
    print(storage.__repr__())
