from fastapi import APIRouter, HTTPException # type: ignore
from typing import List
from services.user_service import user_service, User, UserCreate

router = APIRouter()

@router.post("/", response_model=User)
async def create_user(user: UserCreate):
    return await user_service.create(user)

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    user = await user_service.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/", response_model=List[User])
async def get_users():
    return await user_service.get_all()

@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserCreate):
    return await user_service.update(user_id, user)

@router.delete("/{user_id}", response_model=bool)
async def delete_user(user_id: int):
    return await user_service.delete(user_id)