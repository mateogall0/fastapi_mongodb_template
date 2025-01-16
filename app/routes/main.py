#!/usr/bin/env python3
from fastapi import APIRouter, status, HTTPException

main_router = APIRouter(tags=['Main'])

@main_router.get('/', status_code=status.HTTP_200_OK)
async def get_main():
    return