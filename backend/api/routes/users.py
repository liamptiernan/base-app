from fastapi import APIRouter, Depends, HTTPException, status
from backend.common.repositories.users import get_user

# from backend.app.utils.user import get_current_user

from backend.common.models.user import User
from backend.common.db.__init__ import get_db


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


def get_target(id: int, db=Depends(get_db)):
    user = get_user(db, id)
    if not user:
        print("no")
        raise HTTPException(
            detail=f"User {id} Not Found", status_code=status.HTTP_404_NOT_FOUND
        )
    return user


@router.get("/{id}")
async def fetch_user(user=Depends(get_target)):
    return user
