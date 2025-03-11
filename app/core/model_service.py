#!/usr/bin/env python3
from mongoengine import Document
from typing import Type
from bson import ObjectId
from abc import ABC

class BaseService(ABC):
    def __init__(self, model: Type[Document]) -> None:
        self.model: model = model
    
    def create(self, data: dict) -> Document:
        obj = self.model(**data)
        obj.save()
        return obj
    
    def get(self, **kw) -> Document | None:
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