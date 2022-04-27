from sqlalchemy.orm import Session

from python_project_setup.models import Tweet
from python_project_setup.schemas import tweet


def get_all_from_user(session: Session, user_id: int):
    with session as sess:
        return sess.query(Tweet).filter_by(user_id=user_id).all()


def create(session: Session, tweet: tweet.TweetSchema):
    with session as sess:
        tweet = Tweet(user_id=tweet.user_id, content=tweet.content)
        sess.add(tweet)
        sess.commit()
        return tweet
