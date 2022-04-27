from pydantic import BaseModel


class TweetBaseSchema(BaseModel):
    user_id: int
    content: str


class TweetCreateSchema(TweetBaseSchema):
    pass


class TweetSchema(TweetBaseSchema):
    
    class Config:
        orm_mode = True