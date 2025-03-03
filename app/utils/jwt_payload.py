#!/usr/bin/env python3
from datetime import datetime, timedelta
import jwt
from app.config import settings
from fastapi import HTTPException, status


def encode_payload(id: str, days=0, hours=1, minutes=0, t_type='session') -> str:
    iat = datetime.utcnow()
    exp = iat + timedelta(days=days, hours=hours, minutes=minutes)
    payload = {
        'iat': iat,
        'exp': exp,
        'user_id': id,
        'type': t_type,
    }
    token = jwt.encode(payload, settings.SECRET_KEY_JWT)
    return token

def decode_payload(token: str) -> dict:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY_JWT, algorithms=["HS256"])
        if payload is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        return payload
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)