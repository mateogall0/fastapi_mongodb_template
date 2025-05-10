#!/usr/bin/env python3
from mongoengine import Document
from app.models import Base
from abc import ABC

class BaseService(ABC):
    """
    Base CRUD.

    Services that use MongoDB are intended to be inherited from this class
    to manage different documents data.

    This is intended to be treated as a CRUD repository layer and be wrapped
    with functionalities.
    For intance: if you want to have a user creation layer, you can have a
    Mongo model as class attribute and have a register method that checks for
    email existence and manages password hashing. And finishes by creating the
    user invoking the `super().create` method with the user data.
    """
    model = Base
    
    def create(self, data: dict) -> model:
        obj = self.model(**data)
        obj.save()
        return obj
    
    def get(self, **kw) -> model | None:
        try:
            return self.model.objects.get(**kw)
        except:
            return None

    def get_many(self, **kw) -> list[model]:
        try:
            return self.model.objects(**kw)
        except:
            return []

    def update(self, doc: model, data: dict) -> model:
        doc.update(**data)
        doc.save()
        doc.reload()
        return doc

    def delete(self, **kw) -> bool:
        obj = self.get(**kw)
        if obj:
            obj.delete()
            return True
        return False
