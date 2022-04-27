from sqlalchemy.orm import Session

from python_project_setup.models import User
from python_project_setup.schemas import user


def get_by_id(session: Session, user_id: int):
    with session as sess:
        return sess.query(User).filter(User.id == user_id).first()


def get_all(session: Session):
    with session as sess:
        return sess.query(User).all()


def create(session: Session, user: user.UserCreateSchema):
    with session as sess:
        new_user = User(
            name=user.name, 
            email=user.email, 
            password=user.password
        )
        sess.add(new_user)
        sess.commit()
        return new_user
