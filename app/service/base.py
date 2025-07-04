from app.core.repositories import Repository


class CRUDService:
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

class MongoService(CRUDService):
    async def search(self, skip=0, limit=100, filters={}):
        return await self.repo.get_many(_ignore_none=True, **filters)

