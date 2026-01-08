from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class PollCreate(BaseModel):
    title: str
    description: str
    creator_id: int

class VoteCreate(BaseModel):
    poll_id: int
    user_id: int
    choice: str