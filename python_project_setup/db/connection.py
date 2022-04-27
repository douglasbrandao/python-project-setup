from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Optional


class Connection:

    __base = None
    __engine: Optional[Engine] = None
    __session_maker: Optional[sessionmaker] = None

    @classmethod
    def __configuration(cls) -> None:
        uri: str = "sqlite:///database.db"
        try:
            cls.__engine = create_engine(
                uri, 
                connect_args={"check_same_thread": False}
                )
            cls.__session_maker = sessionmaker(bind=cls.__engine, 
                                               expire_on_commit=False)
            cls.__base = declarative_base()
        except Exception as error:
            raise ConnectionException(str(error))


    @classmethod
    def get_base(cls):
        try:
            if not cls.__base:
                cls.__configuration()
            return cls.__base
        except Exception as error:
            raise ConnectionException(str(error))


    @classmethod
    def get_engine(cls) -> Optional[Engine]:
        try:
            if not cls.__engine:
                cls.__configuration()
            return cls.__engine
        except Exception as error:
            raise ConnectionException(str(error))

    
    @classmethod
    def get_session(cls) -> Optional[sessionmaker]:
        try:
            if not cls.__session_maker:
                cls.__configuration()
            return cls.__session_maker()
        except Exception as error:
            raise ConnectionException(str(error))



class ConnectionException(Exception):
    
    def __init__(self, message: str) -> None:
        self.message = message
