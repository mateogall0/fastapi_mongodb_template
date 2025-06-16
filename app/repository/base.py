from app.core.models import Base
from datetime import datetime, timezone
from bson import ObjectId


def ignore_none_filter(func):
    async def wrapper(self, _ignore_none=False, **kw):
        if _ignore_none:
            kw = clear_nones(kw)
        return await func(self, **kw)
    return wrapper

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

    @ignore_none_filter
    async def get(self, **kw) -> Base | None:
        try:
            return await self.model.find_one(kw)
        except:
            return None

    @ignore_none_filter
    async def get_many(self, **kw) -> list[Base]:
        try:
            cursor = self.model.find(kw)
            return await cursor.to_list()
        except:
            return []

    async def get_by_id(self, id) -> Base | None:
        try:
            id = ObjectId(id)
        except:
            return None
        return await self.get(_id=id)

    async def update(self, doc: Base, data: dict) -> Base:
        data['updated_at'] = datetime.now(timezone.utc)
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

