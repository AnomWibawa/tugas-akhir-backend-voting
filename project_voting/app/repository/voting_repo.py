from sqlalchemy.orm import Session
from .. import models
from ..schemas import voting_schema as schemas # <-- Pastikan baris ini tepat seperti ini

def create_user(db: Session, user: schemas.UserCreate):
    # Password di-hash (sesuai kriteria tugas)
    new_user = models.User(username=user.username, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def create_poll(db: Session, poll: schemas.PollCreate):
    new_poll = models.Poll(title=poll.title, description=poll.description, creator_id=poll.creator_id)
    db.add(new_poll)
    db.commit()
    db.refresh(new_poll)
    return new_poll

def submit_vote(db: Session, vote: schemas.VoteCreate):
    existing = db.query(models.Vote).filter(models.Vote.user_id == vote.user_id, models.Vote.poll_id == vote.poll_id).first()
    if existing:
        return None
    new_vote = models.Vote(poll_id=vote.poll_id, user_id=vote.user_id, choice=vote.choice)
    db.add(new_vote)
    db.commit()
    return new_vote