from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..db import get_session
from ..models.user import User
from pydantic import BaseModel

router = APIRouter()

class UserCreateRequest(BaseModel):
    username: str

@router.post("/user", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreateRequest, session: AsyncSession = Depends(get_session)):
    # Check if user already exists
    result = await session.execute(select(User).where(User.username == user.username))
    existing_user = result.scalars().first()
    if existing_user:
        return {"message": "User already exists"}  # Return 200 OK

    # Create new user
    new_user = User(username=user.username)
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return {"message": "User created successfully", "user": {"id": new_user.id, "username": new_user.username}}
