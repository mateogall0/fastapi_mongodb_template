#!/usr/bin/env python
from app.models import Base
from fastapi import HTTPException


def doc_existence(id: str, document) -> Base | None:
    try:
        return document.objects.get(id=id)
    except:
        return None

def check_doc_input(id: str, document) -> Base:
    d = doc_existence(id, document)
    if not d:
        raise HTTPException(404, detail=f'{document.__name__} not found')
    return d
