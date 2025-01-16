#!/usr/bin/env python3
from pydantic import BaseModel

class BaseCreate(BaseModel):
    pass

class BaseResponse(BaseModel):
    class Config:
        orm_mode = True
