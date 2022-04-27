from datetime import datetime
from python_project_setup.db.connection import Connection
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship


class User(Connection.get_base()):

    __tablename__ = 'users'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False)
    password = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    tweets = relationship('Tweet', back_populates='user')

    def __repr__(self) -> str:
        return f'User(name={self.name}, email={self.email}, \
                 created_at={self.created_at}, updated_at={self.updated_at})'
