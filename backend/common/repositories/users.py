from sqlalchemy import select
from backend.common.models.user import User
from sqlalchemy.orm import Session


def get_user(db: Session, id: int):
    user = db.execute(select(User).where(User.id == id))
    if user:
        return user
    return None
