#!/usr/bin/env python3
from fastapi import FastAPI

from .main import main_router


def init_routes(app: FastAPI):
    app.include_router(main_router)