from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import database
from ..repository import voting_repo
# Ganti baris import schema menjadi seperti di bawah ini:
from ..schemas import voting_schema as schemas 

router = APIRouter(prefix="/api", tags=["Voting"])

@router.post("/users/")
def register(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return voting_repo.create_user(db, user)

@router.post("/polls/")
def create_poll(poll: schemas.PollCreate, db: Session = Depends(database.get_db)):
    return voting_repo.create_poll(db, poll)

@router.post("/votes/")
def vote(vote: schemas.VoteCreate, db: Session = Depends(database.get_db)):
    res = voting_repo.submit_vote(db, vote)
    if not res:
        raise HTTPException(status_code=400, detail="Kamu sudah voting!")
    return {"message": "Vote berhasil"}