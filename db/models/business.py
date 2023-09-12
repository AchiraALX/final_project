#!/usr/bin/env python3

"""Business profile
"""

from db.models.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Storage:
    """Structure database
    """

    def __init__(self, db_name: str) -> None:
        self.engine = create_engine(f'sqlite://{db_name}')

        Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)

    @property
    def new_session(self):
        """Return a new session
        """

        return sessionmaker(bind=self.engine)

    def __repr__(self) -> str:
        return "I am the database handler for the SQL"
