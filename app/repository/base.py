from app.core.models import Base

class BaseRepository:
    """
    Base CRUD.
    """
    def __init__(self, model: Base) -> None:
        self.model = model

    def create(self, data: dict) -> Base:
        obj = self.model(**data)
        obj.save()
        return obj
    
    def get(self, _ignore_none=False, **kw) -> Base | None:
        if _ignore_none:
            kw = clear_nones(kw)
        try:
            return self.model.objects.get(**kw)
        except:
            return None

    def get_many(self, _ignore_none=False, **kw) -> list[Base]:
        if _ignore_none:
            kw = clear_nones(kw)
        try:
            return self.model.objects(**kw)
        except:
            return []

    def update(self, doc: Base, data: dict) -> Base:
        doc.update(**data)
        doc.reload()
        return doc

    def delete(self, doc) -> bool:
        if doc:
            doc.delete()
            return True
        return False

    def delete_where(self, **kw) -> bool:
        obj = self.get(**kw)
        if obj:
            obj.delete()
            return True
        return False
