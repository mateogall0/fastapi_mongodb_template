#!/usr/bin/env python3
from fastapi import Depends
from app.core.utils import decode_payload
from fastapi import HTTPException
from fastapi.security import HTTPBearer as FastapiHTTPBearer


class HTTPBearer(FastapiHTTPBearer):
    """
    Custom HTTPBearer that handles lack of bearer token as a `401` status code
    for easier authentication responses. Otherwise this would occupy the `403`
    staus code.
    """
    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials:
        authorization: str = request.headers.get("Authorization")
        if not authorization:
            raise HTTPException(status_code=401, detail="Authorization header missing")
        return await super().__call__(request)

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
