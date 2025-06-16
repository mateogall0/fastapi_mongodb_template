#!/usr/bin/env python3
from fastapi import APIRouter
from app.handlers import main


main_router = APIRouter(tags=['Main'])

main_router.get('/', status_code=200)(main.get_main_handler)
