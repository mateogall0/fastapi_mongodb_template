#!/usr/bin/env python3
from fastapi import Depends
from app.core.utils import decode_payload
from fastapi import HTTPException
from fastapi.security import HTTPBearer

security = HTTPBearer()

def get_user_from_token(token: str):
    payload = decode_payload(token)
    if payload['type'] != 'session':
        raise HTTPException(status_code=400,
                            detail='Token of type session required')
    user_id = payload['user_id']
    """
    User deserialization logic here
    """
    raise NotImplementedError()

def get_user(authorization = Depends(security)):
    return get_user_from_token(authorization.credentials)
