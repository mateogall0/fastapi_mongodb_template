from app.core.models import Base

class BaseRepository:
    """
    Base CRUD.
    """
    def __init__(self, model: Base) -> None:
        self.model = model

    async def create(self, data: dict) -> Base:
        obj = self.model(**data)
        await obj.insert()
        return obj
    
    async def get(self, _ignore_none=False, **kw) -> Base | None:
        if _ignore_none:
            kw = clear_nones(kw)
        try:
            return await self.model.find_one(kw)
        except:
            return None

    async def get_many(self, _ignore_none=False, **kw) -> list[Base]:
        if _ignore_none:
            kw = clear_nones(kw)
        try:
            cursor = self.model.find(kw)
            return await cursor.to_list()
        except:
            return []

    async def update(self, doc: Base, data: dict) -> Base:
        await doc.update({'$set': data})
        return doc

    async def delete(self, doc) -> bool:
        if doc:
            await doc.delete()
            return True
        return False

    async def delete_where(self, **kw) -> bool:
        obj = await self.get(**kw)
        return await self.delete(obj)

