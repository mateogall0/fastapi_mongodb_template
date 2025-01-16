#!/usr/bin/env python3
from fastapi import FastAPI
from app.routes import init_routes

app = FastAPI()

init_routes(app)