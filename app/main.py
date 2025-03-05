#!/usr/bin/env python3
from fastapi import FastAPI
from app.routes import init_routes
from app.middleware import init_middleware
import app.conn
from app.utils import DEBUG

app = FastAPI(debug=DEBUG,
              title='API',
              description='Fastapi and MongoDB app')


init_routes(app)
init_middleware(app)