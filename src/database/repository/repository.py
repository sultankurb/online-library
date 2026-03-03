from sqlalchemy import select, insert, update, delete
from src.database.connection import session
from .base import AbstractRepository
from src.database.models.base import Base
from typing import Any


class SQLAlchemyRepository(AbstractRepository):
    def __init__(self, model: Base | Any):
        self.model = model

    async def select_all(self, filters: dict):
        async with session() as s:
            stmt = select(self.model).filter_by(**filters)
            result = await s.execute(stmt)
            return result.scalars()

    async def select_one(self, filters: dict):
        async with session() as s:
            stmt = select(self.model).filter_by(**filters)
            result = await s.execute(stmt)
            return result.scalar()

    async def insert_one(self, data: dict):
        async with session() as s:
            stmt = insert(self.model).values(**data)
            await s.execute(stmt)
            await s.commit()

    async def update_one(self, data: dict, pk: int):
        async with session() as s:
            stmt = update(self.model).where(pk=pk).values(**data)
            await s.execute(stmt)
            await s.commit()

    async def delete_one(self, pk: int):
        async with session() as s:
            stmt = delete(self.model).where(pk=pk)
            await s.execute(stmt)
            await s.commit()
