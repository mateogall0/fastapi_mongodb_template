#!/usr/bin/env python3
from mongoengine import Document
from typing import Type
from bson import ObjectId

class BaseService:
    def __init__(self, model: Type[Document]) -> None:
        self.model: model = model
    
    def create(self, data: dict) -> Document:
        obj = self.model(**data)
        obj.save()
        return obj
    
    def get(self, id: ObjectId) -> Document:
        return self.model.objects(id=ObjectId(id)).first()
    
    def delete(self, id: ObjectId) -> bool:
        obj = self.get(id)
        if obj:
            obj.delete()
            return True
        return False