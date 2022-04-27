from fastapi import Depends, FastAPI, HTTPException

from sqlalchemy.orm import Session
from python_project_setup.schemas import user, tweet
from python_project_setup.db import Connection
from python_project_setup.crud import users, tweets
from typing import List

app = FastAPI()


@app.get('/users', response_model=List[user.UserSchema])
def get_users(session: Session = Depends(Connection.get_session)):
    return users.get_all(session=session)


@app.post('/users', response_model=user.UserSchema)
def create_user(user: user.UserCreateSchema, session: Session = Depends(Connection.get_session)):
    return users.create(session=session, user=user)


@app.get('/tweets/{user_id}', response_model=List[tweet.TweetSchema])
def get_tweets_from_user(user_id: int, session: Session = Depends(Connection.get_session)):
    return tweets.get_all_from_user(session=session, user_id=user_id)


@app.post('/tweets', response_model=tweet.TweetSchema)
def create_tweet(tweet: tweet.TweetCreateSchema, session: Session = Depends(Connection.get_session)):
    user = users.get_by_id(session=session, user_id=tweet.user_id)
    if not user:
        raise HTTPException(status_code=400, detail="User does not exist in the database")
    return tweets.create(session=session, tweet=tweet)