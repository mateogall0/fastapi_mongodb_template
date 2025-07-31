from app.core.repositories import Repository
from app.core.usecases import Service


class CRUDService(Service):
    def __init__(self, repo: Repository):
        self.repo: Repository = repo

    async def create(self, data: dict):
        return await self.repo.create(data)

    async def get(self, id: str):
        return await self.repo.get_by_id(id)

    async def update(self, obj, data: dict):
        return await self.repo.update(obj, data)

    async def delete(self, obj):
        return await self.repo.delete(obj)

    async def search(self, skip=0, limit=100, **kw):
        return await self.repo.search(skip=skip, limit=limit, **kw)
