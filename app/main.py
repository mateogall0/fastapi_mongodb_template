#!/usr/bin/env python3
from fastapi import FastAPI
from app.routes import init_routes
import app.conn
app = FastAPI()


init_routes(app)