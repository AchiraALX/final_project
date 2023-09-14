#!/usr/bin/env python3

"""Business profile
"""

from db.models.base import Base
from db.models.blog import Blog
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Business(Base):
    """Business profile
    """

    __tablename__ = 'business'

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    region: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    # Foreign Keys
    owner: Mapped[str] = mapped_column(
        ForeignKey('users.username'),
        nullable=False
    )

    # Relationships
    blogs: Mapped[str] = relationship(
        Blog,
        back_populates='business_blogs',
        uselist=True,
    )

    user_business = relationship(
        'User',
        back_populates='business',
    )

    def __repr__(self) -> str:
        return f"(<name: {self.name}>)\n--> Owner: {self.owner}"
