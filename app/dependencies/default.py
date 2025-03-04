#!/usr/bin/env python3
from fastapi import Depends
from .token import get_user_from_token
from . import security

def get_user(authorization = Depends(security)):
    return get_user_from_token(authorization.credentials)