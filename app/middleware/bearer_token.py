#!/usr/bin/env python3
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request


class BearerTokenMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split()[1]
            self.__use_token(token)
        response = await call_next(request)
        return response
    
    def __use_token(self, token: str):
        # request.state.token = token
        pass