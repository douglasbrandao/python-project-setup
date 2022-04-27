from sqlalchemy_with_alembic.db import Connection

from .user import User
from .tweet import Tweet

Base = Connection.get_base()
