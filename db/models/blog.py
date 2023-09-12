#!/usr/bin/env python3

"""Blog model
"""

from sqlalchemy import String, Text
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from db.models.base import Base


class Blog(Base):
    """Blog model class
    """

    __tablename__ = 'blogs'

    title: Mapped[str] = mapped_column(
        String(1000),
        nullable=False,
    )
    content: Mapped[str] = mapped_column(
        Text(50000)
    )
    author: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    def __repr__(self) -> str:
        return f"(<id>: {self.id})\n"
    "-->Title: {self.title}\n-->Content: {self.content}"


if __name__ == "__main__":
    blog = Blog(
        title="My first blog",
        content="My first blog's content",
        author="achira"
    )

    print(blog.__repr__())
