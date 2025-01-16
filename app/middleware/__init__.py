#!/usr/bin/env python3
from fastapi import FastAPI
from .bearer_token import BearerTokenMiddleware

def init_middleware(app: FastAPI):
    app.add_middleware(BearerTokenMiddleware)