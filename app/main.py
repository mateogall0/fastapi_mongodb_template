#!/usr/bin/env python3
from fastapi import FastAPI
from app.routes import init_routes
from app.middleware import init_middleware
from app.core.db_conn import init_db
from app.utils import DEBUG
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


# fastapi instance
app = FastAPI(debug=DEBUG,
              title='API',
              description='Fastapi and MongoDB app',
              lifespan=lifespan)
init_routes(app)
init_middleware(app)

