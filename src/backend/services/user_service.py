from pydantic import BaseModel # type: ignore
from models.user import users
from services.base import BaseService

class UserCreate(BaseModel):
    username: str
    email: str
    full_name: str

class User(BaseModel):
    id: int
    username: str
    email: str
    full_name: str

user_service = BaseService[User](User, users)