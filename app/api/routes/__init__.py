from fastapi import FastAPI
from .v1 import api_v1_router


def init_routes(app: FastAPI):
    app.include_router(api_v1_router)
