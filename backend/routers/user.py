from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.db import get_session
from backend.models.user import User

router = APIRouter(prefix="/api")

class UserCreateRequest(BaseModel):
    username: str

@router.post("/user", status_code=status.HTTP_201_CREATED)
async def create_user(
    user_req: UserCreateRequest,
    session: AsyncSession = Depends(get_session)
):
    q = await session.execute(select(User).where(User.username == user_req.username))
    existing_user = q.scalars().first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = User(username=user_req.username)
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return {"message": "User created", "user_id": new_user.id}
