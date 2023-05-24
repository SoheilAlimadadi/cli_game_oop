from sqlalchemy import create_engine
from sqlalchemy.orm import (
    declarative_base,
    Session
)

from painless.designs.singleton import Singleton


class SqlAlchemy(metaclass=Singleton):
    def __init__(self):
        self.engine = self.create_engine()
        self.Base = declarative_base()
        self.session = self.create_session()

    def create_engine(self):
        engine = create_engine("sqlite:///DnD.db")
        return engine

    def create_session(self):
        session = Session(self.engine)
        return session
