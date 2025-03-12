#!/usr/bin/env python3
from mongoengine import Document
from app.models import Base
from abc import ABC

class BaseService(ABC):
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

    
    def delete(self, **kw) -> bool:
        obj = self.get(**kw)
        if obj:
            obj.delete()
            return True
        return False