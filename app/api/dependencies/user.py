from fastapi import Depends, Request
from app.core.exceptions import Unauthorized
from fastapi.security import HTTPBearer as FastapiHTTPBearer, HTTPAuthorizationCredentials


class HTTPBearer(FastapiHTTPBearer):
    """
    Custom HTTPBearer that handles lack of bearer token as a `401` status code
    for easier authentication responses. Otherwise this would occupy the `403`
    staus code.
    """
    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials:
        authorization: str = request.headers.get("Authorization")
        if not authorization:
            raise Unauthorized
        return await super().__call__(request)

security = HTTPBearer()

def get_user_from_token(token: str):
    raise NotImplementedError(f'Nothing to do with `{token}`')

def get_user(authorization = Depends(security)):
    return get_user_from_token(authorization.credentials)
