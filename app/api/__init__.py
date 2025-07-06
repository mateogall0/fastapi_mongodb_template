from fastapi import FastAPI
from app.api.routes import init_routes
from .middleware import init_middleware
from contextlib import asynccontextmanager
from app.infra.db import init_db
from .exception_handler import register_exceptions


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

def init_api(app: FastAPI):
    init_routes(app)
    init_middleware(app)
    register_exceptions(app)

