from datetime import datetime
from python_project_setup.db.connection import Connection
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Tweet(Connection.get_base()):

    __tablename__ = 'tweets'

    id = Column(Integer, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    content = Column(String(280), nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    user = relationship('User', back_populates='tweets')

    def __repr__(self) -> str:
        return f'Tweet(content={self.content}, created_at={self.created_at}, \
                 updated_at={self.updated_at})'