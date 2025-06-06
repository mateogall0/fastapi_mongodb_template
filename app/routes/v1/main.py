#!/usr/bin/env python3
from fastapi import APIRouter

main_router = APIRouter(tags=['Main'])

@main_router.get('/', status_code=200)
async def get_main():
    pass