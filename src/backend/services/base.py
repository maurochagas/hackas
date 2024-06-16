from typing import Type, TypeVar, Generic, List, Optional
from sqlalchemy import Table # type: ignore
from sqlalchemy.sql import select # type: ignore
from pydantic import BaseModel # type: ignore
from db import database

T = TypeVar('T', bound=BaseModel)

class BaseService(Generic[T]):
    def __init__(self, model: Type[T], table: Table):
        self.model = model
        self.table = table

    async def create(self, obj_in: T) -> T:
        query = self.table.insert().values(**obj_in.dict())
        obj_id = await database.execute(query)
        return await self.get(obj_id)

    async def get(self, obj_id: int) -> Optional[T]:
        query = self.table.select().where(self.table.c.id == obj_id)
        result = await database.fetch_one(query)
        if result:
            return self.model(**result)
        return None

    async def get_all(self) -> List[T]:
        query = select(self.table)
        results = await database.fetch_all(query)
        return [self.model(**result) for result in results]

    async def update(self, obj_id: int, obj_in: T) -> Optional[T]:
        query = self.table.update().where(self.table.c.id == obj_id).values(**obj_in.dict())
        await database.execute(query)
        return await self.get(obj_id)

    async def delete(self, obj_id: int) -> bool:
        query = self.table.delete().where(self.table.c.id == obj_id)
        result = await database.execute(query)
        return bool(result)