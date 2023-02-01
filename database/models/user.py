from sqlalchemy import sql
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float
)

from database import db


class UserModel(db.Base):
    __tablename__ = 'user_account'

    def __init__(self, username, password):
        self.username = username
        self.password = password

    id = Column(
        Integer,
        primary_key=True
    )

    username = Column(
        String(255),
        nullable=False,
        unique=True
    )

    password = Column(
        String(255),
        nullable=False
    )

    role = Column(
        String(10)
    )

    won = Column(
        Integer,
        default=0
    )

    loss = Column(
        Integer,
        default=0
    )

    win_ratio = Column(
        Float,
        default=0.0
    )
