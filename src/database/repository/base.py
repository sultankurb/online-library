from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    @abstractmethod
    async def select_all(self, filters: dict):
        raise NotImplementedError

    @abstractmethod
    async def select_one(self, filters: dict):
        raise NotImplementedError

    @abstractmethod
    async def insert_one(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def update_one(self, data: dict, pk: int):
        raise NotImplementedError

    @abstractmethod
    async def delete_one(self, pk: int):
        raise NotImplementedError
