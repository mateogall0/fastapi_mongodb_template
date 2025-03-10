#!/usr/bin/env python3
from mongoengine import Document
from typing import Type
from bson import ObjectId
from abc import ABC
from app.utils.doc import doc_existence

class BaseService(ABC):
    def __init__(self, model: Type[Document]) -> None:
        self.model: model = model
    
    def create(self, data: dict) -> Document:
        obj = self.model(**data)
        obj.save()
        return obj
    
    def get(self, id: ObjectId) -> Document | None:
        return doc_existence(ObjectId(id), self.model)
    
    def delete(self, id: ObjectId) -> bool:
        obj = self.get(id)
        if obj:
            obj.delete()
            return True
        return False