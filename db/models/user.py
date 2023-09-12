#!/usr/bin/env python3

"""User model
"""

from db.models.base import Base
from db.models.blog import Blog
from db.models.business import Business
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(Base):
    """User class
    """

    __tablename__ = 'users'

    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    password: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    password_reset_token: Mapped[str] = mapped_column(
        String(100),
        default=None
    )

    session_token: Mapped[str] = mapped_column(
        String(100),
        default=None
    )

    # Relationships
    blogs: Mapped[str] = relationship(
        Blog,
        back_populates='user_blogs',
        uselist=True,
        cascade='all, delete, delete-orphan'
    )

    business: Mapped[str] = relationship(
        Business,
        back_populates='user_business',
        uselist=True,
        cascade='all, delete, delete-orphan'
    )

    def __repr__(self) -> str:
        return f"(<username: {self.username}>)\n--> Email: {self.email}"
