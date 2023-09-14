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

    def delete_object(self, filter_id: dict, model: str) -> None:
        """Delete an object from the database
        """

        if not filter_id or not model:
            raise StringEmptyError

        session = self.new_session
        try:
            session.query(self.available_models[model]).filter_by(
                **filter_id).delete()
            session.commit()

        except NoResultFound:
            raise NoResultFound("No result found")

        finally:
            session.close()

    def update_object(self, filter_id: dict, model: str, data: dict) -> None:
        """Update an object from the database
        """

        if not filter_id or not model:
            raise StringEmptyError

        session = self.new_session
        try:
            session.query(self.available_models[model]).filter_by(
                **filter_id).update(**data)
            session.commit()

        except NoResultFound:
            raise NoResultFound("No result found")

        finally:
            session.close()

    def get_object(self, filter_id: dict, model: str) -> object:
        """Retrieve object from database
        """
        session = self.new_session
        try:
            obj = session.query(self.available_models[model]).filter_by(
                **filter_id
            ).first()

            if obj is None:
                return "Purely none"

        except NoResultFound:
            raise NoResultFound('No entries available at the moment')

    def get_user_by(self, filters: dict) -> object:
        """Get a single user
        """

        session = self.new_session
        user = session.query(User).filter_by(**filters).first()

        if user is None:
            return 'Purely user empty'

        return ""

    def __repr__(self) -> str:
        return f"(<Database engine at: {self.__engine}>)"


if __name__ == "__main__":
    storage = Storage('test')
    print(storage.__repr__())
