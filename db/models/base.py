#!/usr/bin/env python3

"""Base model for the structured data
"""

from sqlalchemy import String
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column
)
from uuid import uuid4


class Base(DeclarativeBase):
    """Base model
    """

    __abstract__ = True

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        nullable=False,
        default=lambda: str(uuid4())
    )
