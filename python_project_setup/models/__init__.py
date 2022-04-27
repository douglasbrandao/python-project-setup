from python_project_setup.db import Connection

from .user import User
from .tweet import Tweet

Base = Connection.get_base()
