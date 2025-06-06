from fastapi import APIRouter
from .main import main_router


api_v1_router = APIRouter(prefix='/v1', tags=['/v1'])

api_v1_router.include_router(main_router)
